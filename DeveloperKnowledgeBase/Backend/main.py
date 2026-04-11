from fastapi import FastAPI, Form
from routes import notes
from models.note import Base
from db.session import engine

app = FastAPI()

Base.metadata.create_all(bind=engine)
app.include_router(notes.router)


# --------------------------------------------------------------------------------
#                               USE THIS WHEN YOU GO MANUAL

# from db import get_conncection
# from fastapi import FastAPI, Form


# @app.post("/save-note")
# def save_note(content: str = Form(...)):

#     sql = "INSERT INTO notes (content) VALUES (%s)"
#     values = (content,)

#     conn = get_conncection()
#     cursor = conn.cursor()
    
#     cursor.execute(sql, values)
#     conn.commit()

#     cursor.close()
#     conn.close()

#     return {"message": "Saved"}

# @app.get("/notes")
# def get_notes():

#     conn = get_conncection()
#     cursor = conn.cursor()

#     sql = "SELECT id, content FROM notes"
#     cursor.execute(sql)

#     data = cursor.fetchall()

#     if not data:
#         return []
    

#     notes = []
#     for row in data:
#         notes.append({
#             "id": row[0],
#             "content": row[1]
#         })

#     cursor.close()
#     conn.close()

#     return notes  

# --------------------------------------------------------------------------------