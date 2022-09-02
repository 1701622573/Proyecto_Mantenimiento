"""
Main Class
"""
import json
from ternary_search_tree import TST

myTree = TST()
def cargar_datos(ruta):
    """
    Load the file and show it
    """
    with open(ruta, encoding='UTF-8') as contenido:
        estruc = json.load(contenido)
        buscar_hijos(estruc)

def buscar_hijos(estr):
    """
    Busca los hijos de un nodo en especifico
    """
    for pers in estr.get('people'):
        print(pers.get('id'), pers.get('name'))
        myTree.add_node(pers.get('id'), pers.get('name'), pers.get('party'), 0) #NUEVA
        _buscar_hijos(pers)


def _buscar_hijos(padre):
    """
    Busca los hijos que tiene un nodo padre
    """
    for pad in padre.get('childrens'):
        print(padre.get('id'),".",pad.get('id'), pad.get('name'))
        myTree.add_node(pad.get('id'), pad.get('name'), pad.get('party'),padre.get('id')) #NUEVA
        #hasChilds(pad)
        hijos = str(pad.get('childrens'))
        if hijos != "[]":
            _buscar_hijos(pad)

def update():
    """Update"""
    print("\n")
    print ("----Level Order----")
    myTree.level_order(myTree.root)

    print("\n\n")
    print ("----Preorder----")
    myTree.pre_order(myTree.root)

    print("\n\n")
    print ("----Inorder----")
    myTree.in_order(myTree.root)


    print("\n\n")
    print ("----Posorde")
    myTree.pos_order(myTree.root)

    print("\n")
    print ("----Longer Path----")
    myTree.longer_path(myTree.root)

    print("\n")
    print ("----Complete Tree----")
    myTree.complete_tree(myTree.root)

    print("\n")
    print ("----Full Tree----")
    myTree.full_tree(myTree.root)

RUTA = "data/formatJSON.json"
cargar_datos(RUTA)
update()
