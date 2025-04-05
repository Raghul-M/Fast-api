from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    return {'data':{"name":"Raghul"}}

@app.get('/about')  #path (/about) , get (operation) , app (path decorator)
def about():        # path operation function
    return {'data':"data page"}

