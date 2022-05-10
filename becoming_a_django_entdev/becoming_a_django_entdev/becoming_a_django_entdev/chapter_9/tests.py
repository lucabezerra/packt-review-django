from django.contrib.auth.models import AnonymousUser
from django.test import RequestFactory, TestCase, Client

from djmoney.money import Money
from rest_framework.test import APITestCase, APIClient

from ..chapter_3.models import Engine, Seller, Vehicle, Vehicle_Model, Seller
from ..chapter_4.views import practice_year_view, VehicleView


# class ModelUnitTestCase(TestCase):
#     def setUp(self):
#         model = Vehicle_Model.objects.create(
#             name = 'Grand Cherokee Laredo 4WD',
#             make = 8
#         )
#         engine = Engine.objects.create(
#             name = '3.6L FI FFV DO',
#             vehicle_model = model
#         )
#         vehicle = Vehicle.objects.create(
#             vin = 'aa890123456789012',
#             sold = False,
#             price = Money(39875, 'USD'),
#             make = 8,
#             vehicle_model = model,
#             engine = engine
#         )
#         seller = Seller.objects.create_user(
#             'test',
#             'testing@example.com',
#             'testpassword',
#             is_staff = True,
#             is_superuser = True,
#             is_active = True,
#             name = 'Chapter 9 Seller 1'
#         )
#         seller.vehicles.set([vehicle])

#     def test_full_vehicle_name(self):
#         vehicle_1 = Vehicle.objects.get(
#             vin = 'aa890123456789012'
#         )
#         self.assertEqual(
#             vehicle_1.full_vehicle_name(),
#             'Jeep Grand Cherokee Laredo 4WD - 3.6L FI FFV DO'
#         )

# class YearRequestTestCase(TestCase):
#     def setUp(self):
#         self.factory = RequestFactory()

#     def test_methodbased(self):
#         request = self.factory.get('/my_year_path/2022/')
#         request.user = AnonymousUser()
#         response = practice_year_view(request, 2022)
#         self.assertEqual(response.status_code, 200)

# class VehicleRequestTestCase(TestCase):
#     fixtures = ['chapter_3']

#     def setUp(self):
#         self.factory = RequestFactory()

#     def test_classbased(self):
#         request = self.factory.get('/vehicle/1/')
#         request.user = AnonymousUser()
#         response = VehicleView.as_view()(request, 99)
#         self.assertEqual(response.status_code, 200)


# class SellerClientTestCase(TestCase):
#     fixtures = ['chapter_3']

#     def setUp(self):
#         self.user = Seller.objects.get(id=1)
#         self.client = Client()
#         self.client.login(
#             username = self.user.username,
#             password = 'mynewpassword'
#         )

#     def test_get(self):
#         response = self.client.get('/chapter-8/seller/1/')
#         self.assertEqual(response.status_code, 200)
#         seller = response.context['seller']
#         self.assertEqual(seller.name, 'Test Biz Name')

class EngineAPITestCase(APITestCase):
    fixtures = ['chapter_3']

    def setUp(self):
        model = Vehicle_Model.objects.create(
            name = 'Grand Cherokee Laredo 4WD', 
            make = 8
        )
        engine = Engine.objects.create(
            name = '3.6L FI FFV DO', 
            vehicle_model = model
        )

        self.user = Seller.objects.get(id=1)
        self.client = APIClient()
        self.client.login(
            username = self.user.username,
            password = 'mynewpassword'
        )

    # def test_post(self):
    #     response = self.client.post(
    #         '/chapter-8/engines/',
    #         {'name': 'New Engine'},
    #         format = 'json'
    #     )

    #     self.assertEqual(response.status_code, 201)
    #     self.assertEqual(response.data['name'], 'New Engine')

    def test_put(self):
        response = self.client.put(
            '/chapter-8/engines/3/',
            {'name': 'My Changed Engine Name'},
            format='json'
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.data['name'],
            'My Changed Engine Name'
        )
