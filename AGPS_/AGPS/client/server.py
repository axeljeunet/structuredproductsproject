from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from routes import router

app = FastAPI()

def start():
    """Démarre le server FastAPI"""
    app.include_router(router)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # or specify allowed origins
        allow_credentials=True,
        allow_methods=["*"],  # Allow all HTTP methods
        allow_headers=["*"],
    )
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    start()