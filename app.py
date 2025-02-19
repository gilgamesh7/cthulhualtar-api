from fastapi import FastAPI
from routers.check_alive_router import router as check_alive_router


# Initialize the FastAPI app
app = FastAPI()

# Include the router under the "/api" prefix
app.include_router(check_alive_router, prefix="/api")
print(app.routes)

# Run the server for local testing 
if __name__ == "__main__":
    import uvicorn
    import os

    if __name__ == "__main__":
        port = int(os.getenv("PORT", 8000))  # Use Azure-assigned port
        uvicorn.run(app, host="0.0.0.0", port=port)
