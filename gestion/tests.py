from django.test import TestCase
from gestion.models import User


class UserRoleTestCase(TestCase):
    def test_user_roles(self):
        user_admin = User.objects.get(username ="Maguy")
        self.assertEqual(user_admin.role, "Admin")

        user_supplier = User.objects.get(username ="Inès")
        self.assertEqual(user_supplier.role, "Supplier")

        user_buyer = User.objects.get(username ="Cédric")
        self.assertEqual(user_buyer.role, "Buyer")
