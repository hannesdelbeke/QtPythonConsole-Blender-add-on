# QtPythonConsole-Blender-add-on
a Blender add-on wrapper for [QtPythonConsole](https://github.com/Ahuge/QtPythonConsole), a simple qt script editor & console.
<img width="900" alt="image" src="https://user-images.githubusercontent.com/3758308/226135266-3f390cc6-64d7-4bf1-8ed4-61e85cedfd84.png">

## Support
- Bugs & feature requests for the original console go here: [QtPythonConsole issues](https://github.com/Ahuge/QtPythonConsole/issues) (likely unsupported)
- Packaging & Blender add-on support here: [QtPythonConsole-Blender-add-on issues](https://github.com/hannesdelbeke/QtPythonConsole-Blender-add-on/issues)


## Purpose
This repo was made to test several types of dependencies, as a demo for [plugget](https://github.com/hannesdelbeke/plugget). (See the 
QtPythonConsole plugget package)
- a Python module in a repo: [QtPythonConsole](https://github.com/Ahuge/QtPythonConsole)
- a Blender addon in a repo: [bqt](https://github.com/techartorg/bqt)
  - bqt has it's own dependency: Python pip install: `PySide2`

TODO:
- handle dependencies smarter
  - should work without bqt, with just PySide2 or PyQt5 if you handle the QT yourself.
