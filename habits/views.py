
from rest_framework.viewsets import generics
from habits.paginations import HabitsPagination
from habits.models import Habit
from habits.serializers import HabitSerializer


class HabitsCreateAPIView(generics.CreateAPIView):
    serializer_class = HabitSerializer

    def perform_create(self, serializer):
        habit = serializer.save()
        habit.owner = self.request.user
        habit.save()

class HabitsListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    pagination_class = HabitsPagination


class HabitsRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()


class HabitsUpdateAPIView(generics.UpdateAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()


class HabitsDestroyAPIView(generics.DestroyAPIView):
    queryset = Habit.objects.all()

