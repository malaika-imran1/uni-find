from django.urls import path
from . import views

urlpatterns = [
    path("report-lost/", views.report_lost, name="report_lost"),
    path("lost-items/", views.lost_items_list, name="lost_items"),
]