!INC Local Scripts.EAConstants-JScript
/*
 * Script Name: Create diagram
 * Author: Ovidio Andrade
 * Purpose: 
 * Date: 26/12/2021
 */
const CreateElement = ['ArchiMate_Artifact','ArchiMate_DataObject','ArchiMate_ApplicationComponent']
const memory =[ 'EXCEL', 'CONSULTA PAGOS INCONSISTENCIAS', 'CORRECCIONES PAGOS (CORRDNC)', 'MODIDNC', 'HISTORICO SUBSIDIADOS', 'LIQUIDADOR', 'CONSGRE', 'CONSDNC', 'VERIGRE PAGOS', 'COMBINACION DE AUTOLIQUIDACIONES DE CORRECCIÓN', 'AUTOLISS', 'SAP - ERP', 'HISTORIA LABORAL MASIVA', 'MODICAN', 'HISTORIA LABORAL UNIFICADA', 'HPOO', 'VERIGRE', 'BIZAGI', 'MODISUBSI', 'CONSIDE']

function main()
{  
	Repository.EnsureOutputVisible( "Script" );
	Repository.ClearOutput("Script");
	
	const ctrl = [false, true];
	var pkgColpensiones as EA.Package;
	var dgmColpensiones as EA.Diagram;
	var objDiagramas as EA.DiagramObject;

	pkgColpensiones = Repository.GetTreeSelectedPackage(); 
	dgmColpensiones = Repository.GetDiagramByGuid('{5E62CA76-13CA-4600-9BF6-0A50BE82A019}');
	pkgElements     = pkgColpensiones.Elements;

	if(ctrl[0]){
		for (var i=0; i<memory.length;i++){
			NewElements  = pkgElements.AddNew(memory[i], CreateElement[2]);
			objDiagramas = dgmColpensiones.DiagramObjects.AddNew("l=200;r=400;t=200;b=270;","");
			objDiagramas.ElementID = NewElements.ElementID
			objDiagramas.Update()
		}
	}
	Session.Output("[WORKSPACE] Pakage:     " + pkgColpensiones.Name);
	Session.Output("[WORKSPACE] Diagram:   "  + dgmColpensiones.Name);
	Session.Output("[PROCESS] Adding " + memory.length + " New Elements");	
	if (NewElements.Update()){
		Session.Output("[OK] Successful process")
	}
}
main();
