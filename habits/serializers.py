from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from habits.models import Habit
from habits.validators import SimultaneousSelection, validate_duration


class HabitSerializer(ModelSerializer):
    duration = serializers.IntegerField(validators=[validate_duration])

    class Meta:
        model = Habit
        fields = "__all__"

        validators = [
            SimultaneousSelection("connection_habit", "reward")
        ]


