from django.urls import path
from .views import generator_view, generated_view

urlpatterns = [
    path('DynamicContentGenerator', generator_view),
    path('Generated/<str:word>/', generated_view, name='Generated'),
]
