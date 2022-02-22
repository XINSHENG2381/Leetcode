###### This is a bubble_sort exercise for a given list of transactions and sorting it according to its key ########
def bubble_sort(elements, key):
    size = len(elements)
    for i in range(size -1 ):
        swapped = False
        for j in range(size - 1 - i):
            if elements[j][key] > elements[j+1][key]:
                tmp = elements[j][key]
                elements[j][key] = elements[j+1][key]
                elements[j+1][key] = tmp
                swapped = True
        if not swapped:
            break
    return


elements = [
    {'name':'mona','transaction_amount': 1000, 'device': 'iphone-13'},
    {'name':'ted','transaction_amount': 500, 'device': 'google pixel'},
    {'name':'robin','transaction_amount': 800, 'device': 'ipad'},
    {'name':'ruby','transaction_amount': 200, 'device': 'macbook-pro'},
]


# print(elements[0]['transaction_amount'])
bubble_sort(elements,key = 'transaction_amount')
print(elements)