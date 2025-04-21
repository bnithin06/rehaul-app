from django.urls import path
from .views import LoadRequestListCreateView

urlpatterns = [
    path('load-requests/', LoadRequestListCreateView.as_view(), name='load-requests'),
]