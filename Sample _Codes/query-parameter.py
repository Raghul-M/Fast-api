from fastapi import FastAPI
from typing import Optional

app = FastAPI()


@app.get('/')
def index():
    return {'data':'blog_list'}


@app.get('/blog')  
def about(limit=10, published: bool=True, sort: Optional[str] = None): 
    if published:
        return {'data':f'{limit} published blogs from the db'}
    else: 
        return {'data':f'{limit} blogs from the db'}

