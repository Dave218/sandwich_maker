from django.urls import path
from sandwichapp.views import SandwichappView, IngredientsListView, SandwichGeneratorView

urlpatterns = [
    # sandwich/
    path('', SandwichappView.as_view(), name='sandwich'),
    path('ingredients/<str:ingredient_type>', IngredientsListView.as_view(), name='ingredients_list'),
    path('random', SandwichGeneratorView.as_view(), name='sandwich_generator')
]