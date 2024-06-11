from django.urls import path
from .views import TaskManagerViewSet

urlpatterns = [
    path("taskmanager/start_scraping", TaskManagerViewSet.as_view({"post": "start_scraping"})),
    path("taskmanager/scraping_status/<str:job_id>", TaskManagerViewSet.as_view({"get": "scraping_status"})),
]
