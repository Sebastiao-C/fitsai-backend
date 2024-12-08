from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Add CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://https://blue-pebble-0e2752303.4.azurestaticapps.net/",  # Add your frontend URL
        "http://localhost:5173",  # Optional: For local testing
    ],    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)
@app.get("/")
def read_root():
    return {"message": "Hello, world!"}
