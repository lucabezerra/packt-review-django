from django.http import JsonResponse
from django.shortcuts import render
from django.template.response import TemplateResponse
from django.views.generic import View

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from ..chapter_3.models import Engine, Seller, Vehicle, Vehicle_Model
from .serializers import (
    EngineSerializer,
    SellerSerializer,
    VehicleSerializer,
    Vehicle_ModelSerializer
)


class EngineViewSet(ModelViewSet):
    queryset = Engine.objects.all().order_by('name')
    serializer_class = EngineSerializer
    permission_classes = [IsAuthenticated]


class Vehicle_ModelViewSet(ModelViewSet):
    queryset = Vehicle_Model.objects.all().order_by(
        'name'
    )
    serializer_class = Vehicle_ModelSerializer
    permission_classes = [IsAuthenticated]


class VehicleViewSet(ModelViewSet):
    queryset = Vehicle.objects.all().order_by('price')
    serializer_class = VehicleSerializer
    permission_classes = [IsAuthenticated]


class SellerViewSet(ModelViewSet):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
    permission_classes = [IsAuthenticated]


class GetSellerView(View):
    template_name = 'chapter_8/spa_pages/get_seller.html'

    def get(self, request, *args, **kwargs):
        context = {}
        return TemplateResponse(
            request, 
            self.template_name, 
            context
        )


class GetSellerHTMLView(APIView):
    permission_classes = [IsAuthenticated]
    template_name = 'chapter_8/details/seller.html'

    def get(self, request, format=None, id=0, *args, **kwargs):
        if request.user.is_authenticated and request.user.has_perm('chapter_3.view_seller'):
            try:
                seller = Seller.objects.get(id=id)
            except Seller.DoesNotExist:
                seller = None
        else:
            seller = None

        context = {'seller': seller,}

        return render(
            request, 
            self.template_name, 
            context = context
        )


class GetSellerWithTokenView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None, id=0, *args, **kwargs):
        seller = None
        req_user = request._user

        if req_user.has_perm('chapter_3.view_seller'):
            perm_granted = True

            try:
                seller = Seller.objects.get(id=id)
            except Seller.DoesNotExist:
                pass
        else:
            perm_granted = False

        context = {
            'request': request,
            'seller': seller,
        }

        seller = SellerSerializer(
            seller, 
            context = context
        )

        new_context = {
            'seller': seller.data,
            'perm_granted': perm_granted
        }

        return JsonResponse(new_context)
