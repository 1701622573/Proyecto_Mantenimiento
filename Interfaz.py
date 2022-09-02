import re
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import ttk
from tkinter.ttk import *
import tkinter as tk
import json
from ternary_search_tree import TST
from nodo import TSTNode


app = Tk()
style = ttk.Style()
style.configure("BW.TLabel", foreground="black", background = "black")
app.title('Congreso')
imgPerson = PhotoImage(file="./images/congre.png")


myTree = TST()
ventana = 0


# Loading data JSON
def cargarDatos(ruta):
    with open(ruta) as contenido:
        estruc = json.load(contenido)
        buscarHijos(estruc)
        pintar()
                    
def buscarHijos(estr):
    for pers in estr.get('people'):
        print(pers.get('id'), pers.get('name'))
        myTree.add_node(pers.get('id'), pers.get('name'), pers.get('party'), 0) #NUEVA
        _buscarHijos(pers)
        
def _buscarHijos(padre):
    for pad in padre.get('childrens'):
        print(padre.get('id'),".",pad.get('id'), pad.get('name'))
        myTree.add_node(pad.get('id'), pad.get('name'), pad.get('party'),padre.get('id')) #NUEVA
        #hasChilds(pad)
        hijos = str(pad.get('childrens'))
        if(hijos != "[]"):
            _buscarHijos(pad)

def update():
    
    print("\n")
    print ("----Level Order----")
    myTree.level_order(myTree.root)
    print(myTree.levelOrder(myTree.root))


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


