class treeNode:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None
    
    def add_child(self,child): #here child should be a treeNode object
        child.parent = self
        self.children.append(child)
        return
    
    # def get_level(self):
    #     level = 0
    #     p = self.parent
    #     while p:
    #         level += 1
    #         p = self.parent
    #     return level
        

    def print_tree(self):
        print(self.data)
        if len(self.children):
            for child in self.children:
                child.print_tree()


def buildTree():
    N = treeNode('Nilupul')
    C = treeNode('Chinmay')
    V = treeNode('Vishwa')
    D = treeNode('Dhaval')
    A = treeNode('Abhijit')
    Aa = treeNode('Aamir')
    G = treeNode('Gels')
    P = treeNode('Peter')
    W = treeNode('Waqas')
    
    N.add_child(C)
    N.add_child(G)
    C.add_child(V)
    C.add_child(Aa)
    V.add_child(D)
    V.add_child(A)
    G.add_child(P)
    G.add_child(W)

    # print(N.get_level())

    return N




if __name__ == '__main__':
    root = buildTree()
    root.print_tree()

    