import maya.OpenMayaUI as omui
from PySide2 import QtWidgets, QtQuick, QtCore
from shiboken2 import wrapInstance

import create_prop


def Create_Window():
    Window = omui.MQtUtil.mainWindow()
    return wrapInstance(long(Window), QtWidgets.QWidget)

class UI(QtWidgets.QDialog):

    def __init__(self):

        super(UI, self).__init__(parent=Create_Window())
        self.create_prop = create_prop.Create_Prop()
        self.setWindowTitle("Prop Building")
        self.resize(300, 250)
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)
        self.create_widgets()
        self.create_layout()
        self.create_connections()

    def create_widgets(self):
        self.title_lbl = QtWidgets.QLabel("Building")
        self.title_lbl.setStyleSheet("font: bold 20px")

        self.height_lbl = QtWidgets.QLabel("Height")
        self.height_le = QtWidgets.QLineEdit()
        self.height_spinbox = QtWidgets.QSpinBox()
        self.width_lbl = QtWidgets.QLabel("Width")
        self.width_le = QtWidgets.QLineEdit()
        self.width_spinbox = QtWidgets.QSpinBox()
        self.length_lbl = QtWidgets.QLabel("Length")
        self.length_le = QtWidgets.QLineEdit()
        self.length_spinbox = QtWidgets.QSpinBox()

        self.close_btn = QtWidgets.QPushButton("Close")
        self.build_btn = QtWidgets.QPushButton("Build")

    def create_layout(self):
        self.height_lay = QtWidgets.QHBoxLayout()
        self.height_lay.addWidget(self.height_lbl)
        self.height_lay.addWidget(self.height_spinbox)

        self.width_lay = QtWidgets.QHBoxLayout()
        self.width_lay.addWidget(self.width_lbl)
        self.width_lay.addWidget(self.width_spinbox)

        self.length_lay = QtWidgets.QHBoxLayout()
        self.length_lay.addWidget(self.length_lbl)
        self.length_lay.addWidget(self.length_spinbox)

        self.button_lay = QtWidgets.QHBoxLayout()
        self.button_lay.addWidget(self.build_btn)
        self.button_lay.addWidget(self.close_btn)

        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.addWidget(self.title_lbl)
        self.main_layout.addWidget(self.height_lbl)
        self.main_layout.addWidget(self.height_spinbox)
        self.main_layout.addWidget(self.width_lbl)
        self.main_layout.addWidget(self.width_spinbox)
        self.main_layout.addWidget(self.length_lbl)
        self.main_layout.addWidget(self.length_spinbox)
        self.main_layout.addLayout(self.button_lay)
        self.setLayout(self.main_layout)

    def create_connections(self):
        self.close_btn.clicked.connect(self.cancel)
        self.build_btn.clicked.connect(self.build)

    @QtCore.Slot()
    def spinbox_value(self):
        self.create_prop.widthSelection = self.width_spinbox.value()
        self.create_prop.lengthSelection = self.length_spinbox.value()
        self.create_prop.heightSelection = self.height_spinbox.value()

    @QtCore.Slot()
    def build(self):
        self.create_prop.create_prop()

    @QtCore.Slot()
    def cancel(self):
        self.close()




