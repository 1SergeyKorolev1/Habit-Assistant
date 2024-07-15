
from rest_framework.viewsets import generics
from rest_framework.permissions import IsAuthenticated
from habits.permissions import IsOwner
from habits.paginations import HabitsPagination
from habits.models import Habit
from habits.serializers import HabitSerializer


class HabitsCreateAPIView(generics.CreateAPIView):
    serializer_class = HabitSerializer
    permission_classes = (IsAuthenticated, )


    def perform_create(self, serializer):
        habit = serializer.save()
        habit.owner = self.request.user
        habit.save()

class HabitsListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    pagination_class = HabitsPagination

    def get_queryset(self):
        user = self.request.user
        return Habit.objects.filter(owner=user)


class HabitsPublicListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.filter(published_bool=True)
    pagination_class = HabitsPagination


class HabitsRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = (IsAuthenticated, IsOwner)


class HabitsUpdateAPIView(generics.UpdateAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = (IsAuthenticated, IsOwner)


class HabitsDestroyAPIView(generics.DestroyAPIView):
    queryset = Habit.objects.all()
    permission_classes = (IsAuthenticated, IsOwner)

