marks = []


def sortList(list):

    for i in list:
        for j in list:
            if(list[i] > list[j]):
                a = list[i]



    return list

def getMarks(marks):
    i = 1
    file = open('marks_file.txt', 'r')
    while i <= 10:
        marks.append(file.readline()[:2])
        i += 1
    file.close()
    print(marks)
    sorted_list = sortList(marks)
    print(sorted_list)    

getMarks(marks)
