#  Use when you use script.js in frontend aslo change in notes.py at line 20

from pydantic import BaseModel

class Notes(BaseModel):

    content: str