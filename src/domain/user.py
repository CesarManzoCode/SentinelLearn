class User:
    user_name: str

    # conocimiento por tema
    knowledge: dict[str, float]
    # Ejemplo: {"derivatives": 0.4, "algebra": 0.2}

    # debilidades detectadas
    weaknesses: list[str]
    # Ejemplo: ["algebra", "chain_rule"]

    # historial resumido
    history: list[dict]
    # Ejemplo: [{"task": "derivatives", "success": False}]