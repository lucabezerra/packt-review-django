from django.urls import re_path
from django.views.generic import (
    TemplateView
)
from .views import FormClassView, ModelFormClass_CreateView, ModelFormClass_UpdateView


urlpatterns = [
    re_path(
        r'^chapter-7/form-class/?$', 
        FormClassView.as_view()
    ),
    re_path(
        r'^chapter-7/contact-form-success/?$', 
        TemplateView.as_view(
            template_name = 'chapter_7/contact-success.html'
        ),
        kwargs = {
            'title': 'FormClassView Success Page',
            'page_id': 'form-class-success',
            'page_class': 'form-class-success-page',
            'h1_tag': 'This is the FormClassView Success Page Using ContactForm',
        }
    ),
    re_path(
        r'^chapter-7/model-form-class/?$', 
        ModelFormClass_CreateView.as_view()
    ),
    re_path(
        r'^chapter-7/vehicle-form-success/?$', 
        TemplateView.as_view(
            template_name = 'chapter_7/vehicle-success.html'
        ), 
        kwargs = {
            'title': 'ModelFormClassView Success Page',
            'page_id': 'model-form-class-success',
            'page_class': 'model-form-class-success-page',
            'h1_tag': 'This is the ModelFormClassView Success Page Using VehicleForm',
        }
    ),
    re_path(
        'chapter-7/model-form-class/(?P<id>[0-9])/?$', 
        ModelFormClass_UpdateView.as_view(), 
        name = 'vehicle_detail'
    ),
]
