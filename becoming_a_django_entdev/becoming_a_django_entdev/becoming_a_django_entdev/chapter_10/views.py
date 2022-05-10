from django.db.models import Prefetch
from django.http import Http404
from django.template.response import (
    TemplateResponse
)
from django.views.generic import View
from ..chapter_3.models import Seller, Vehicle

class VehiclesView(View):
    template_name = 'chapter_10/vehicles.html'

    def get(self, request, *args, **kwargs):
        try:
            vehicles = Vehicle.objects.prefetch_related(
                            'vehicle_sellers'
                        ).select_related(
                            'vehicle_model',
                            'engine'
                        ).all()

        except Vehicle.DoesNotExist:
            raise Http404('No Vehicles Found')

        return TemplateResponse(
            request,
            self.template_name,
            {'vehicles': vehicles}
        )


class SellersView(View):
    template_name = 'chapter_10/sellers.html'

    def get(self, request, *args, **kwargs):
        try:
            sellers = Seller.objects.prefetch_related(
                Prefetch(
                    'vehicles',
                    to_attr  = 'filtered_vehicles',
                    queryset = Vehicle.objects.filter(
                        vehicle_model__name = 'Blazer LT'
                    )
                ),
                'filtered_vehicles__vehicle_model',
                'filtered_vehicles__engine'
            ).all()


        except Seller.DoesNotExist:
            raise Http404('No Sellers Found')

        return TemplateResponse(
            request,
            self.template_name,
            {'sellers': sellers}
        )
