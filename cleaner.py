import pandas as pd
import numpy as np

df = pd.read_csv("dataset.csv")
df = df.fillna("")

for col in df.columns:
    df[col] = df[col].apply(lambda x: x.strip() if isinstance(x, str) else x)

rules_dict = {}
groups = df.groupby("Disease")
for disease, group_data in groups:
    all_symptoms = group_data.iloc[:, 1:].values.flatten()

    unique_symptoms = set([sym for sym in all_symptoms if sym != ""])

    rules_dict[disease] = list(unique_symptoms)

print("Contoh Struktur Rule yang terbentuk:")
import json

first_2_rules = {k: rules_dict[k] for k in list(rules_dict)[:2]}
print(json.dumps(first_2_rules, indent=2))

with open("knowledge_base.json", "w") as f:
    json.dump(rules_dict, f)
