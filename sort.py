# 1
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        print(i)
        swapped = False
        for j in range(0,n-i-1):
            print(arr,j)
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not swapped:
            break
    return arr

"""result = bubble_sort([3,2,1])"""
"""print(result)"""

# 2 a) - urvarlssortering

def urval_sortering(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[min_index],arr[i] = arr[i], arr[min_index]

    return arr

#result = urval_sortering([3,2,1])
#print(result)

# 2 b) - combsort

def comb_sort(arr):
    def get_next_gap(gap):
        gap = (gap * 10) // 13
        
        if gap < 1:
            return 1
        return gap

    n = len(arr)
    gap = n
    swapped = True

    while gap != 1 or swapped == True:
        gap = get_next_gap(gap)
        swapped = False

        for i in range(0,n-gap):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                swapped = True

    return arr

#result = comb_sort([4,3,2,1])
#print(result)

# 3 

def name_sort(arr):
    sorterade_namn = sorted(arr,key = lambda namn: namn.lower()[0])
    return sorterade_namn

#resultat = name_sort(["Åberg","Öberg","Viklund","andersson","Anderberg","Ärleskog","Sträng","Stråby","viklander"])
#print(resultat)


# 4 instickssortering

def instickssortering(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i - 1

        while j <= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j+1] = key

    return arr


# 5 quicksort

def quicksort(arr):
    if len(arr) <= 1:
        return arr

    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

result = quicksort([9,2,4,1,51,2,4,8,3,1])
print(result)


