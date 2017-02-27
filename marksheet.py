#Given the names and grades for each student in a Physics class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
#Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.
#Input Format

#The first line contains an integer,N , the number of students. 
#The 2N subsequent lines describe each student over N lines; the first line contains a student's name, and the second line contains their grade.


if __name__ == '__main__':
    marks_name = []
    for _ in range(int(input())):
        marks_name.append([input(),float(input())])
    answer = sorted(list(set([marks for name,marks in marks_name])))[1]
    s = '\n'
    print (s.join([name for name,mark in sorted(marks_name) if mark==answer]))