from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import ListView,DetailView
from .models import RescuePet

class PetListView(ListView):
    model = RescuePet
    paginate_by=24
    template_name="pages/adoption_list.html"
    context_object_name = "rescuepets"
    
    def get_queryset(self) -> QuerySet[Any]:
        return super().get_queryset().filter(adopted=False)
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        pets = context["rescuepets"]
        
        if len(pets) <= 4:
            context['rows'] = 1
            context['pets_rows'] = pets
        else:
            context['rows'] = 4
            context['pets_rows'] = [pets[i:i + 4] for i in range(0, len(pets), 4)]
            
        num_pets = self.get_queryset().count()  
        print(f"Total de mascotas sin adoptar: {num_pets}")
        print(context['pets_rows'])

        return context
    
class PetDetailView(DetailView):
    model = RescuePet
    template_name="pages/detail_pet.html"
    context_object_name = "pet"