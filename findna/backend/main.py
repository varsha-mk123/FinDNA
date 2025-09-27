from src.core.app import create_application
from src.core.database import engine, Base
from src.api.routers import include_api_routes

# Create tables
Base.metadata.create_all(bind=engine)

app = create_application()

# Include API routes
include_api_routes(app.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)