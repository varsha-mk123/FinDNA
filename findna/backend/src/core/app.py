from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .config import get_settings

def create_application() -> FastAPI:
    settings = get_settings()
    
    app = FastAPI(
        title=settings.PROJECT_NAME,
        debug=settings.DEBUG,
        version=settings.VERSION
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_HOSTS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app

app = create_application()

@app.get("/")
def read_root():
    return {"message": "Welcome to Findna API"}