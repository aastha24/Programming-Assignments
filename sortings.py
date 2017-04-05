import random
from bubblesort import bubble_sort
from insertionsort import insertion_sort

storage = [random.randint(-30,100) for number in range(10)]
print("Before Sort: " , storage)

storage_sorted_b = bubble_sort(storage)
print("After Sort by Bubble Sort: ", storage_sorted_b )

storage_sorted_i = insertion_sort(storage)
print("After Sort by Insertion Sort: ", storage_sorted_i )
