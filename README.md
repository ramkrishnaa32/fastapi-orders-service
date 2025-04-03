# fastapi-orders-service

# strating postgress
- brew services restart postgresql@14


# starting the app
lsof -i :8000
kill -9 1234
uvicorn app.main:app --reload --host 127.0.0.1 --port 8080
