from fastapi import FastAPI
from routers.check_alive_router import router as check_alive_router


# Initialize the FastAPI app
app = FastAPI()

# Include the router under the "/api" prefix
app.include_router(check_alive_router, prefix="/api")

# Run the server for local testing 
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)
