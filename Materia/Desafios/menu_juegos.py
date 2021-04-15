import consolemenu
from consolemenu import *
from consolemenu.items import *

menu=ConsoleMenu('titulo','subtitulo')
menuitem=MenuItem('item')

menu.append_item(menuitem)

def inc (x=0):
  return x+1
x=0
menu.append_item(FunctionItem('funcion=',inc))
menu.draw()
menu.append_item(FunctionItem.get_return())
menu.show()