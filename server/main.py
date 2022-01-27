from fastapi import FastAPI, UploadFile, Request, File

app = FastAPI()

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    
    return {"filename": file.filename}