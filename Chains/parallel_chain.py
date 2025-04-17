from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv 
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel  #execute multiple chains in parallel

load_dotenv()

model1 = ChatGoogleGenerativeAI(model='gemini-2.0-flash')
model2 = ChatAnthropic(model='claude-3-7-sonnet-20250219')

prompt1 = PromptTemplate(
    template = 'Generate short and simple notes from the following text \n {text}',
    input_variables=['text']
)

prompt2 = PromptTemplate(
    template = 'Generate 5 short question answer from the following text \n {text}',
    input_variables=['text']
)

prompt3 = PromptTemplate(
    input_variables=["notes", "quiz"],
    template="Merge the provided notes and quiz into a single document."
)


parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'notes': prompt1 |model1 | parser,
    'quiz': prompt2 |model2 | parser
})

merge_chain = prompt3 | model1 | parser 

chain = parallel_chain | merge_chain
text = """ Support Vector Machine (SVM) is a powerful supervised machine learning algorithm commonly 
used for classification and, to a lesser extent, regression tasks. The main idea behind SVM is to find 
the optimal hyperplane that separates data points of different classes with the maximum margin. In simpler 
terms, it tries to draw the best possible boundary between categories so that the distance between the nearest
points of each class (called support vectors) and the dividing line is as large as possible. SVM is particularly 
effective in high-dimensional spaces and is versatile due to the use of kernel functions, which allow it to handle
non-linearly separable data by transforming it into a higher-dimensional space where it becomes linearly separable.
Common kernels include linear, polynomial, radial basis function (RBF), and sigmoid. Despite its strengths, such as 
robustness to overfitting in high-dimensional datasets, SVM can be computationally intensive and sensitive to parameter
tuning, especially with large datasets or noisy data.

ne of the key strengths of SVM is its ability to handle both linearly separable and non-linearly separable data. When data 
is not linearly separable, SVM employs a technique known as the kernel trick, which maps the input data into a higher-dimensional 
space where a linear separator can be found. This transformation is done using kernel functions such as linear, polynomial, radial
basis function (RBF), or sigmoid, allowing SVMs to tackle complex problems like image recognition, natural language processing, 
and bioinformatics.

Another advantage of SVM is that it is relatively memory efficient, as it only relies on a subset of the training data (the support vectors)
to make predictions. This makes it suitable for high-dimensional datasets, such as those found in text classification or genomics. However,
SVMs do have limitations. They can be computationally intensive and slow to train on large datasets, especially when using non-linear kernels.
Additionally, selecting the right kernel and tuning hyperparameters such as the regularization parameter (C) and the kernel parameters 
(like gamma for RBF) can be challenging and often requires cross-validation.

In summary, SVM is a powerful tool in the machine learning toolbox, known for its strong theoretical foundation and high accuracy in 
many real-world applications. Its ability to create complex decision boundaries while maintaining good generalization performance
 makes it a preferred choice for many classification tasks, provided the data size is manageable and the model is carefully tuned.








"""
result = chain.invoke({'text':text})
print(result)


