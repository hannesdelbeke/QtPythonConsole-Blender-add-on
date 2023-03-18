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
    console_reference = None

    def execute(self, context):
        import QtPythonConsole.console as c
        from QtPythonConsole.Qt import QtCore, QtWidgets

        d = c.ConsoleDialog()
        d = c.ConsoleDialog(QtCore.Qt.Tool)
        # parent to bqt if available
        app = QtWidgets.QApplication.instance()
        bqt_setup = hasattr(app, 'blender_widget')
        if bqt_setup:
            d.setParent(app.blender_widget, QtCore.Qt.Window)
        d.show()

        # if not bqt_setup:
        #     app.exec_()

        global console_reference
        console_reference = d

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

