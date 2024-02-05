from django.urls import path 
from .views import PetListView,PetDetailView

urlpatterns = [
    path("list/",PetListView.as_view(),name="list_rescue_pets"),
    path("pet/<int:pk>",PetDetailView.as_view(),name="detail_pet")
]