!INC Local Scripts.EAConstants-JScript
/*
 * Script Name: Create diagram
 * Author: Ovidio Andrade
 * Purpose: 
 * Date: 26/12/2021
 */
const ElementTypes    = ['ArchiMate_Artifact','ArchiMate_ApplicationComponent','ArchiMate_DataObject']
const ElementMeasures = ['l=260;r=400;t=200;b=250;','l=260;r=400;t=200;b=270;']
const ElementNames    = ['FD_RADICA']


function main()
{  
	Repository.EnsureOutputVisible( "Script" );
	Repository.ClearOutput("Script");
	
	const ctrl = [false, true];
	var pkgColpensiones as EA.Package;
	var dgmColpensiones as EA.Diagram;
	var objDiagramas as EA.DiagramObject;

	pkgColpensiones = Repository.GetTreeSelectedPackage(); 
	dgmColpensiones = Repository.GetDiagramByGuid('{ECA94A63-08B2-4379-AFD9-E1373247CAA3}');
	pkgElements     = pkgColpensiones.Elements;
	
	Session.Output("[WORKSPACE] Pakage:     " + pkgColpensiones.Name);
	Session.Output("[WORKSPACE] Diagram:   "  + dgmColpensiones.Name);
		
	if(ctrl[1]){
		Session.Output("[PROCESS] Adding " + ElementNames.length + " New Elements");
		for (var i=0; i<ElementNames.length;i++){
			NewElements  = pkgElements.AddNew(ElementNames[i], ElementTypes[0]);
			objDiagramas = dgmColpensiones.DiagramObjects.AddNew(ElementMeasures[1],"");
			objDiagramas.ElementID = NewElements.ElementID
			objDiagramas.Update()
		}
		if (NewElements.Update()){
			Session.Output("[OK] Successful process")
		}
	}
}
main();
