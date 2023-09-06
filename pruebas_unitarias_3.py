from django.test import TestCase
from .models import Productor, Finca, Vivero

class ViveroTestCase(TestCase):
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
        self.vivero = Vivero.objects.create(
            codigo_vivero="VIV001",
            cultivo_vivero="Tomates",
            numero_catastro=self.finca,
        )

    def test_vivero_creation(self):
        self.assertEqual(self.vivero.codigo_vivero, "VIV001")
        self.assertEqual(self.vivero.cultivo_vivero, "Tomates")
        self.assertEqual(self.vivero.numero_catastro, self.finca)

    def test_vivero_str_representation(self):
        self.assertEqual(str(self.vivero), "VIV001 - Tomates")

    def test_vivero_foreign_key_relationship(self):
        self.assertEqual(self.vivero.numero_catastro, self.finca)