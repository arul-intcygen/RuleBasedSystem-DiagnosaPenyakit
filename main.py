# main.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import json

from rule_engine import diagnose

app = FastAPI(title="Rule-Based Diagnosis API")

# lokasi dataset ada di /data
DATA_DIR = "Data"

with open(f"{DATA_DIR}/symptoms.json") as f:
    SYMPTOMS = json.load(f)

with open(f"{DATA_DIR}/rules.json") as f:
    RULES = json.load(f)

with open(f"{DATA_DIR}/diseases.json") as f:
    DISEASES = json.load(f)

class DiagnoseRequest(BaseModel):
    symptoms: List[str]

@app.post("/diagnose")
def diagnose_endpoint(request: DiagnoseRequest):
    if not request.symptoms:
        raise HTTPException(status_code=400, detail="Symptoms list cannot be empty")
    results = diagnose(
        input_symptoms=request.symptoms,
        rules=RULES
    )

    if not results:
        return {
            "message": "No matching disease found",
            "results": []
        }

    enriched = []
    for item in results:
        disease_key = item["disease"]
        meta = DISEASES.get(disease_key, {})

        enriched.append({
            "disease": disease_key,
            "score": item["score"],
            "label": meta.get("label", {}),
            "description": meta.get("description", {}),
            "severity": meta.get("severity")
        })

    return {
        "results": enriched
    }

@app.get("/symptoms")
def list_symptoms(lang: str = "id"):
    results = []

    for key, symptom in SYMPTOMS.items():
        label = symptom["label_id"] if lang == "id" else symptom["label_en"]

        results.append({
            "id": symptom["id"],
            "label": label
        })

    return {
        "count": len(results),
        "symptoms": results
    }
