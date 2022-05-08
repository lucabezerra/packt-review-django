from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

from rest_framework import routers

from .views import (
    EngineViewSet,
    SellerViewSet,
    VehicleViewSet,
    Vehicle_ModelViewSet,
    GetSellerView,
    GetSellerHTMLView,
    GetSellerWithTokenView
)


router = routers.DefaultRouter()
router.register(r'engines', EngineViewSet)
router.register(r'sellers', SellerViewSet)
router.register(r'vehicles', VehicleViewSet)
router.register(r'vehicle-models', Vehicle_ModelViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        '', 
        TemplateView.as_view(
            template_name = 'chapter_8/index.html'
        )
    ),
    path('chapter-8/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path(
        'chapter-8/get-seller/',
        GetSellerView.as_view(),
        name = 'get-seller'
    ),
    path(
        'chapter-8/seller/<int:id>/', 
        GetSellerHTMLView.as_view(), 
        name = 'seller-detail'
    ),
    path(
        'chapter-8/sellertoken/<int:id>/', 
        GetSellerWithTokenView.as_view(),
        name = 'seller-token-detail'
    ),
]
