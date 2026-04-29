import shutil
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from project_gov.face_ai.main import recognize_person, add_person

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/recognize")
async def recognize(file: UploadFile = File(...)):
    path = "temp.jpg"

    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return recognize_person(path)

@app.post("/register")
async def register(
    name: str = Form(...),
    file: UploadFile = File(...)
):
    path = "temp_add.jpg"

    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    ok = add_person(name, path)

    return {"status":"success" if ok else "error"}