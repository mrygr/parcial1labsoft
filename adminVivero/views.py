from django.shortcuts import render, redirect
from django.db import IntegrityError
from .models import Productor, Finca, Vivero, Tarea, Producto
from django.contrib import messages
import datetime


# Landing page del viviero
def index(request):
    return render(
        request,
        "index.html",
    )


#####################
# Sección productores
#####################

# Página para ver todos los productores
def ver_productores(request):
    productores_lista = Productor.objects.all()

    return render(request, "verProductores.html", {"productores": productores_lista})


# Página para crear un productor
def crear_productor(request):
    if request.method == "GET":
        return render(request, "crearProductor.html")

    else:
        try:
            Productor.objects.create(
                documento_productor=request.POST["productor_id"],
                nombres_productor=request.POST["productor_nombre"],
                apellidos_productor=request.POST["productor_apellido"],
                telefono_productor=request.POST["productor_telefono"],
                correo_productor=request.POST["productor_correo"],
            )

            messages.success(request, "¡Productor Registrado correctamente!")
            return redirect("productor_ver")

        except IntegrityError:
            messages.error(request, "¡El productor ya existe!")
            return render(
                request,
                "crearProductor.html",
            )


#####################
# Sección Fincas
#####################

# Página para ver todos las fincas registradas en el sistema
def ver_fincas(request):
    fincas_lista = Finca.objects.select_related("documento_productor")
    # print(fincas_lista.query)
    return render(request, "verFincas.html", {"fincas": fincas_lista})


# Página para crear una finca y asociarla a un productor
def crear_finca(request):
    if request.method == "GET":
        productores_lista = Productor.objects.all()

        return render(request, "crearFinca.html", {"productores": productores_lista})

    else:
        try:
            Finca.objects.create(
                numero_catastro=request.POST["finca_id"],
                municipio_ubicacion=request.POST["finca_ubicacion"],
                documento_productor=Productor.objects.get(
                    documento_productor=request.POST["seleccion_productor"]
                ),
            )

            messages.success(request, "¡Finca Registrada correctamente!")
            return redirect("finca_ver")

        except IntegrityError:
            messages.error(request, "¡La finca ya existe!")
            productores_lista = Productor.objects.all()

            return render(
                request, "crearFinca.html", {"productores": productores_lista}
            )



#####################
# Sección viveros
#####################

# Página para ver todos los viveros registradas en el sistema
def ver_viveros(request):
    viveros_lista = Vivero.objects.select_related("numero_catastro")
    return render(request, "verViveros.html", {"viveros": viveros_lista})


# Página para crear un vivero y asociarlo a una finca
def crear_vivero(request):
    if request.method == "GET":
        fincas_lista = Finca.objects.all()

        return render(request, "crearVivero.html", {"fincas": fincas_lista})

    else:
        print(request.POST.get("vivero"))
        try:
            Vivero.objects.create(
                codigo_vivero=request.POST["vivero_codigo"],
                cultivo_vivero=request.POST["vivero_cultivo"],
                numero_catastro=Finca.objects.get(
                    numero_catastro=request.POST["seleccion_finca"]
                ),
            )

            messages.success(request, "¡Vivero Registrado correctamente!")
            return redirect("vivero_ver")

        except IntegrityError:
            messages.error(request, "¡El Vivero ya existe!")
            fincas_lista = Finca.objects.all()

            return render(request, "crearVivero.html", {"fincas": fincas_lista})



#####################
# Sección Labores
#####################

# Página para ver todos las labores registradas en el sistema
def ver_labores(request):
    labores_lista = Tarea.objects.select_related("codigo_vivero")

    return render(request, "verLabores.html", {"labores": labores_lista})


