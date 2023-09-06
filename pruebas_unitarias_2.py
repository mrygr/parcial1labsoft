from django.test import TestCase
from .models import Productor, Finca

class FincaTestCase(TestCase):
    def setUp(self):
        self.productor = Productor.objects.create(
            documento_productor=12345,
            nombres_productor="Juan",
            apellidos_productor="Perez",
            telefono_productor="123-456-7890",
            correo_productor="juan@example.com",
        )
        self.finca = Finca.objects.create(
            numero_catastro="ABC123",
            municipio_ubicacion="Ciudad",
            documento_productor=self.productor,
        )

    def test_finca_creation(self):
        self.assertEqual(self.finca.numero_catastro, "ABC123")
        self.assertEqual(self.finca.municipio_ubicacion, "Ciudad")
        self.assertEqual(self.finca.documento_productor, self.productor)

    def test_finca_str_representation(self):
        self.assertEqual(str(self.finca), "ABC123 - Ciudad")

    def test_finca_foreign_key_relationship(self):
        self.assertEqual(self.finca.documento_productor, self.productor)
