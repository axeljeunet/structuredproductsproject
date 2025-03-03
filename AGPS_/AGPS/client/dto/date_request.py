from pydantic import BaseModel
from datetime import datetime

class DateRequest(BaseModel):
    date: datetime
