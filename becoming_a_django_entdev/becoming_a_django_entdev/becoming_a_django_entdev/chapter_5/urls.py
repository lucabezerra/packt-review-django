from django.urls import re_path
from django.views.generic import (
    TemplateView
)
from .views import FormClass_View, ModelFormClass_CreateView, ModelFormClass_UpdateView


urlpatterns = [
    re_path(
        r'^chapter-5/form-class/?$', 
        FormClass_View.as_view()
    ),
    re_path(
        r'^chapter-5/contact-form-success/?$', 
        TemplateView.as_view(
            template_name = 'chapter_5/contact-success.html'
        ),
        kwargs = {
            'title': 'FormClass_View Success Page',
            'page_id': 'form-class-success',
            'page_class': 'form-class-success-page',
            'h1_tag': 'This is the FormClass_View Success Page Using ContactForm',
        }
    ),
    re_path(
        r'^chapter-5/model-form-class/?$', 
        ModelFormClass_CreateView.as_view()
    ),
    re_path(
        r'^chapter-5/vehicle-form-success/?$', 
        TemplateView.as_view(
            template_name = 'chapter_5/vehicle-success.html'
        ), 
        kwargs = {
            'title': 'ModelFormClass_View Success Page',
            'page_id': 'model-form-class-success',
            'page_class': 'model-form-class-success-page',
            'h1_tag': 'This is the ModelFormClass_View Success Page Using VehicleForm',
        }
    ),
    re_path(
        'chapter-5/model-form-class/(?P<id>[0-9])/?$', 
        ModelFormClass_UpdateView.as_view(), 
        name = 'vehicle_detail'
    ),
]
