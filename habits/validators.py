from rest_framework.exceptions import ValidationError


class SimultaneousSelection:
    """Валидация на совместный выбор 'связанной привычки' и 'вознаграждения'."""
    def __init__(self, connection_habit, reward):
        self.field_1 = connection_habit
        self.field_2 = reward

    def __call__(self, habit):
        if habit.get("connection_habit") and habit.get("reward"):
            raise ValidationError(
                "Нельзя одновременно выбирать связанную привычку и вознаграждение"
            )
