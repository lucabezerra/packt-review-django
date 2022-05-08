from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer 
from django.contrib.auth.models import Group, Permission, User
from django.contrib.contenttypes.models import ContentType
from ..chapter_3.models import (
    Seller, 
    Vehicle, 
    Engine, 
    Vehicle_Model
)


class EngineSerializer(ModelSerializer):
    class Meta:
        model = Engine
        fields = '__all__'


class Vehicle_ModelSerializer(ModelSerializer):
    class Meta:
        model = Vehicle_Model
        fields = '__all__'


class VehicleSerializer(ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'


class SellerSerializer(ModelSerializer):
    class Meta:
        model = Seller
        fields = '__all__'


# # class GroupSerializer(ModelSerializer):
# class GroupSerializer(HyperlinkedModelSerializer):
#    class Meta:
#        model = Group
#        fields = '__all__'
#        depth = 3


# # class PermissionSerializer(ModelSerializer):
# class PermissionSerializer(HyperlinkedModelSerializer):
#    class Meta:
#        model = Permission
#        fields = '__all__'
#        depth = 3


# # class ContentTypeSerializer(ModelSerializer):
# class ContentTypeSerializer(HyperlinkedModelSerializer):
#    class Meta:
#        model = ContentType
#        fields = '__all__'
#        depth = 3