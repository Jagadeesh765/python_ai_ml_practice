from fastapi import FastAPI,UploadFile,File,Form
import shutil
app = FastAPI()
notes=[]
@app.post("/notes/")
async def create_note(
    title:str=Form(...),
    content:str=Form(...),
    file:UploadFile=File(...)
):
    file_path=f"C:/Users/raavi/OneDrive/Desktop/{file.filename}"
    with open(file_path,"wb") as buffer:
        shutil.copyfileobj(file.file,buffer)
    note={
        "title":title,
        "content":content,
        "file":file.filename
    }
    notes.append(note)
    return {"message":"Note created","note":note}