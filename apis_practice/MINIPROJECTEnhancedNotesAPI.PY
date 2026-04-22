from fastapi import FastAPI, HTTPException, UploadFile, File
from pydantic import BaseModel
app = FastAPI()
notes = {}
current_id = 1
class NoteIn(BaseModel):
    title: str
    content: str
class NoteOut(BaseModel):
    id: int
    title: str
    content: str
    attached_file: str | None = None
@app.post("/notes", response_model=NoteOut, status_code=201)
def create_note(note: NoteIn):
    global current_id
    notes[current_id] = {
        "id": current_id,
        "title": note.title,
        "content": note.content,
        "attached_file": None
    }
    current_id += 1
    return notes[current_id - 1]
@app.get("/notes/{note_id}", response_model=NoteOut)
def get_note(note_id: int):
    if note_id not in notes:
        raise HTTPException(404, "Note not found")
    return notes[note_id]
@app.put("/notes/{note_id}", response_model=NoteOut)
def update_note(note_id: int, note: NoteIn):
    if note_id not in notes:
        raise HTTPException(404, "Note not found")
    notes[note_id]["title"] = note.title
    notes[note_id]["content"] = note.content
    return notes[note_id]
@app.delete("/notes/{note_id}")
def delete_note(note_id: int):
    if note_id not in notes:
        raise HTTPException(404, "Note not found")
    del notes[note_id]
    return {"message": "Deleted"}
@app.post("/notes/{note_id}/attachment")
def upload_file(note_id: int, file: UploadFile = File(...)):
    if note_id not in notes:
        raise HTTPException(404, "Note not found")
    notes[note_id]["attached_file"] = file.filename
    return {"filename": file.filename}