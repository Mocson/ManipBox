import maya.cmds as cmds

def wrd():
    cmds.manipMoveContext("Move", e=True, m=2)
    cmds.manipScaleContext("Scale", e=True, m=2)
    cmds.manipRotateContext("Rotate", e=True, m=2)

def lcl():
    cmds.manipMoveContext("Move", e=True, m=0)
    cmds.manipScaleContext("Scale", e=True, m=0)
    cmds.manipRotateContext("Rotate", e=True, m=0)

def cus():
    cmds.manipMoveContext("Move", e=True, m=6)
    cmds.manipScaleContext("Scale", e=True, m=6)
    cmds.manipRotateContext("Rotate", e=True, m=6)

cmds.window(title='ManipBox', w=200)
cmds.columnLayout(adj=True)
cmds.separator( h=3 )
cmds.text("MinipBox_V2")
cmds.separator( h=3 )
cmds.button( label = 'World', w=100, h=40, command='wrd()')

cmds.button( label = 'Object', w=100, h=40, command='lcl()')

cmds.button( label = 'Custom', w=100, h=40, command='cus()')

cmds.showWindow()
