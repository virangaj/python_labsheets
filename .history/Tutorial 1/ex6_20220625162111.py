marks = []


# def sortList(list):


def getMarks(marks):
    i = 1
    file = open('marks_file', 'r+')
    while i <= 10:
        # mark = input('Enter marks for studnet {} : '.format(i))
        mark = file.readline()
        marks.append(mark)
        i += 1

    print(marks)


getMarks(marks)