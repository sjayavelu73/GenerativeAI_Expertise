Python Environment
------------------

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



