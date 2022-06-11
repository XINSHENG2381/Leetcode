from unittest import result


def fixed_sliding_window(arr: list[int], k:int)-> int: 
    # input arr: List[int] -- given array
    # k: int -- number of elements in one subarray
    sum_curr_array = sum(arr[:k])
    result = [sum_curr_array]
    for i in range(1, len(arr)-k+1):
        sum_curr_array -= arr[i-1]
        sum_curr_array += arr[i+k-1]

        result.append(sum_curr_array)

        
    return result


def dynamic_sliding_window(arr: list[int], x: int) -> int:
    # input arr: List[int] -- given array
    # target sum of the desired subarray
    min_length = float('inf')

    start, end, cur_sum = 0, 0, 0

    while end < len(arr):
        cur_sum += arr[end]
        end += 1
        while start < end and cur_sum >= x:
            cur_sum -= arr[start]
            start += 1
            min_length = min(min_length, end-start+1)
    
    return start, end, cur_sum, min_length



if __name__ == '__main__':
    arr = [1,2,3,4,5,6,7]
    k = 3
    print(fixed_sliding_window(arr, k))
    _,_,_,min_length = dynamic_sliding_window(arr, 10)
    print(min_length)