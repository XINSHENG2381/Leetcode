class treeNode:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self,child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent 
        while p:  # 自下而上查找parent的数量，即可知level值
            level += 1
            p = self.parent
        return level


    def print_tree(self):
        spaces = ' ' * 4 *self.get_level()
        prefix = spaces + '|__' if self.parent else ""
        print(prefix + self.data)
        if len(self.children):
            for child in self.children:
                # print(child.data)
                child.print_tree() 

def build_product_tree():
    root = treeNode('Electronics') #class括号内容即赋值给def __init__（self,data）里面的data

    laptop = treeNode('Laptop')
    laptop.add_child(treeNode('Macbook'))
    laptop.add_child(treeNode('Surface'))
    laptop.add_child(treeNode('Thinkpad'))
    
    cellphone = treeNode('Cellphone')
    cellphone.add_child(treeNode('iPhone'))
    cellphone.add_child(treeNode('Google Pixel'))
    cellphone.add_child(treeNode('Vivo'))

    tv = treeNode('TV')
    tv.add_child(treeNode('Samsung'))
    tv.add_child(treeNode('LG'))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    # print(root.get_level())
    return root


if __name__ == '__main__':
    root = build_product_tree()
    root.print_tree()
