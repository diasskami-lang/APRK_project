from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Connection Test API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# TEST CONNECTION

@app.get("/ping")
def ping():
    return {
        "status": "success",
        "message": "Backend is connected with frontend (index.html)",
        "connection": True
    }



# MOCK REGISTER

@app.post("/register")
def register():
    return {
        "status": "success",
        "message": "Register endpoint is working (frontend connected)"
    }
