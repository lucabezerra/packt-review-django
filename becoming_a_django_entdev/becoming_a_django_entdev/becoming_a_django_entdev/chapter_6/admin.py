from django.contrib import admin
from django.contrib.admin import ModelAdmin, TabularInline
from django.contrib.auth.admin import UserAdmin

from ..chapter_3.models import Seller, Vehicle, Vehicle_Model, Engine
from .forms import AddEngineForm, EngineForm, EngineSuperUserForm


class VehiclesInline(TabularInline):
    model = Seller.vehicles.through
    extra = 1


@admin.register(Seller)
class SellerAdmin(UserAdmin):
    save_on_top = True
    actions_on_top = True
    actions_on_bottom = True
    actions_selection_counter = True
    preserve_filters = False
    list_per_page = 20
    ordering = ('username',)
    inlines = [VehiclesInline,]
    prepopulated_fields = {
        'username': ('first_name', 'last_name',)
    }
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'name',
        'is_staff',
        'is_superuser',
    )
    list_display_links = (
        'username',
        'name',
    )
    list_editable = (
        'first_name',
        'last_name',
    )
    list_filter = (
        'is_staff',
        'is_superuser',
        'is_active',
        'name',
        'groups'
    )
    search_fields = (
        'username',
        'first_name',
        'last_name',
        'name',
        'email'
    )
    fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username',
                'password',
            ),
        }),
        (('Personal Info'), {'fields': (
            'first_name',
            'last_name',
            'name',
            'email',
        )}),
                (('Permissions'), {'fields': (
            'is_active',
            'is_staff',
            'is_superuser',
            'groups',
            'user_permissions',
        )}),
        (('Important Dates'), {'fields': (
             'last_login',
             'date_joined',
        )}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username',
                'password1',
                'password2',
            ),
        }),
        (('Personal Info'), {'fields': (
            'first_name',
            'last_name',
            'name',
            'email',
        )}),
    )



class VehicleInline(TabularInline):
    model = Vehicle
    extra = 1


class VehicleAdmin(ModelAdmin):
    radio_fields = {'engine': admin.HORIZONTAL,}


class Vehicle_ModelAdmin(ModelAdmin):
    pass


class EngineAdmin(ModelAdmin):
    inlines = [VehicleInline,]
    
    def get_form(self, request, obj=None, **kwargs):
        if obj:
            if request.user.is_superuser:
                return EngineSuperUserForm

            return EngineForm
        else:
            return AddEngineForm

    def save_model(self, request, obj, form, change):
        print(obj.__dict__)
        # Code actions before save here
        super().save_model(request, obj, form, change)
        # Code actions after save here

    def delete_model(self, request, obj):
        print(obj.__dict__)
        # Code actions before delete here
        super().delete_model(request, obj)
        # Code actions after delete here



admin.site.register(Vehicle_Model, Vehicle_ModelAdmin)
admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(Engine, EngineAdmin)