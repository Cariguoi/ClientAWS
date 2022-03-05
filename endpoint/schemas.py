from pydantic import BaseModel


class DataSchema(BaseModel):
    subject: str
    teacher_name: str
    hours_numbers: str
    description: str


class Response(BaseModel):
    status: bool
    message: str