# Página para crear una labor y asociarla al viviero y los productos que se van a utilizar
def crear_labor(request):
    if request.method == "GET":
        viveros_lista = Vivero.objects.all()
        productos_lista = Producto.objects.all()

        return render(
            request,
            "crearLabor.html",
            {"viveros": viveros_lista, "productos": productos_lista},
        )
    else:
        per_carencia = 0
        tip_hongo = "No aplica"
        dte_fertilizante = datetime.date(
            1900, 1, 1
        )  # para cumplir con el formato de Date en la DB

        # Se selecciona el campo que se va a guardar segun el tipo de labor:
        # Para control de plagas: solo se guarda su periodo de carencia
        # Para control hongos: solo se guarda el tipo de hongo
        # Para control de fertilizante: solo se guarda la fecha del último fertilizante
        if request.POST["tipo_labor"] == "Control Plagas":
            if request.POST["periodo_carencia"] == "":
                messages.error(
                    request,
                    "¡Para el control de plagas debe ingresar el periodo de carencia!",
                )

                viveros_lista = Vivero.objects.all()
                productos_lista = Producto.objects.all()
                return render(
                    request,
                    "crearLabor.html",
                    {"viveros": viveros_lista, "productos": productos_lista},
                )
            else:
                per_carencia = request.POST["periodo_carencia"]

        elif request.POST["tipo_labor"] == "Control Hongos":
            if request.POST["nombre_hongo"] == "":
                messages.error(
                    request,
                    "¡Para el control de hongos debe ingresar el nombre del hongo!",
                )

                viveros_lista = Vivero.objects.all()
                productos_lista = Producto.objects.all()
                return render(
                    request,
                    "crearLabor.html",
                    {"viveros": viveros_lista, "productos": productos_lista},
                )
            else:
                tip_hongo = request.POST["nombre_hongo"]

        elif request.POST["tipo_labor"] == "Control Fertilizante":
            if request.POST["fecha_aplicacion"] == "":
                messages.error(
                    request,
                    "¡Para el control de fertilizante debe ingresar la última fecha de aplicación!",
                )

                viveros_lista = Vivero.objects.all()
                productos_lista = Producto.objects.all()
                return render(
                    request,
                    "crearLabor.html",
                    {"viveros": viveros_lista, "productos": productos_lista},
                )
            else:
                dte_fertilizante = request.POST["fecha_aplicacion"]

        try:
            Tarea.objects.create(
                fecha_labor=request.POST["labor_fecha"],
                tipo_labor=request.POST["tipo_labor"],
                descripcion_labor=request.POST["labor_descripcion"],
                nombre_hongo=tip_hongo,
                periodo_carencia=per_carencia,
                fecha_aplicacion=dte_fertilizante,
                codigo_vivero=Vivero.objects.get(
                    codigo_vivero=request.POST["seleccion_vivero"]
                ),
                registro_ICA=Producto.objects.get(
                    registro_ICA=request.POST["seleccion_producto"]
                ),
            )

            messages.success(request, "Labor creada correctamente!")
            return redirect("labor_ver")

        except IntegrityError:
            messages.error(request, "¡La labor ya existe!")

            viveros_lista = Vivero.objects.all()
            productos_lista = Producto.objects.all()
            return render(
                request,
                "crearLabor.html",
                {"viveros": viveros_lista, "productos": productos_lista},
            )


#####################
# Sección Productos
#####################

# Página para ver todos los productos de control registrados en el sistema
def ver_productos(request):
    productos_lista = Producto.objects.all()

    return render(request, "verProductos.html", {"productos": productos_lista})


# Página para crear un producto
def crear_producto(request):
    if request.method == "GET":
        return render(request, "crearProducto.html")
    else:
        try:
            Producto.objects.create(
                registro_ICA=request.POST["producto_ICA"],
                nombre_producto=request.POST["producto_nombre"],
                aplicacion_producto=request.POST["producto_frecuencia"],
                valor_producto=request.POST["producto_costo"],
            )

            messages.success(request, "Producto de control creado correctamente!")
            return redirect("producto_ver")

        except IntegrityError:
            messages.error(request, "¡El producto de control ya existe!")

            return render(request, "crearProducto.html")
