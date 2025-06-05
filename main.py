from fastapi import FastAPI, Request
from pydantic import BaseModel
import joblib

# Chargement des objets
models = joblib.load("naive_bayes.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Sélection d’un modèle (ex: Naive Bayes)
model = models['Naive Bayes']

app = FastAPI()

# Schéma d’entrée pour la requête
class SMSRequest(BaseModel):
    message: str

@app.post("/predict")
def predict(data: SMSRequest):
    vect_text = vectorizer.transform([data.message])
    prediction = model.predict(vect_text)[0]
    label = "spam" if prediction == 1 else "ham"
    return {"prediction": label}
