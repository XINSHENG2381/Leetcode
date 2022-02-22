 ################ 原始未改进算法 #################
def bubble_sort(elements):
    size = len(elements)

    for i in range(size - 1):
        for j in range(size - 1):
            if elements[j] > elements[j+1]:
                tmp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = tmp
    return  #原地排序，列表elemenys已改变，无须返回elements，仅return即可


################ 改进算法 #################
def bubble_sort_revised(elements): 
    size = len(elements)

    for i in range(size - 1):
        swapped = False
        for j in range(size - 1 - i):  #不再比较列表最末端的已排序的元素
            if elements[j] > elements[j+1]:
                tmp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = tmp
                swapped = True
        
        if not swapped:
            break

    return  #原地排序，列表elements已改变，无须返回elements，仅return即可


if __name__ == '__main__':
    elements = [5,9,2,1,67,34,88,34]

    # bubble_sort(elements)
    # print(elements)

    bubble_sort_revised(elements)
    print(elements)

    nameList = ['Zoe', 'Alice', 'Galahad', 'Ruby', 'George', 'Jerry', 'Batman', 'Monica']
    print(sorted(nameList))
    bubble_sort_revised(nameList)
    print(nameList)