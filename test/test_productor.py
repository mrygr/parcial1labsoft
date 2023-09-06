import pytest
from adminVivero.models import Productor

@pytest.mark.django_db
def test_productor_creation():
    productor = Productor.objects.create(
        documento_productor = 1088325831,
        nombres_productor = 'Usuario de prueba',
        apellidos_productor = 'Usuario apellidos',
        telefono_productor = '322345678',
        correo_productor = 'correo@correo.com',
    )

    assert productor.nombres_productor == 'Usuario de prueba'
