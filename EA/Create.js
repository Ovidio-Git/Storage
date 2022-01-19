!INC Local Scripts.EAConstants-JScript
/*
 * Script Name: Create diagram
 * Author: Ovidio Andrade
 * Purpose: 
 * Date: 26/12/2021
 */
 
const power           = {"off":false, "on":true}
const ElementStorage  = ['ArchiMate_Artifact','ArchiMate_DataObject'];
const ElementTypes    = ['ArchiMate_BusinessFunction','ArchiMate_BusinessProcess','ArchiMate_ApplicationService', 'ArchiMate_ApplicationComponent','ArchiMate_BusinessActor','ArchiMate_Location'];                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
const ElementMeasures = ['l=260;r=400;t=200;b=250;','l=260;r=400;t=200;b=270;'];
const ctrlProscess    = power["off"];
const targetDiagram   = '{92BA5D0F-F446-4611-AE38-9FFA3912D8F5}';                                                                                                                                                                                          
const ElementType     = ElementTypes[4];
const ElementNames    = ['Afiliado', 'Apoderado', 'Tercero', 'Empleador'];    



function main()
{  
	Repository.EnsureOutputVisible( "Script" );
	Repository.ClearOutput("Script");

	var pkgColpensiones as EA.Package;
	var dgmColpensiones as EA.Diagram;
	var objDiagramas as EA.DiagramObject;

	pkgColpensiones = Repository.GetTreeSelectedPackage(); 
	dgmColpensiones = Repository.GetDiagramByGuid(targetDiagram);
	pkgElements     = pkgColpensiones.Elements;
	
	Session.Output("[WORKSPACE] Pakage:     " + pkgColpensiones.Name);
	Session.Output("[WORKSPACE] Diagram:   "  + dgmColpensiones.Name);
	
	
	if(ctrlProscess){
		Session.Output("[PROCESS] Adding " + ElementNames.length + " New Elements type "+ ElementType);
		for (var i=0; i<ElementNames.length;i++){
			NewElements  = pkgElements.AddNew(ElementNames[i], ElementType);
			objDiagramas = dgmColpensiones.DiagramObjects.AddNew(ElementMeasures[1],"");
			objDiagramas.ElementID = NewElements.ElementID;
			objDiagramas.Update();
		}
		if (NewElements.Update()){
			Session.Output("[OK] Successful process");
		}
	}
	else {
		Session.Output("[PROCESS] Status: OFF");
	}
}
main();
