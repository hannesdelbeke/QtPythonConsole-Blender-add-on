bl_info = {
    "name": "Qt Python editor & console",
    "description": "open a python editor & console",
    "author": "Alex Hughes, Hannes D",
    "version": (1, 0),
    "blender": (2, 91, 0),
    "location": "",
    "category": "Development"
}

import bpy


class QtConsolePreferences(bpy.types.AddonPreferences):
    bl_idname = __name__

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.operator("wm.open_qt_console", text="Open Console")


class OpenConsoleOperator(bpy.types.Operator):
    bl_idname = "wm.open_qt_console"
    bl_label = "Python Editor & Console"
    console_widget = None

    def execute(self, context):
        import QtPythonConsole.console
        from QtPythonConsole.Qt import QtCore, QtWidgets
        
        app = QtWidgets.QApplication.instance()
        if not app:
            app = QtWidgets.QApplication()
        
        args = []
        # parent to bqt if available to keep widget in front
        if hasattr(app, 'blender_widget'):
            args = [app.blender_widget]
        args.append[QtCore.Qt.Tool]
            
        self.console_widget = QtPythonConsole.console.ConsoleDialog(*args)            
        self.console_widget.show()

        return {'FINISHED'}


def menu_func(self, context):
    self.layout.operator(OpenConsoleOperator.bl_idname)


def register():
    import QtPythonConsole.console  # test if we can import the console
    bpy.utils.register_class(QtConsolePreferences)
    bpy.utils.register_class(OpenConsoleOperator)
    bpy.types.TOPBAR_MT_window.append(menu_func)


def unregister():
    bpy.utils.unregister_class(QtConsolePreferences)
    bpy.utils.unregister_class(OpenConsoleOperator)
    bpy.types.TOPBAR_MT_window.remove(menu_func)

