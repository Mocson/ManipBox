import maya.cmds as cmds

def ManiObj():
    cmds.manipMoveContext("Move", e=True, m=0)

def ManiWrd():
    cmds.manipMoveContext("Move", e=True, m=2)

def ManiCus():
    cmds.manipMoveContext("Move", e=True, m=6)

cmds.window(title='ManipBox', w=150)
cmds.columnLayout(adj=True)
cmds.button( label = 'Object', w=100, h=40, command='ManiObj()')
cmds.button( label = 'World', w=100, h=40, command='ManiWrd()')
cmds.button( label = 'Custom', w=100, h=40, command='ManiCus()')
cmds.textField('tFld')

cmds.showWindow()
