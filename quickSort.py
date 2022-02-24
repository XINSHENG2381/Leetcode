import random
def swap(a,b,arr):
    if a != b:
        tmp = arr[a]
        arr[a] = arr[b]
        arr[b] = tmp
    return

def partition(elements,start,end):
    pivot_index = start
    pivot = elements[pivot_index]

    while start < end:
        while start < len(elements) and elements[start] <= pivot:
            start += 1
        
        while elements[end] > pivot:
            end -= 1

        if start < end:
            swap(start,end,elements)
    
    swap(pivot_index,end,elements)
    
    return end

def quickSort(elements,start,end):
    if start < end:
        pi = partition(elements,start,end)
        quickSort(elements,start,pi - 1) #left partition
        quickSort(elements,pi + 1,end) #right partition



if __name__ == '__main__':
    elements = [11,9,29,7,2,15,28]
    quickSort(elements,0,len(elements)-1)
    print(elements)

