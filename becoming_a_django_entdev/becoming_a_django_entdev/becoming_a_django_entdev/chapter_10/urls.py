from django.urls import path
from django.views.generic import TemplateView
from .views import VehiclesView, SellersView

urlpatterns = [
    path(
        '', 
        TemplateView.as_view(
            template_name = 'chapter_9/index.html'
        )
    ),

    path(
        'all-vehicles/',
        VehiclesView.as_view(),
        name = 'all-vehicles'
    ),
    path(
        'all-sellers/',
        SellersView.as_view(),
        name = 'all-sellers'
    )

]
