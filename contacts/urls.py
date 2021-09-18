from django.urls import path
from .views import ContactList, ContactDetialView

app_name = "contacts"

urlpatterns = [
    path('', ContactList.as_view()),
    path('<int:id>', ContactDetialView.as_view())
]
