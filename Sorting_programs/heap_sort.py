def heapsort(arr):  # arr - lista
    n = len(arr)
    build_max_heap(arr, n)  # budujemy cały kopiec
    for i in range(n-1, 0, -1):  # zaczynamy sortowanie
        arr[i], arr[0] = arr[0], arr[i]  # zamieniamy max element z ostatnim w liście
        max_heapify(arr, 0, i)  # kopcujemy resztę pomniejszoną o jeden element
    print(arr)


def build_max_heap(arr, n):  # arr - lista, n - len(arr)
    for i in range(n//2, -1, -1):
        max_heapify(arr, i, n)


def max_heapify(arr, i, n):  # arr - lista; i - index node gdzie jesteśmy, n - len(arr)
    largest = i
    left = 2*i+1
    right = 2*i+2
    if left < n and arr[left] > arr[largest]:  # porównujemy lewą z rodzicem
        largest = left
    if right < n and arr[right] > arr[largest]:  # porównujemy prawą z rodzicem/parentem
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, largest, n)


list1 = [1,3,1,2,7,9,1,6,1,0,4,2]
list2 = [15,3,99,1,25,7,9,9,1,100,6,1,0,12,4,2,9,0,87,122,54]
list3 = [0,12,4,2,9,0,87,122,54,1,2,11,55,99]

print("Lista 1.:")
heapsort(list1)
print("Lista 2.:")
heapsort(list2)
print("Lista 3.:")
heapsort(list3)