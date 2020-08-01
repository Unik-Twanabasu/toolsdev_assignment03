import maya.OpenMayaUI as omui
import maya.cmds as cmds
import pymel.core as pmc


print("inside")


class Create_Prop(object):
    x = 5
    y = 6
    z = 7

    def __init__(self):
        self.x = 1
        print(self.x)

    def create_prop(self, widthSection= 5, lengthSection=6, heightSection=7):
        cmds.select('window_')
        print("selecting window...")
        i = 1
        while i <= widthSection:
            width = cmds.getAttr('width.distance')
            print(width)
            cmds.duplicate()
            cmds.move(-width, 0, 0, relative=True)
            i += 1

            cmds.rotate(0, '-90deg', 0, relative=True)

            i = 1
            while i <= lengthSection:
                length = cmds.getAttr('width.distance')
                cmds.duplicate()
                cmds.move(0, 0, -length, relative=True)
                i += 1

            #comds()
            cmds.select('window_*')
            cmds.group(relative=True)
            cmds.duplicate()
            cmds.rotate(0, '180deg', 0, relative=True)
            cmds.ungroup('group1', relative=True)
            cmds.select('group2')
            cmds.ungroup()
            cmds.select('window_*')
            cmds.group(relative=True)

            i = 1
            while i <= heightSection:
                height = cmds.getAttr('height.distance')
                cmds.duplicate()
                cmds.move(0, height, 0, relative=True)
                i += 1

