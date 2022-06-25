marks = []


def sortList(list):
    return list

def getMarks(marks):
    i = 1
    file = open('marks_file.txt', 'r')
    while i <= 10:
        marks.append(file.readline()[:2])
        i += 1
    file.close()
    print(marks)
    sortList(marks)


getMarks(marks)
