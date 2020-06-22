from django.contrib.auth.models import User
from rest_framework import viewsets
from ticketapi.serializers import UserSerializer, TicketSerializer, CategorySerializer
from tickets.models import Ticket, Category

from .permissions import IsOwner


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsOwner]


# ViewSets define the view behavior.
class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [IsOwner]


# ViewSets define the view behavior.
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsOwner]
