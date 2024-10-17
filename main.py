from fastapi import FastAPI

app = FastAPI()

# Rota raiz
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/hello thiago")
def read_root():
    return {"message": "esta url é do thiago"}
    

@app.get("/hello Kamila")
def read_root():
    return {"message": "Esta url é da kamila"}

@app.get("/hello Gaby")
def read_root():
    return {"message": "Esta url é da Gaby"}


@app.get("/subtração")
def read_root(v1: int, v2: int):
    res=v1 - v2
    return {"resultado" : res}

app.put


# Rota com parâmetros
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


