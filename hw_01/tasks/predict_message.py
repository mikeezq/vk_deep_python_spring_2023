class SomeModel:
    def __init__(self, num):
        self.num = num

    def predict(self, message: str) -> float:
        print(f"For message '{message}', predict {self.num}")
        return self.num


def predict_message_mood(message: str, model: SomeModel, bad_thresholds: float = 0.3,
                         good_thresholds: float = 0.8) -> str:
    if not message:
        raise ValueError("Message can't be empty")
    predict = model.predict(message)
    if predict > good_thresholds:
        return "отл"
    if predict < bad_thresholds:
        return "неуд"
    return "норм"
