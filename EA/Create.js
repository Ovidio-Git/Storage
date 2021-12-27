!INC Local Scripts.EAConstants-JScript

/*
 * Script Name: Create diagram
 * Author: Ovidio Andrade
 * Purpose: 
 * Date: 26/12/2021
 */
const memory =['Aceptación del servicio', ' Acreditación Cuenta Individual (BEPS)', ' Acta de notificación', ' Acta liquidación', ' Actividades de divulgación', ' Actividades de vinculación', ' Acto Administrativo', ' Acto Administrativo de Pago de Incapacidades', ' Acto Administrativo de Reconocimiento', ' Acuerdo de Pago', ' Afiliación', ' Afiliación (Colombianos en el exterior)', ' Afiliación (Subsidiada)', ' Afiliación (por Sentencia/ Tutela)', ' Anulación de Afiliación', ' Auditoria Reconocimiento', ' Autoliquidación', ' Autorización de procesamiento automático',' Auxilio Funerario']
function main()
{  
   Repository.EnsureOutputVisible( "Script" );
   Repository.ClearOutput("Script");
   var pkgColpensiones as EA.Package; 

   pkgColpensiones = Repository.GetTreeSelectedPackage();   
   pkgElements = pkgColpensiones.Elements;
	for (var i=0; i<=memory.length;i++){
	   pkgElements.AddNew(memory[i], 'ArchiMate_DataObject');
	}
 
   Session.Output("Values0: " + pkgColpensiones.Name);
   Session.Output("Values1: " + pkgElements.Name);
   pkgColpensiones.Update()	
}

main();
