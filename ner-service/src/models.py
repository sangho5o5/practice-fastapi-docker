from fastapi import FastAPI
from typing import List
from pydantic import BaseModel


class Content(BaseModel):
    post_url: str
    content: str


class Payload(BaseModel):
    # batch process for posting multiple contents at a time
    data: List[Content] # list of dictionary(post_url, content)

class SingleEntity(BaseModel):
    text: str
    entity_type: str

class Entities(BaseModel):
    post_url: str 
    entities: List[SingleEntity]