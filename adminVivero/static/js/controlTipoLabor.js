function mostrarCampoLabor(){
    var tipoLabor = document.getElementById("tipo_labor").value;

    //Solo se muestra el campo periodo para control de plagas
    if (tipoLabor == 'Control Plagas'){
        document.getElementById('periodo').style.display='block';
        document.getElementById('nombreHongo').style.display='none';
        document.getElementById('fechaAplica').style.display='none';
    
    //Solo se muestra el campo Control Hongos para control de Hongos
    }else if (tipoLabor == 'Control Hongos'){
        document.getElementById('periodo').style.display='none';
        document.getElementById('nombreHongo').style.display='block';
        document.getElementById('fechaAplica').style.display='none';

    //Solo se muestra el campo Control Fertilizante para control de fertilizantes
    }else if (tipoLabor == 'Control Fertilizante'){
        document.getElementById('periodo').style.display='none';
        document.getElementById('nombreHongo').style.display='none';
        document.getElementById('fechaAplica').style.display='block';

    //Se ocultan todos los campos cuando no se ha seleccionado un tipo de labor
    } else {
        document.getElementById('periodo').style.display='none';
        document.getElementById('nombreHongo').style.display='none';
        document.getElementById('fechaAplica').style.display='none';
    }
}