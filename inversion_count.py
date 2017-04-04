#Developer: Aastha Anand
import time
import sys
import math

def inv(array):
    if len(array) < 2:
        return array, 0
    mid = int(math.ceil(len(array) / 2))
    a_array = array[:mid]
    b_array = array[mid:]
    l_a,inv_a = inv(a_array)
    r_b,inv_b = inv(b_array)
    merged, inv_count = merge_and_count(l_a,r_b)
    inv_count = inv_count + inv_a + inv_b
    return merged, inv_count

def merge_and_count(left,right):
    answer = list()
    i,j = 0,0
    inv_count = 0
    length = len(left)
    while i < length and j < len(right):
        if (2 * right[j]) < left[i]:
            j += 1
            inv_count += (length-i)
        else:
            i += 1
    i,j = 0,0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            answer.append(left[i])
            i += 1
        elif right[j] < left[i]:
            answer.append(right[j])
            j += 1
    answer += left[i:]
    answer += right[j:]
    return answer,inv_count

def main():
    start_time = time.time()
    a = [line.strip() for line in open("hw1test.txt", 'r')]
    merge_array = []
    merge_array,inversions = inv(a)
    print(inversions)
    end_time = time.time()
    print("Time taken for execution of O(nlogn) program= ", end_time-start_time)

if __name__=="__main__":
    main()    