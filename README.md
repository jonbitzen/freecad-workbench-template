## Development

Following are some tips to set up the project and have hot reloading and code assistance to improve development productivity


### Developing a FreeCAD Workbench with Hot Reloading

- set up a new workbench according to the workbench template available on Github
  - be sure to use python modules and packages that use "__init__.py" so that package paths get automatically imported

- to develop the workbench efficiently, softlink the top-level module folder into the FreeCAD user modules directory
  - `ln -s ${WB_DEV_PATH}/MyWorkBench ~/.local/share/FreeCAD/Mod` where "MyWorkBench" is the top-level folder of your workbench, containing all the artifacts that are ingested by FreeCAD to instantiate your workbench
  - when working on your workbench, import your top level workbench module to bring it into FreeCAD.  doing so will allow you to reload it as follows:

```
import my_wb_module

# experiment, make changes to your source, then reload them
from importlib import reload
reload(my_wb_module)
```

### Vscode Type Hinting
- install FreeCAD into the /opt folder as an exploded AppImage archive; we need to install FreeCAD as an exploded archive so that we can obtain Python library paths, and provide them to vscode for python code analysis
  - `./FreeCAD*.AppImage --appimage-extract`
    - this will usually create a default folder name like "squashfs", which you should rename to something more recognizable
- in the workbench folder, create a hidden folder ".vscode", and inside it create a file called "settings.json"
- in the file settings.json, create the following properties
```
{
"python.analysis.stubPath": "FREECAD_STUB_PATH",
"python.analysis.extraPaths": [
    "LIB_PATH1",
    "LIB_PATH2",
    ...
    "LIB_PATHN"
]
}
```
#### Generating FreeCAD stubs

Some of the FreeCAD work benches are provided by native libraries, and require stub files to enable code assistance.

To generate the stubs:

- checkout the repository freecad-stubs, `git clone https://github.com/ostr00000/freecad-stubs`, and change to the latest available tagged version:
  - note that for FreeCAD 1.0, you should use commit `d57fd4a` as it contains fixes that allow it to parse FreeCAD 1.0 sources
- checkout the FreeCAD source, `git clone https://github.com/FreeCAD/FreeCAD.git` from inside the `freecad-stubs` repo folder
- enter the FreeCAD source checkout, and change to the desired branch
- edit the file `lib/freecad_stub_gen/config.py`, and change the variable `TARGET_DIR` from `freecad_stubs` to some other name.  This is where your stub files will be generated underneath the `freecad-stubs` repo folder
  - it is important to perform this step to avoid folder name collision, as the `freecad-stubs` repo already contains a generated stub folder
- in your terminal, set the PYTHONPATH variable to `PYTHONPATH="freecad-stubs/lib"`.  Note this step is not in the upstream instructions for `freecad-stubs` but is necessary to avoid module import errors when generating stubs
- go the the `freecad-stubs` *parent* directory, and run the command `python3 freecad-stubs/lib/freecad_stub_gen/__main__.py`
- after generating the stubs, copy it to a sub-folder called `stubs` underneath your exploded AppImage FreeCAD installation; then provide the new stub directory (e.g., `/opt/FreeCAD/stubs`) as the `FREECAD_STUB_PATH` variable noted above
  
#### Setting the FreeCAD Python Extra Paths

  - in `python.analysis.extraPaths`, fill in the entire python path set from the FreeCAD python console.  You can obtain this by starting FreeCAD, going to the python console, and entering the following:
```
import sys
print(sys.path)
```
  - you can use a text editor to reformat the path strings in a manner suitable for entry into the extraPaths variable above
    - format to get each path on its own line for viewing ease (replace ", " with ", \n" in a text editor)
    - replace single-quote string delimiters (`) with double-quotes (")
    - note that this will also contain the paths to installed workbenches that are usually in the user's local folder; if you add or remove workbenches from within FreeCAD, you may need to update the paths to include the changes
