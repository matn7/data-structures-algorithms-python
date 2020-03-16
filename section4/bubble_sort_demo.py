def bubble_sort(arr):
    swap_happened = True
    while swap_happened:
        print('bubble sort happened: ' + str(arr))
        swap_happened = False
        for num in range(len(arr) - 1):
            if arr[num] > arr[num + 1]:
                swap_happened = True
                arr[num], arr[num + 1] = arr[num + 1], arr[num]


l = [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]

bubble_sort(l)

# can be optimized after first iteration 10 steps
# after second 9
# after third 8

# l = [6,8,1,4,10,7,8,9,3,2,5] # original 
# l = [10,9,8,7,6,5,4,3,2,1] # worst case
# l = [1,2,3,4,5,6,7,8,9,10] # best case