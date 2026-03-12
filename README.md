# Generative AI Expertise

A comprehensive guide for building and deploying a FastAPI-based LLM (Large Language Model) application with OpenAI integration.

---

## Table of Contents

- [Part I: Python Environment Setup](#part-i-python-environment-setup)
- [Part II: Git Repository Management](#part-ii-git-repository-management)
- [Part III: Ongoing Development](#part-iii-ongoing-development)

---

## Part I: Python Environment Setup

### Overview
Set up a Python virtual environment for your FastAPI LLM application with all required dependencies.

### Step-by-Step Instructions

1. **Create Project Directory**
   ```bash
   mkdir fastapi-llm-api
   cd fastapi-llm-api
   ```

2. **Create Virtual Environment**
   ```bash
   python3 -m venv fastapi_week1
   source fastapi_week1/bin/activate
   ```
   > Note: Your terminal prompt should now display `(fastapi_week1)`

3. **Install Dependencies**
   ```bash
   pip install fastapi uvicorn openai python-dotenv pydantic
   ```

4. **Generate Requirements File**
   ```bash
   pip freeze > requirements.txt
   ```

5. **Create Project Structure**
   ```bash
   mkdir app
   touch app/main.py          # Driver file: creates FastAPI object and defines endpoints
   touch app/prompts.py       # Define prompts for testing
   touch app/schemas.py       # Pydantic data models
   touch .env                 # Store OPENAI_API_KEY (never commit this)
   touch README.md
   ```

### Project Structure
```
fastapi-llm-api/
├── app/
│   ├── main.py          # FastAPI application entry point
│   ├── prompts.py       # Prompt definitions and management
│   └── schemas.py       # Pydantic schemas for request/response
├── fastapi_week1/       # Virtual environment
├── .env                 # Environment variables (DO NOT COMMIT)
├── .gitignore           # Git ignore file
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

## Part II: Git Repository Management

### Phase 1: Generate Personal Access Token (PAT)

1. Navigate to **GitHub Settings**
   - Go to GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)

2. **Create New Token**
   - Click "Generate new token (classic)"
   - Name: `fastapi-git-token` (or preferred name)
   - Expiration: 90 days (or no expiration)
   - Scopes: Check `repo` checkbox

3. **Copy Token**
   - Click "Generate token"
   - **Copy the token immediately** (you won't be able to see it again)

### Phase 2: Initialize and Push Repository

1. **Navigate to Project Directory**
   ```bash
   cd /path/to/fastapi-llm-api
   ```

2. **Initialize Git Repository**
   ```bash
   git init
   git add .
   git commit -m "Initial commit - FastAPI LLM API"
   ```

3. **Connect to Remote Repository**
   ```bash
   git remote add origin https://github.com/sjayavelu73/GenerativeAI_Expertise.git
   git remote -v  # Verify the connection
   ```

4. **Push to Main Branch**
   ```bash
   git branch -M main
   git push -u origin main
   ```
   - Username: `sjayavelu73`
   - Password: Paste your PAT (not your GitHub password)

5. **Save Credentials Locally** (Optional but Recommended)
   ```bash
   git config --global credential.helper store
   ```
   > This prevents needing to enter your PAT on every push

6. **Verify Remote**
   Visit: https://github.com/sjayavelu73/GenerativeAI_Expertise

---

## Part III: Ongoing Development

### Updating Your Repository

As you make changes to your codebase, follow these steps to keep your repository updated:

1. **Check Repository Status**
   ```bash
   git status
   ```
   > Displays modified, staged, and untracked files

2. **Stage Changes**
   ```bash
   git add .                    # Stage all changes
   # OR
   git add app/main.py          # Stage specific file
   ```

3. **Commit Changes**
   ```bash
   git commit -m "Meaningful description of changes"
   ```
   > Example: `git commit -m "Add authentication endpoint"`

4. **Push to Remote**
   ```bash
   git push -u origin main
   ```

### Recommended Workflow
```bash
git status              # Check what changed
git add .              # Stage changes
git commit -m "msg"    # Create meaningful commits
git push               # Push to remote
```

---

## Best Practices

- **Environment Variables**: Never commit `.env` files. Use `.gitignore`:
  ```
  .env
  fastapi_week1/
  __pycache__/
  *.pyc
  ```

- **Commit Messages**: Write clear, descriptive commit messages
  - ❌ Bad: `git commit -m "fix"`
  - ✅ Good: `git commit -m "Fix OpenAI API error handling"`

- **Pull Before Push**: Always pull latest changes before pushing
  ```bash
  git pull origin main
  git push origin main
  ```

## Part IV: Publish to Render 
### Overview
Render is a cloud platform that lets you easily deploy web apps, APIs, and services from your GitHub repository, making them publicly accessible without managing servers.
### Step-by-Step Instructions
Logged in to Render and clicked New → Web Service.         

Connected the GitHub repository to Render.

Configured the service:
     Environment: Python
     
     Build Command: pip install -r requirements.txt
     
     Start Command:uvicorn app.main:app --host 0.0.0.0 --port 10000
     
     Added environment variables (like OPENAI_API_KEY) on Render to replace .env.
     
     Clicked Deploy, letting Render clone the repo, install dependencies, and start the server.
     

The API became publicly accessible with documentation at /docs and /redoc.

https://fastapi-llm-api-apmc.onrender.com/

## Additional Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Git Documentation](https://git-scm.com/doc)
- [OpenAI API Reference](https://platform.openai.com/docs)
- [Pydantic Documentation](https://docs.pydantic.dev/)

---

**Last Updated**: 2026-03-12 01:29:06
