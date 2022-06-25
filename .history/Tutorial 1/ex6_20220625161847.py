marks = []


def sortList(list):


def getMarks(marks):
    i = 1
    while i <= 10:
        mark = input('Enter marks for studnet {} : '.format(i))
        marks.append(mark)
        i += 1

    print(marks)


getMarks(marks)
