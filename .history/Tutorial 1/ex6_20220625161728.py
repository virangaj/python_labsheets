from inspect import getmembers


def getMarks():
    i = 1
    marks = []
    while i <= 10:
        mark = input('Enter marks for studnet {} : '.format(i))
        marks.append(mark)
        i += 1

    print(marks)


getMarks()
