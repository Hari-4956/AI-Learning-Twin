from fastapi import FastAPI

app = FastAPI(title="AI Learning Twin API")


@app.get("/")
def home():
    return {"message": "Backend is running successfully!"}