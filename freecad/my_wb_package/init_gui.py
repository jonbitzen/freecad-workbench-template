import os
import FreeCADGui as Gui
import FreeCAD as App
from freecad.my_wb_package import ICONPATH


class WorkbenchTemplate(Gui.Workbench):
    """
    class which gets initiated at startup of the gui
    """

    MenuText = "My Workbench Template"
    ToolTip = "A workbench template with vscode integration"
    Icon = os.path.join(ICONPATH, "icons8-airplane-64.png")
    toolbox = []

    def GetClassName(self) -> str:
        return "Gui::PythonWorkbench"

    def Initialize(self) -> None:
        """
        This function is called at the first activation of the workbench.
        here is the place to import all the commands
        """

        self.appendToolbar("Tools", self.toolbox)
        self.appendMenu("Tools", self.toolbox)

    def Activated(self) -> None:
        """
        This method is called whenever the workbench is activated
        """
        pass

    def Deactivated(self) -> None:
        """
        This method is called whenever the workbench is deactivated
        """
        pass


Gui.addWorkbench(WorkbenchTemplate())
