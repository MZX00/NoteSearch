from fastapi import FastAPI, APIRouter

app = FastAPI()

router = APIRouter()

@app.get("/")
def root():
    return {"Hello": "World"}