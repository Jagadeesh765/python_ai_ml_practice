from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List
app = FastAPI()

# -------- MODELS --------
class NoteBase(BaseModel):
    title: str
    content: str

class NoteIn(NoteBase):   # Input model
    pass

class NoteOut(NoteBase):  # Output model
    id: int

# --- Note DATABASE ---
notes_db = []
current_id = 1

# -------- CREATE NOTE --------
@app.post("/notes/", response_model=NoteOut, status_code=status.HTTP_201_CREATED)
def create_note(note: NoteIn):
    global current_id
    new_note = note.dict()
    new_note["id"] = current_id
    notes_db.append(new_note)
    current_id += 1
    return new_note

# -------- GET ALL NOTES --------
@app.get("/notes/", response_model=List[NoteOut])
def get_notes():
    return notes_db

# -------- GET SINGLE NOTE --------
@app.get("/notes/{note_id}", response_model=NoteOut)
def get_note(note_id: int):
    for note in notes_db:
        if note["id"] == note_id:
            return note
    raise HTTPException(status_code=404, detail="Note not found")

# -------- DELETE NOTE --------
@app.delete("/notes/{note_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_note(note_id: int):
    for note in notes_db:
        if note["id"] == note_id:
            notes_db.remove(note)
            return
    raise HTTPException(status_code=404, detail="Note not found")