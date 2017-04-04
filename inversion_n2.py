#Developer: Aastha Anand
import time
import sys

def main():
    start_time = time.time()
    a = [line.strip() for line in open("hw1test.txt", 'r')]
    no_of_inv = 0
    for i in range(0,len(a)):
        for j in range(i+1,len(a)):
            if  a[i] >(2*a[j]):
                no_of_inv += 1
    print(no_of_inv)
    end_time = time.time()
    print("Time taken for execution of O(n^2)-Naive program  = ", end_time-start_time)

if __name__=="__main__":
    main()  