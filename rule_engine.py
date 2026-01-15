from typing import List, Dict, Set

def calculate_score(
    input_symptoms: Set[str],
    rule_symptoms: Set[str]
) -> float:
    """
    Hitung skor kecocokan antara input user dan satu rule penyakit.
    """
    if not rule_symptoms:
        return 0.0

    matched = input_symptoms & rule_symptoms
    return len(matched) / len(rule_symptoms)

def diagnose(
    input_symptoms: List[str],
    rules: List[Dict],
    threshold: float = 0.6
) -> List[Dict]:
    """
    Lakukan diagnosis berdasarkan rule matching.
    """

    input_set = set(input_symptoms)
    results = []

    for rule in rules:
        rule_symptoms = set(rule["symptoms"])
        score = calculate_score(input_set, rule_symptoms)

        if score >= threshold:
            results.append({
                "disease": rule["disease"],
                "score": round(score, 2)
            })

    results.sort(key=lambda x: x["score"], reverse=True)
    return results
