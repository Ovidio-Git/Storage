!INC Local Scripts.EAConstants-JScript
/*
 * Script Name: Create diagram
 * Author: Ovidio Andrade
 * Purpose: 
 * Date: 26/12/2021
 */
const memory =['Actividades de vinculación', 'Sustanciación','Tiempos Públicos', 'Tipos de PQRS', 'Trámite', 'Trámite (BEPS)', 'Trámite (RPM)']

function main()
{  
	Repository.EnsureOutputVisible( "Script" );
	Repository.ClearOutput("Script");
	
	
	var pkgColpensiones as EA.Package;
	var dgmColpensiones as EA.Diagram;
	var objDiagramas as EA.DiagramObject;

	pkgColpensiones = Repository.GetTreeSelectedPackage(); 
	dgmColpensiones = Repository.GetDiagramByID(5);
	pkgElements     = pkgColpensiones.Elements;

	
	for (var i=0; i<memory.length;i++){
		NewElements = pkgElements.AddNew(memory[i], 'ArchiMate_DataObject');
		objDiagramas = dgmColpensiones.DiagramObjects.AddNew("l=200;r=400;t=200;b=270;","");
		objDiagramas.ElementID = NewElements.ElementID
		objDiagramas.Update()
	}
	
	Session.Output("[WORKSPACE] Pakage:     " + pkgColpensiones.Name);
	Session.Output("[WORKSPACE] Diagram:   " + dgmColpensiones.Name);
	Session.Output("[PROCESS] Adding " + memory.length + " New Elements");	
	if (NewElements.Update()){
		Session.Output("[OK] Successful process")
	}
	
	 

}
main();
