# test_rule_engine.py

from rule_engine import diagnose

# daftar penyakit dari database
rules = [
    {
        "disease": "Acne",
        "symptoms": ["S001", "S002", "S003", "S004"]
    },
    {
        "disease": "Fungal infection",
        "symptoms": ["S001", "S005", "S006"]
    },
    {
        "disease": "Vertigo",
        "symptoms": ["S010", "S011", "S012"]
    }
]

# misalkan ini adalah input dari User
input_symptoms = ["S001", "S005", "S006"]

# buat variable yang fungsinya memanggil fungsi lain yaitu diagnose
# dari rule_engine.py untuk dihitung kecocokannya berapa dengan penyakit yang ada
results = diagnose(
    input_symptoms=input_symptoms,
    rules=rules,
    threshold=0.6
)

print(results)
