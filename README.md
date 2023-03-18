# QtPythonConsole-Blender-add-on
a Blender add-on wrapper for [QtPythonConsole](https://github.com/Ahuge/QtPythonConsole), a simple qt script editor & console.
<img width="900" alt="image" src="https://user-images.githubusercontent.com/3758308/226135266-3f390cc6-64d7-4bf1-8ed4-61e85cedfd84.png">

## Support
- For bugs and feature requests for the original console, post the issue here: [QtPythonConsole issues](https://github.com/Ahuge/QtPythonConsole/issues) (but likely unsupported)
- For packaging and addon support, make a ticket in this repo: [QtPythonConsole-Blender-add-on issues](https://github.com/hannesdelbeke/QtPythonConsole-Blender-add-on/issues)


## Purpose
Mainly to test several types of dependencies:
- a Python module in a repo: [QtPythonConsole](https://github.com/Ahuge/QtPythonConsole)
- a Blender addon in a repo: [bqt](https://github.com/techartorg/bqt)
  - bqt has it's own dependency: Python pip install: `PySide2`

TODO:
- handle dependencies smarter
  - should work without bqt, with just PySide2 or PyQt5 if you handle the QT yourself.
