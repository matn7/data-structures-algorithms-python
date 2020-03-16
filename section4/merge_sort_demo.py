def merge_sorted(arr1,arr2):
    # print("Merge function called with lists below:")
    # print(f"left: {arr1} and right: {arr2}")
    sorted_arr = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        # print(f"Left list index i is {i} and has value: {arr1[i]}")
        # print(f"Right list index j is {j} and has value: {arr2[j]}")
        if arr1[i] < arr2[j]:
            sorted_arr.append(arr1[i])
            i += 1
        else:
            sorted_arr.append(arr2[j])
            j += 1
        # print(sorted_arr)
    
    while i < len(arr1):
        sorted_arr.append(arr1[i])
        i += 1

    while j < len(arr2):
        sorted_arr.append(arr2[j])
        j += 1

    return sorted_arr

def divide_arr(arr):
    if len(arr) < 2:
        # print(f"Base condition reached with {arr[:]}")
        return arr[:]
    else:
        middle = len(arr) // 2
        l1 = divide_arr(arr[:middle])
        l2 = divide_arr(arr[middle:])
        return merge_sorted(l1, l2)    

# Program Execution
l = [8, 6, 2, 5]
print(divide_arr(l))

# Steps
# 1. Compare first element in each list and append smaller element
# 2. Using a indices and an iterator perform same comparision for all elements in both list
# 3. Move marker up by 1 position after smaller number is found
# 4. Copy remaining list once comparisions are completed and there are items still remaining o the lists