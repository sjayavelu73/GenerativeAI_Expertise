I.Python Environment Creation
---------------------------------

1. mkdir fastapi-llm-api
2. cd fastapi_llm_api
3. python3 -m venv fastapi_week1
4. source fastapi_week1/bin/activate
The terminal show show fastapi_week1 
5. pip install fastapi uvicorn openai python-dotenv pydantic
6. pip freeze > requirements.txt
7. Create the directory structure inside fastapi_llm_api
      mkdir app  
      touch app/main.py (Driver ,  creates FastAPI Object , and defines endpoints)
      touch app/prompts.py (Define the prompts you want to use , test) 
      touch app/schemas.py (Pydantic Schemas)
      touch .env ( OPENAI_API_KEY )
      touch README.md    

II. Publish to Git
---------------------
1: Generate a PAT (if you haven’t already)

Go to GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)

Click “Generate new token (classic)”

Name it, e.g., fastapi-git-token

Expiration: choose 90 days (or no expiration)

Scopes: check repo

Click Generate token → copy it now (you won’t see it again)

2. cd /path/to/fastapi-llm-api
git init
git add .
git commit -m "Initial commit - FastAPI LLM API"
git remote add origin https://github.com/sjayavelu73/GenerativeAI_Expertise.git (Replace with yours)
check your remote with git remote -v


3. 
git branch -M main
git push -u origin main 
Username → your GitHub username (sjayavelu73)
Password → paste the PAT 

4. Step 4: Save credentials (so you don’t type PAT every time)
git config --global credential.helper store

5. Verify https://github.com/sjayavelu73/GenerativeAI_Expertise

As and when we make changes we will need to update the repo in Git
 
1. git status (to check the files that have changed)
2. git add . (assuming that all the files in the pwd has changed) or git add app/main.py (assuming that main.py has changed)
3. git commit -m "meaningful comment for the change"
4. git push -u origin main
