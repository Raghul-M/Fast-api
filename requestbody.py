from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


@app.get('/')
def index():
    return {'data':'blog_list'}

class Blog(BaseModel):
    title: str
    body: str
    id: int
    published : Optional[bool] = None

@app.post('/blog')
def create_blog(blog:Blog):
    return  {'data':f'blog is created wih title as {blog.title} '}
    