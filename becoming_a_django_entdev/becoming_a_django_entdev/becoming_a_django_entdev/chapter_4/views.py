from django.http import Http404, HttpResponseRedirect
from django.template.response import (
    TemplateResponse
)
from django.urls import reverse
from django.views.generic import View

from ..chapter_3.models import Vehicle


def practice_view(request, year):
    return TemplateResponse(request, 'chapter_4/my_year.html', {'year': year})

def practice_year_view(request, year):
    print(
        request.build_absolute_uri(
            reverse('year_url', args=(2023,))
        )
    )
    print(
        request.build_absolute_uri(
            reverse('year_url', args=(2024,))
        )
    )


    if year >= 1900:
        return TemplateResponse(
            request, 
            'chapter_4/my_year.html', 
            {'year': year}
        )
    else:
        raise Http404('Year Not Found: %s' % year)


def vehicle_view(request, id):
    try:
        vehicle = Vehicle.objects.get(id=id)
    except Vehicle.DoesNotExist:
        raise Http404('Vehicle ID Not Found: %s' % id)
    else:
        print(vehicle.get_url())
        print(vehicle.get_absolute_url(request))

    return TemplateResponse(
        request,
        'chapter_4/my_vehicle.html',
        {'vehicle': vehicle}
    )


class VehicleView(View):
    template_name = 'chapter_4/my_vehicle_class_1.html'

    def get(self, request, id, *args, **kwargs):
        try:
            vehicle = Vehicle.objects.get(id=id)
        except Vehicle.DoesNotExist:
            raise Http404(
                'Vehicle ID Not Found: %s' % id
            )
        return TemplateResponse(
            request,
            self.template_name,
            {'vehicle': vehicle}
        )
    
    def post(self, request, *args, **kwargs):
        return HttpResponseRedirect(
            '/success/'
        )


class VehicleView2(VehicleView):
    template_name = 'chapter_4/my_vehicle_class_2.html'


class TestPage_View(View):
    template_name = 'chapter_4/pages/test_page_1.html'

    def get(self, request, *args, **kwargs):
        return TemplateResponse(
            request, 
            self.template_name, 
            {
                'title': 'My Test Page 1',
                'page_id': 'test-id-1',
                'page_class': 'test-page-1',
                'h1_tag': 'This is Test Page 1'
            }
        )


