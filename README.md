# QtPythonConsole-Blender-add-on
a Blender add-on wrapper for [QtPythonConsole](https://github.com/Ahuge/QtPythonConsole)

## Purpose
Mainly to test several types of dependencies:
- a Python module in a repo: [QtPythonConsole](https://github.com/Ahuge/QtPythonConsole)
- a Blender addon in a repo: [bqt](https://github.com/techartorg/bqt)
  - bqt has it's own dependency: Python pip install: `PySide2`

TODO:
- handle dependencies smarter
  - should work without bqt, with just PySide2 or PyQt5 if you handle the QT yourself.
