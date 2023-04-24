from django.urls import path
from .views import IndexView, delete_event

urlpatterns = [
    path("", IndexView.as_view(), name = "index"),
    path('delete_event/<event_id>', delete_event, name = 'delete-event')
]