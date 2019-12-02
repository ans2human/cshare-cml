from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .serializers import ContactSerializer, UserSerializer
from .models import Contact
from .serializers import User

# Create your views here.

class ContactViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ContactSerializer
    def get_queryset(self):
        return Contact.objects.filter(user=self.request.user)

class UserViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = User.objects.all()
