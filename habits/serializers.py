from rest_framework.serializers import ModelSerializer

from habits.models import Habit
from habits.validators import SimultaneousSelection


class HabitSerializer(ModelSerializer):

    class Meta:
        model = Habit
        fields = "__all__"

        validators = [
            SimultaneousSelection("connection_habit", "reward")
        ]