def pintar():
    nvl = myTree.num_childs(myTree.root)#List with the numbers of nodes
    nodes = myTree.level_order(myTree.root)#List of the nodes for level
    snodes = myTree.sum_childs(myTree.root)#Sum of numbers of nodes
    listpos = []
    pixels = 1280
    height = 110
    ArrayPos = []
    posNodes = []
    Nods = []

    #Create list of the names and ids, level order
    for e in nodes:
        for i in range(0, len(e)):
            Nods.append(e[i])

    #Create list of positions
    for i in range(0, len(nvl)):
        aux = []
        division = (nvl[i]) + 1#The screen is divided according to the number of nodes per level
        for j in range(0, nvl[i]):
            aux.append(((pixels // division) * (j + 1), height * (i + 1)))#The pixels are divided and divided by the number, and given a certain height
        ArrayPos.append(aux.copy())#The x and y directions are copied into an Array
    for e in ArrayPos:
        for i in range(0, len(e)):
            posNodes.append(e[i])
            canvas.create_image(e[i][0], e[i][1]-20, anchor= NW, image = imgPerson)#Create image person for people
    for i in range(0, snodes):
        Txtid = Label(canvas, text = Nods[i][0]).place(x = posNodes[i][0]+40,y = posNodes[i][1])#Add label ID information
        Txtname = Label(canvas, text = Nods[i][1]).place(x = posNodes[i][0]+40,y = posNodes[i][1]-20)#Add label name information
        if (myTree.get_node(myTree.root, Nods[i][0]).party) == 1:#If party in people is equals to 1, rectangle is red
            canvas.create_rectangle(posNodes[i][0]+5, posNodes[i][1]+10, posNodes[i][0] + 30, posNodes[i][1] + 30, fill="red")
        elif(myTree.get_node(myTree.root, Nods[i][0]).party) == 2:#If party in people is equals to 1, rectangle is blue
            canvas.create_rectangle(posNodes[i][0]+5, posNodes[i][1]+10, posNodes[i][0] + 30, posNodes[i][1] + 30, fill="blue")
        elif(myTree.get_node(myTree.root, Nods[i][0]).party) == 3:#If party in people is equals to 1, rectangle is green
            canvas.create_rectangle(posNodes[i][0]+5, posNodes[i][1]+10, posNodes[i][0] + 30, posNodes[i][1] + 30, fill="green")
        else:#If party in people is equals to 1, rectangle is yellow
            canvas.create_rectangle(posNodes[i][0]+5, posNodes[i][1]+10, posNodes[i][0] + 30, posNodes[i][1] + 30, fill="yellow")

    #SETTING LINES
    print("\n -- INTERFAZ --")
    print(nodes) #Array of nodes by level
    print(ArrayPos) #Array of nodes position by level
    i = 0 
    level = len(ArrayPos) #Array positions of nodes by level
    for nivel in nodes: #walk into levels array
        if(i + 1 >= level): #
            break
        coordenadasPadre = ArrayPos[i]
        coordenadasHijos = ArrayPos[i + 1]
        j = 0
        posHijos = 0
        if(i < len(nodes)):#goes to the penultimate level  -  i<level-1  -  (height-1)
            for nodos in nivel:
                coordenadaPadre = coordenadasPadre[j]
                node = myTree.get_node(myTree.root, int(nodos[0]))
                numHijos = myTree.get_nums_childs(node)
                if(numHijos != 0):
                    for num in range(numHijos):
                        coordenadaHijo = coordenadasHijos[posHijos]
                        canvas.create_line(coordenadaPadre[0] + 25, coordenadaPadre[1] + 40, coordenadaHijo[0] + 25, coordenadaHijo[1] -25, width=3, fill="gray")
                        posHijos += 1
                j += 1
        i += 1 #identify the level

#Create new window for add new node
def addNewNodeWindow(win):
    win.deiconify()#Show the window
    #New entry id
    newID = Label(win, text="Id congresista").grid(row = 0, column = 0)#Indicative label
    entryVarID = tk.IntVar()#New integer variable for the id
    entryID = Entry(win, textvariable = entryVarID).grid(row = 0, column = 1)#Text Entry
    #New entry name
    newName = Label(win, text="Nombre congresista").grid(row = 1, column = 0)#Indicative label
    entryVarName = tk.StringVar()#New String variable for the name
    entryName = Entry(win,textvariable = entryVarName).grid(row = 1, column = 1)#Text Entry
    #New entry party
    newParty = Label(win, text="ID del Party").grid(row = 2, column = 0)#Indicative label
    entryVarParty = tk.IntVar()#New integer variable for the party
    entryParty = Entry(win,textvariable = entryVarParty).grid(row = 2, column = 1)#Text Entry
    #Entry father id
    fatherId = Label(win, text = "ID del padre").grid(row = 3, column = 0)#Indicative label
    entryVarF = tk.IntVar()#New integer variable for the Father ID
    entryFID = Entry(win,textvariable = entryVarF).grid(row = 3, column = 1)#Text Entry
    

    btnAdd = ttk.Button(win, text="Agregar congresista",command = lambda: (myTree.add_node(entryVarID.get(),entryVarName.get(),entryVarParty.get(),entryVarF.get()),repintar())).grid(row = 6, column = 0)
    btnClose = ttk.Button(win, text = "Cerrar Ventana", command = lambda: win.withdraw()).grid(row = 6, column = 1)

#New window for add new node
def addDeleteNodeWindow(win1):
    win1.deiconify()#Show the window
    delId = Label(win1, text= "ID a eliminar").grid(row = 0, column = 0)#Indicative label
    entryDelVar = tk.IntVar()#New integer variable for the id
    entryDelID = Entry(win1, textvariable = entryDelVar).grid(row = 0, column = 1)#Text Entry

    btnDel = ttk.Button(win1, text="Eliminar congresista", command = lambda:(myTree.del_node(myTree.root,entryDelVar.get()), repintar())).grid(row = 6, column = 0)
    btnClose = ttk.Button(win1, text = "Cerrar Ventana", command =lambda: win1.withdraw()).grid(row = 6, column = 1)

#New window for supplant node for new node
def supplantNodeWindow(win2):
    win2.deiconify()#Show the window
    suppID = Label(win2, text = "ID congresista a suplantar").grid(row = 0, column = 0)#Indicative label
    entrySupVar = tk.IntVar()#New integer variable for the id
    entrySup = Entry(win2, textvariable = entrySupVar).grid(row = 0, column = 1)#Text Entry
    newName = Label(win2, text="Nombre congresista suplente").grid(row = 1, column = 0)#Indicative label
    entryVarName = tk.StringVar()#New String variable for the name
    entryName = Entry(win2,textvariable = entryVarName).grid(row = 1, column = 1)#Text Entry
    newID = Label(win2, text = "ID congresista suplente").grid(row = 2, column = 0)#Indicative label
    entryNewSup = tk.IntVar()#New integer variable for the id new
    entryNSup = Entry(win2, textvariable = entryNewSup).grid(row =2, column = 1)#Text Entry
    btnSupp = ttk.Button(win2, text="Suplantar congresista", command = lambda: (suppNode(entrySupVar.get(),entryNewSup.get(),entryVarName.get()), repintar())).grid(row = 6, column = 0)
    btnClose = ttk.Button(win2, text = "Cerrar Ventana", command =lambda: win2.withdraw()).grid(row = 6, column = 1)

#Function for supplant node
def suppNode(id, id1, name1):
    currentNode = myTree.get_node(myTree.root, id)#The node is obtained
    if currentNode == None:#If node is equals to None, print node does not exist
        print("No existe el nodo")
    else:#If node is't None, its name and id are changed
        currentNode.name = name1#Change name node for new name
        currentNode.id = id1#Change id node for new id
        print("Congresista suplantado")
        update()#Reprint tours
        pintar()#Repaint canvas

def messageWindow(win3):
    win3.deiconify()#Show the window
    sml = []
    emiID = Label(win3, text = "ID del Emisor").grid(row = 0, column = 0)#Indicative label
    entryEmiVar = tk.IntVar()#New integer variable for the id
    entryEmi = Entry(win3, textvariable = entryEmiVar).grid(row = 0, column = 1)#Text Entry
    recID = Label(win3, text = "ID del receptor").grid(row = 1, column = 0)#Indicative label
    entryRecVar = tk.IntVar()#New integer variable for the id
    entryRec = Entry(win3, textvariable = entryRecVar).grid(row = 1, column = 1)#Text Entry
    btnEn = ttk.Button(win3, text="Enviar Mensaje", command = lambda: myTree.sendMessage(sml, entryEmiVar.get(),entryRecVar.get())).grid(row = 6, column = 0)
    btnClose = ttk.Button(win3, text = "Cerrar Ventana", command =lambda: win3.withdraw()).grid(row = 6, column = 1)




def addJSON():
    filename = askopenfilename()
    fn = filename
    print(fn)
    return fn

def repintar():
    canvas.delete("all")
    update()
    pintar()


content = Frame(app)
content.pack(side = BOTTOM)
content.config(width=1360, height=760)

canvas = Canvas(content, width = 1360, height =700, bg = 'white')
canvas.place(x=0, y=0)

#Menu Interfaz
menuBar = Menu(app)#A menu bar is created
app.config(menu=menuBar)#Config menu bar

archivoMenu = Menu(menuBar, tearoff= 0)
archivoMenu.add_command(label= 'Importar Datos', command= lambda : (cargarDatos(addJSON())))
archivoMenu.add_command(label = 'Cerrar', command = lambda: (canvas.delete("all")))

#Menu Editar
editarMenu = Menu(menuBar, tearoff= 0)
editarMenu.add_command(label = 'Agregar ', command = lambda: (addNewNodeWindow(win)))
editarMenu.add_command(label = 'Eliminar ', command = lambda: (addDeleteNodeWindow(win1)))
editarMenu.add_command(label = 'Suplantar ', command = lambda: (supplantNodeWindow(win2)))

menuBar.add_cascade(label= 'Archivo', menu= archivoMenu)
menuBar.add_cascade(label= 'Editar', menu= editarMenu)

win = Toplevel(app)#Creation new window
win.geometry('300x150')#Size of window
win.configure(background = 'white')#Color of background window
win.title('Ingreso nuevo congresista')#Title of the window
win1 = Toplevel(app)#Creation new window
win1.geometry('300x150')#Size of window
win1.configure(background = 'white')#Color of background window
win1.title('Eliminar Congresista')#Title of the window
win2 = Toplevel(app)#Creation new window
win2.geometry('300x150')#Size of window
win2.configure(background = 'white')#Color of background window
win2.title('Suplantar Congresista')#Title of the window
win3 = Toplevel(app)#Creation new window
win3.geometry('300x150')#Size of window
win3.configure(background = 'white')#Color of background window
win3.title('Enviar Mensaje')#Title of the window

#btnAdd = ttk.Button(app, text="Agregar congresista", command = lambda: addNewNodeWindow(win)).pack(side = LEFT)
#btnDel = ttk.Button(app, text="Eliminar congresista", command = lambda : addDeleteNodeWindow(win1)).pack(side = LEFT)
#btnSup = ttk.Button(app, text="Suplantar congresista", command = lambda: supplantNodeWindow(win2)).pack(side = LEFT)
#btnMes = ttk.Button(app, text="Enviar Mensaje", command = lambda: messageWindow(win3)).pack(side = LEFT)
#btnUdt = ttk.Button(app, text="Generar recorridos", command = lambda: update()).pack(side = LEFT)
#tnRep = ttk.Button(app, text="Repintar", command = lambda : repintar()).pack(side = LEFT)

win.withdraw()#Hide the window
win1.withdraw()#Hide the window
win2.withdraw()#Hide the window
win3.withdraw()#Hide the window

app.mainloop()
