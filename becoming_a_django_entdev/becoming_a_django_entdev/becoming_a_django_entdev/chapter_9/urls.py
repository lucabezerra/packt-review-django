from django.urls import path, register_converter
from ..chapter_4.converters import YearConverter 
from django.views.generic import TemplateView
from ..chapter_4.views import (
    practice_year_view,
    VehicleView
)

register_converter(YearConverter, 'year') 
urlpatterns = [
    path(
        '', 
        TemplateView.as_view(
            template_name = 'chapter_9/index.html'
        )
    ),
    path(
        'my_year_path/<year:year>/',
        practice_year_view, 
        name='year_url'
    ),
    path(
        'vehicle/<int:id>/',
        VehicleView.as_view(), 
        name='vehicle-detail'
    ),
]
