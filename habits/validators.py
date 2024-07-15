from rest_framework.exceptions import ValidationError
from datetime import datetime

class SimultaneousSelection:
    """Валидация на совместный выбор 'связанной привычки' и 'вознаграждения'."""
    def __init__(self, connection_habit, reward):
        self.field_1 = connection_habit
        self.field_2 = reward

    def __call__(self, habit):
        if habit.get(self.field_1) and habit.get(self.field_2):
            raise ValidationError(
                "Нельзя одновременно выбирать связанную привычку и вознаграждение"
            )

def validate_duration(duration):
    if duration and duration > 120:
        raise ValidationError("время выполнения не должно превышать 120 секунд")