from fastapi import FastAPI

app = FastAPI(
    title="Weather API",
    description="A Python-powered Weather API",
    version="1.0.0"
)

@app.get("/")
async def home():
    return {
        "message": "Welcome to Weather API",
        "status": "Running"
    }

@app.get("/Health_check")
async def ping():
    return {
        "message": "Healthyyy!!",
        "status": "Healthy"
    }