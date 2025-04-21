from django.urls import path
from .views import LorryListCreateView

urlpatterns = [
    path('', LorryListCreateView.as_view(), name='lorry-list-create'),
]
