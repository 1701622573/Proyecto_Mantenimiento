"""
TST class
"""
from nodo import TSTNode
class TST:
    """
    parameters class
    """
    paths = ""
    array_paths = []
    array_nodes_level = []

    def __init__(self):
        self.root = None
        self.weight = 0

    def _weight(self):
        """
        get weight
        """
        return self.weight

    def __len__(self):
        return self.weight

    def __setitem__(self, key, value):
        self.add_node(key, value)

    def add_node(self, key, name, party, father_key):
        """
        This method verifies if a tree exists, then the node is added as
        a root or as a child node
        """
        if self.root:
            if father_key == 0:
                self._add_node(key, name, self.root)
            else:
                current_node = self.get_node(self.root, father_key)
                if current_node:
                    self._add_node(key, name, party, current_node)
                else:
                    print("Nodo ", father_key, "no encontrado")
        else:
            self.root = TSTNode(key, name, party)
            print("The node " + str(name) + " has been added as the main root.")
        self.weight += 1

    def _add_node(self, id_node_to_add, name, party, current_node):
        """
        As a TST, the childs need to be add to the left, middle and right
        """
        if current_node.is_leaf():
            current_node.left_child = TSTNode(id_node_to_add, name, party, parent_node=current_node)
            print("The node " + str(name) + " has been added as left child of "
            + str(current_node.name))
        else:
            if not current_node.has_right_child():
                if not current_node.has_middle_child():
                    current_node.middle_child = TSTNode(id_node_to_add, name, party,
                        parent_node=current_node)
                    print("The node " + str(name) + " has been added as middle child of " +
                        str(current_node.name))
                else:
                    current_node.right_child = TSTNode(id_node_to_add, name,
                        party, parent_node=current_node)
                    print("The node " + str(name) + " has been added as right child of " +
                        str(current_node.name))
            else:
                print("The node " + str(name) + " can't be added as a child of " +
                str(current_node.name))

    def get_node(self, root, id_node_to_get):
        """
        Get node by key
        """
        if root:
            node = self._get_node(root, id_node_to_get)
            if node:
                return node
        else:
            return None

    def _get_node(self, current_node, id_node_to_get):
        """
        get child node
        """
        nod = None
        if current_node:
            if current_node.id == id_node_to_get:
                nod = current_node
                return nod

            if nod is None:
                nod = self._get_node(current_node.left_child, id_node_to_get)
            if nod is None:
                nod = self._get_node(current_node.middle_child, id_node_to_get)
            if nod is None:
                nod = self._get_node(current_node.right_child, id_node_to_get)
        return nod

    def del_node(self, root, id_node_to_delete):
        """
        delete node
        """
        print("\n___Deleting Node__")
        if root:
            node = self.get_node(root, id_node_to_delete)
            return self._del_node(node)
        return None

    def _del_node(self, current_node):
        flag = False
        find_flag = False

        if current_node.is_leaf():
            if current_node.is_left_child():
                print(current_node.id, "era hoja hijo izquierdo de", current_node.parent_node.id)
                current_node.parent_node.left_child = None
                if current_node.parent_node.has_middle_child():
                    current_node.parent_node.left_child = current_node.parent_node.middle_child
                    current_node.parent_node.middle_child = None
                if current_node.parent_node.has_right_child():
                    current_node.parent_node.middle_child = current_node.parent_node.right_child
                    current_node.parent_node.right_child = None
                current_node.parent_node = None
                flag = True
            elif current_node.is_middle_child():
                print(current_node.id, "era hoja hijo medio de", current_node.parent_node.id)
                current_node.parent_node.middle_child = None
                if current_node.parent_node.has_right_child():
                    current_node.parent_node.middle_child = current_node.parent_node.right_child
                    current_node.parent_node.right_child = None
                flag = True
            elif current_node.is_right_child():
                print(current_node.id, "era hoja hijo derecho de", current_node.parent_node.id)
                current_node.parent_node.right_child = None
                flag = True
            current_node.parent_node = None
        else:  # No leaf
            if not current_node.left_child.has_middle_child():
                if current_node.has_right_child():
                    current_node.right_child.parent_node = current_node.left_child
                    current_node.left_child.right_child = current_node.right_child
                    print(current_node.left_child.right_child.id, "movido a",
                        current_node.left_child.id)
                    current_node.right_child = None
                    flag = True
                if current_node.has_middle_child():
                    current_node.middle_child.parent_node = current_node.left_child
                    current_node.left_child.middle_child = current_node.middle_child
                    print(current_node.left_child.middle_Child.id, "movido a",
                    current_node.left_child.id)
                    current_node.middle_child = None
                    flag = True
            else:
                if current_node.has_all_childs():
                    if current_node.left_child.has_right_child():
                        self.find_empty_child(current_node.left_child.right_child,
                        current_node.right_child, find_flag)
                        current_node.left_child.right_child = None
                    self.find_empty_child(current_node.left_child.middle_Child,
                    current_node.middle_child, find_flag)
                    current_node.left_child.middle_child = None

                    current_node.middle_child.parent_node = current_node.left_child
                    current_node.left_child.middle_child = current_node.middle_child
                    current_node.middle_child = None
                    current_node.right_child.parent_node = current_node.left_child
                    current_node.left_child.right_child = current_node.right_Child
                    current_node.right_child = None
                    flag = True
                else:
                    if current_node.left_child.has_right_child():
                        self.find_empty_child(current_node.left_child.right_child,
                            current_node.middle_child, find_flag)
                        current_node.left_child.right_child = None
                    self.find_empty_child(current_node.left_child.middle_child,
                        current_node.middle_child, find_flag)
                    current_node.left_child.middle_child = None

                    current_node.middle_child.parent_node = current_node.left_child
                    current_node.middle_child = None
                    flag = True
            current_node.left_child.parent_node = current_node.parent_node
        if current_node == self.root:
            self.root = current_node.left_child
        if current_node.is_left_child():
            current_node.parent_node.left_child = current_node.left_child
            current_node.left_child = None
            flag = True
        elif current_node.is_middle_Child():
            current_node.parent_node.middle_child = current_node.left_child
            current_node.left_child = None
            flag = True
        elif current_node.is_right_Child():
            current_node.parent_node.right_child = current_node.left_child
            current_node.left_child = None
            flag = True
        return flag

    findbool = False


    def adopt_child_node(self, parent, child):
        """
        add the child node to the parent node

        Parameters
        ----------
        parent : Nodo
            node that will adopt the child node
        child : Nodo
            node to be adopted

        Returns
        -------
        bool
            returns true if the parent node was able to adopt the child node
        """
        if parent.is_leaf():
            child.parent_node = parent
            parent.left_child = child
            return True
        if not parent.has_right_child():
            if parent.has_middle_child():
                parent.middle_child = child
                parent.middle_child.parent_node = parent
            else:
                parent.right_child = child
                parent.right_child.parent_node = parent
            return True
        return False



    def find_empty_child(self, hijo_adop, padre_adop, find_bool):
        """
        recursively searches for a node that can adopt the child node

        Parameters
        ----------
        padreadop : Nodo
            node that will adopt the child node
        hijoadop : Nodo
            node to be adopted

        Returns
        -------
        bool
            returns true if it found a parent node and false if it didn't
        """
        if find_bool:
            print(hijo_adop.id, "reposition to", padre_adop.id)
            return True
        if padre_adop:
            if self.adopt_child_node(padre_adop, hijo_adop):
                find_bool = True
            else:
                if padre_adop.has_left_child():
                    find_bool = self.find_empty_child(hijo_adop, padre_adop.left_child, find_bool)
                if padre_adop.has_middle_child():
                    find_bool = self.find_empty_child(hijo_adop, padre_adop.middle_child, find_bool)
                if padre_adop.has_right_child():
                    find_bool = self.find_empty_child(hijo_adop, padre_adop.right_child,
                        find_bool)
        return find_bool

    def longer_path(self, root):
        """
        show the bigger path
        """
        if root:
            complet_path = self._paths(root, self.array_paths,
                                    self.paths)
            print(len(complet_path))
            num_nodos = 0
            for arreglo_caminos in complet_path:
                i = 0
                for k in arreglo_caminos:
                    i += 1
                if num_nodos < i:
                    num_nodos += 1
                    camino = arreglo_caminos
            print(camino)
            return camino
        print("El arbol no existe")
        return None

    def _paths(self, root, arreglo, caminos):
        """
        find all paths from foot to leaf
        """
        if root.is_leaf():
            caminos = caminos + str(root.id) + ";"
            arreglo.append(caminos)
        else:
            caminos = caminos + str(root.id) + ";"
            if root.has_left_child():
                self._paths(root.left_child, arreglo, caminos)
            if root.has_middle_child():
                self._paths(root.middle_child, arreglo, caminos)
            if root.has_right_child():
                self._paths(root.right_child, arreglo, caminos)
        arreglado = self.path_fixer(arreglo)
        return arreglado

    def path_fixer(self, arrayPath):
        """
        Fix Array of Strings to Array of Arrays
        """
        separated_arr = []
        for k in arrayPath:
            j = str(k)
            separated_arr.append(j.split(";"))

        for x in separated_arr:
            x.remove('')
        return separated_arr

    def complete_tree(self, root):
        """
        helps to know if a tree is complete
        """
        complete_bool = True
        if root is None:
            return []
        levels = self.get_nodes_by_level(root)
        i = 0
        for level in levels:
            if i < len(levels) - 2:
                print("Nivel", i, "-", level)
                for lvl in level:
                    node = self.get_node(root, int(lvl[0]))
                    if node:
                        if not node.has_all_childs():
                            complete_bool = False
            i += 1
        if complete_bool:
            print("IT IS A COMPLETE TREE")
        else:
            print("IT IS NOT A COMPLETE TREE")
        return complete_bool

    def full_tree(self, root):
        """
        helps to know if a tree is complete
        """
        full_bool = True
        if root is None:
            return []
        levels = self.get_nodes_by_level(root)
        i = 0
        for level in levels:
            if i < len(levels) - 2:
                print("Nivel", i, "-", level)
                for lvl in level:
                    node = self.get_node(root, int(lvl[0]))
                    if node:
                        if not node.has_all_childs():
                            full_bool = False
            i += 1
        if full_bool:
            print("IT IS A COMPLETE TREE")
        else:
            print("IT IS NOT A COMPLETE TREE")
        return full_bool

    def pre_order(self, root):
        """
        run tree in pre order
        """
        print(root.name, root.id)
        if root.has_left_child():
            self.pre_order(root.left_child)
        if root.has_middle_child():
            self.pre_order(root.middle_child)
        if root.has_right_child():
            self.pre_order(root.right_child)

    def in_order(self, root):
        """
        run tree in in order
        """
        if root.has_left_child():
            self.in_order(root.left_child)
        if root.has_middle_child():
            self.in_order(root.middle_child)
        print(root.name, root.id)
        if root.has_right_child():
            self.in_order(root.right_child)

    def pos_order(self, root):
        """
        run tree in pos order
        """
        if root.has_left_child():
            self.pos_order(root.left_child)
        if root.has_middle_child():
            self.pos_order(root.middle_child)
        if root.has_right_child():
            self.pos_order(root.right_child)
        print(root.name, root.id)

    def level_order(self, root):
        """
        Nodes by level
        """
        if root is None:
            return []
        res = []
        nodes = [root]
        while nodes:
            res.append([(node.id, node.name) for node in nodes])
            next_nodes = []
            for node in nodes:
                if node.has_left_child():
                    next_nodes.append(node.left_child)
                if node.has_middle_child():
                    next_nodes.append(node.middle_child)
                if node.has_right_child():
                    next_nodes.append(node.right_child)
            nodes = next_nodes
        return res

    def num_childs(self, root):
        """
        Number of nodes by Level
        """
        res = self.level_order(root)
        nc = []
        for x in res:
            nc.append(len(x))
        return nc

    def sum_childs(self, root):
        """
        Sum of totality by nodes
        """
        suma = 0
        nc = self.num_childs(root)
        for i in nc:
            suma = suma + i
        return suma

    def get_nums_childs(self, nodo):
        """
        get the number childs
        """
        i = 0
        if nodo.has_left_child():
            i += 1
        if nodo.has_middle_child():
            i += 1
        if nodo.has_right_child():
            i += 1
        return i

    def add_new_node(self, id_new_node, name, party, fatherkey):
        """
        add new node
        """
        self.add_node(id_new_node, name, party, fatherkey)

    def get_nodes_by_level(self, root):
        """
        get nodes by level
        """
        if self.array_nodes_level:
            return self.array_nodes_level
        array_nodes_level = self.level_order(root)
        return array_nodes_level

    def levels(self, root):
        """
        levels
        """
        path = self.longer_path(root)
        for i in range(len(path)):
            x = i + 1
        print(x)

    def height(self, root):
        """
        height
        """
        path = self.longer_path(root)
        for i in range(len(path)):
            x = i + 1
        print(x)

    def send_message(self, sml, current_node, message_node):
        """
        send message
        """
        ide = self.get_node(self.root, current_node).id
        complet_path = self._paths(self.root, self.array_paths, self.paths)
        sml.append(str(ide))
        if self.get_node(self.root, current_node).has_parent_node():
            self.send_message(sml, self.get_node(self.root, current_node).parent_node.id,
                            message_node)
        for i in complet_path:
            if i[len(i) - 1] == str(message_node):
                iq = i
        sml.append(iq)
        print(sml)
        return sml
