import maya.cmds as cmds

def ManiObjMove():
    cmds.manipMoveContext("Move", e=True, m=0)

def ManiWrdMove():
    cmds.manipMoveContext("Move", e=True, m=2)

def ManiCusMove():
    cmds.manipMoveContext("Move", e=True, m=6)

def ManiObjScale():
    cmds.manipScaleContext("Scale", e=True, m=0)

def ManiWrdScale():
    cmds.manipScaleContext("Scale", e=True, m=2)

def ManiCusScale():
    cmds.manipScaleContext("Scale", e=True, m=6)

def ManiObjRotate():
    cmds.manipRotateContext("Rotate", e=True, m=0)

def ManiWrdRotate():
    cmds.manipRotateContext("Rotate", e=True, m=2)

def ManiCusRotate():
    cmds.manipRotateContext("Rotate", e=True, m=6)

cmds.window(title='ManipBox', w=150)
cmds.columnLayout(adj=True)

cmds.separator( h=3 )
cmds.text("World")
cmds.separator( h=3 )
cmds.button( label = 'Object', w=100, h=20, command='ManiObjMove()')
cmds.button( label = 'World', w=100, h=20, command='ManiWrdMove()')
cmds.button( label = 'Custom', w=100, h=20, command='ManiCusMove()')

cmds.separator( h=3 )
cmds.text("Scale")
cmds.separator( h=3 )
cmds.button( label = 'Object', w=100, h=20, command='ManiObjScale()')
cmds.button( label = 'World', w=100, h=20, command='ManiWrdScale()')
cmds.button( label = 'Custom', w=100, h=20, command='ManiCusScale()')

cmds.separator( h=3 )
cmds.text("Rotate")
cmds.separator( h=3 )
cmds.button( label = 'Object', w=100, h=20, command='ManiObjRotate()')
cmds.button( label = 'World', w=100, h=20, command='ManiWrdRotate()')
cmds.button( label = 'Custom', w=100, h=20, command='ManiCusRotate()')

cmds.showWindow()
