

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions

from .models import Contact
from .serializers import ContactListSerializer

class ContactList(ListCreateAPIView):
    serializer_class = ContactListSerializer
    permission_classes = (permissions.IsAuthenticated,)
    
    def perform_create(self, serializer):
        serializer = ContactListSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Contact.objects.filter(owner=self.request.user)

class ContactDetialView(RetrieveUpdateDestroyAPIView):
    serializer_class = ContactListSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = "id"
    
    def get_queryset(self):
        return Contact.objects.filter(owner=self.request.user)


