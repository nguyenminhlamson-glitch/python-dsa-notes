def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        items_smaller = []
        items_bigger = []
        for item in arr[1:]:
            if item < pivot:
                items_smaller.append(item)
            else:
                items_bigger.append(item)
        return quick_sort(items_smaller) + [pivot] + quick_sort(items_bigger)


print(quick_sort([1, 2, 8, 9, 4, 5]))
