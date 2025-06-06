from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import joblib

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Charger modèle et vectorizer
models = joblib.load("naive_bayes.pkl")
vectorizer = joblib.load("vectorizer.pkl")
model = models["Naive Bayes"]

# API JSON classique
class SMSRequest(BaseModel):
    message: str

@app.post("/predict")
def predict(data: SMSRequest):
    vect_text = vectorizer.transform([data.message])
    prediction = model.predict(vect_text)[0]
    label = "spam" if prediction == 1 else "ham"
    return {"prediction": label}

# Formulaire web
@app.get("/", response_class=HTMLResponse)
async def get_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/", response_class=HTMLResponse)
async def post_form(request: Request, message: str = Form(...)):
    vect = vectorizer.transform([message])
    prediction = model.predict(vect)[0]
    label = " SPAM" if prediction == 1 else " Message normal"
    return templates.TemplateResponse("index.html", {"request": request, "result": label})
