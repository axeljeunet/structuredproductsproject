from fastapi import FastAPI
import uvicorn
from routes import router

app = FastAPI()

def start():
    """Démarre le server FastAPI"""
    app.include_router(router)
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    start()