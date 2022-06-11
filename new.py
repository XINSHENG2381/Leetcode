def dfs1(root):
    if not root:
        return 

    dfs1(root.left)
    lst1.append(root.val)
    dfs1(root.right)

def dfs2(root):
    if not root:
        return 

    dfs2(root.left)
    lst2.append(root.val)
    dfs2(root.right)

if __name__ == '__main__':
    root = input()
    layer0 = root.val
    lst1 = []
    lst2 = []
    dfs1(root.left)
    dfs2(root.right)

    ###打印左边###
    print(layer0+'->',end = '')
    for i in range(len(lst1)):
        print(lst1[i]+'->')
    print(lst1[-1])

    ###打印右边###
    print(layer0+'->',end = '')
    for i in range(len(lst2)):
        print(lst2[i]+'->')
    print(lst2[-1])
