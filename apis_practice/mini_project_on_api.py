from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from typing import List,Optional
app = FastAPI()
notes_details=[]
class Note(BaseModel):
    id:int
    title:str
    content:str
#####create
@app.post("/notes/",response_model=Note)
def create_note(note:Note):
    notes_details.append(note)
    return note
###read
@app.get("/notes/",response_model=List[Note])
def view_notes(title:Optional[str]=None):
    if title:
        return [note for note in notes_details if note.title==title]
    return notes_details
##3update
@app.put("/notes/{note_id}",response_model=Note)
def update_notes(note_id:int,updated_note:Note):
    for index,note in enumerate(notes_details):
        if note.id==note_id:
            notes_details[index]=updated_note
            return updated_note
    raise HTTPException(status_code=404,detail="Note not found")
##delete
@app.delete("/notes/{note_id}")
def delete_notes(note_id:int):
    for index,note in enumerate(notes_details):
        if note.id==note_id:
            notes_details.pop(index)
            return {"message":"Note deleted"}
    raise HTTPException(status_code=404,detail="Note not found")
