from models.note import Note
from fastapi import APIRouter, Depends, Form
from fastapi import HTTPException
from schemas.note import Notes
from db.session import SessionLocal
from sqlalchemy.orm import Session

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/save-note")
def save_notes(content: str = Form(...), db: Session = Depends(get_db)):

# --------------------------------------------------------------------------------
#                               USE THIS WHEN YOU USE JAVASCRIPT
# we use Form so data comes as string → content: str = Form(...)

# def save_notes(note_data: Notes, db: Session = Depends(get_db)):

    # note = models.Note(
    #     content = note_data.content
    # )

# --------------------------------------------------------------------------------
    note_obj = Note(content=content)

    db.add(note_obj)
    db.commit()
    db.refresh(note_obj)
    return note_obj

@router.get("/notes")
def get_notes(db: Session = Depends(get_db)):
    notes = db.query(Note).all()
    return notes