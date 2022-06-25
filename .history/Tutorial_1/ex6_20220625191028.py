marks = []


# def sortList(list):


def getMarks(marks):
    i = 1
    file = open('marks_file.txt', 'r')
    
    
    while i <= 10:
        
        mark = file.readline()[:2]
        marks.append(mark)
        i += 1
    file.close()
    print(marks)


getMarks(marks)
