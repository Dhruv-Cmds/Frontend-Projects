#  Use when you use script.js in frontend aslo change in notes.py at line 20

from pydantic import BaseModel, StringConstraints
from typing import Annotated

class Notes(BaseModel):

    content: Annotated[str,
                       StringConstraints
                       (min_length=10,
                        max_length=255
                        )
                    ]