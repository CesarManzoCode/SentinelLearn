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

    def update_knowledge(self, topic: str, score: float):
        current = self.knowledge.get(topic, 0.0)
        self.knowledge[topic] = (current + score) / 2

    def add_weakness(self, weakness: str):
        if weakness not in self.weaknesses:
            self.weaknesses.append(weakness)