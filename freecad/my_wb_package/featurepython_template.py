import FreeCAD as App
from typing import Tuple


class MyFeature():
    def __init__(
        self,
        obj: App.DocumentObject
    ) -> None:
        
        obj.Proxy = self


    def onChanged(self, obj: App.DocumentObject, property: str) -> None:
        """
        Called when FreeCAD Properties attached to the FeaturePython object are
        changed, so they can be handled by this class (the Proxy)
        """
        pass

    def attach(self, obj: App.DocumentObject) -> None:
        """
        TODO: Explain what this method does
        """
        pass

    def execute(self, obj: App.DocumentObject) -> None:
        """
        Called when FreeCAD updates a DocumentObject
        """
        pass

class MyFeatureViewProvider():
    def __init__(
            self,
            vobj: App.Gui.ViewProviderDocumentObject
        ) -> None:
        vobj.Proxy = self
        self.Object = vobj.Object
        
    def getIcon(self) -> str:
        return None
    
    def attach(self, vobj: App.Gui.ViewProviderDocumentObject) -> None:
        pass

    def onDelete(self, vobj: App.Gui.ViewProviderDocumentObject, subelements: Tuple[str]) -> bool:
        return True
    
    def onChanged(self, vob: App.Gui.ViewProviderDocumentObject, prop: str) -> None:
        pass

