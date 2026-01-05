import joblib as jb 
from fastapi import FastAPI,Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import pandas as pd

model = jb.load("model.pkl")

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

class Heart(BaseModel):
    age : float
    sex: float
    cp : float
    trestbps : float
    chol : float
    fbs : float
    restecg : float
    thalach : float
    exang : float
    oldpeak : float
    slope : float
    ca : float
    

templates = Jinja2Templates(directory="template")

@app.get("/",response_class=HTMLResponse)
async def home(request:Request):
    return templates.TemplateResponse("page1.html",{"request":request})

@app.post("/predict")
async def attack_prediction(heart:Heart):

    data = pd.DataFrame([heart.dict()])
    predicted = float(model.predict(data)[0])

    return JSONResponse({"target": predicted})

@app.get("/result",response_class=HTMLResponse)
async def result_page(request:Request, target: float):
    return templates.TemplateResponse(
        "page2.html",
        {"request": request, "target": target}
    )
