#!/bin/bash
pyinstaller --onefile --icon=Roc_icon.ico --hidden-import About_GUI.py --hidden-import Auto_GUI.py --hidden-import Config.py --hidden-import GUI.py --hidden-import GUI_Graph.py --hidden-import Help_GUI.py --hidden-import Parsers.py Start_.py

