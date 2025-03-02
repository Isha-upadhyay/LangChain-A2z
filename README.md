﻿# LangChain-A2z

# 🛠️ Installation & Setup

# 1️⃣ Clone the Repository
git clone https://github.com/Isha-upadhyay/LangChain-A2z.git
cd LangChain-A2z

# 2️⃣ Create a Virtual Environment (Recommended)
python -m venv venv

# Windows:
venv\Scripts\activate

# Mac/Linux:
source venv/bin/activate

# 3️⃣ Install Dependencies
pip install -r requirements.txt

# ⚙️ Environment Variables
# Create a .env file in the project root and add the following:
echo "OPENAI_API_KEY=" >> .env
echo "ANTHROPIC_API_KEY=" >> .env
echo "GOOGLE_API_KEY=" >> .env
echo "HUGGINGFACEHUB_ACCESS_TOKEN=" >> .env

# Run the Project
python project name # Adjust this command based on your project structure
