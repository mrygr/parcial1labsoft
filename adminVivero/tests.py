from django.forms import ValidationError
from django.test import TestCase
from adminVivero.models import Productor

class ProductorTestCase(TestCase):
    def setUp(self):
        self.productor = Productor.objects.create(
            documento_productor=12345,
            nombres_productor="Juan",
            apellidos_productor="Perez",
            telefono_productor="123-456-7890",
            correo_productor="juan@example.com",
        )

    def test_productor_creation(self):
        self.assertEqual(self.productor.documento_productor, 12345)
        self.assertEqual(self.productor.nombres_productor, "Juan")
        self.assertEqual(self.productor.apellidos_productor, "Perez")
        self.assertEqual(self.productor.telefono_productor, "123-456-7890")
        self.assertEqual(self.productor.correo_productor, "juan@example.com")

    '''def test_productor_str_representation(self):
        self.assertEqual(str(self.productor), "Juan Perez")'''

    def test_productor_email_validation(self):
        invalid_productor = Productor(
            documento_productor=54321,
            nombres_productor="Maria",
            apellidos_productor="Lopez",
            telefono_productor="987-654-3210",
            correo_productor="correo_invalido",  # Correo inválido
        )
        with self.assertRaises(ValidationError):
            invalid_productor.full_clean()
