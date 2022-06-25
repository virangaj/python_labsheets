marks = []


def sortList(list):
    swapped = False
    for i,n in enumerate(list):
        for j in enumerate(list):
            if i >= j:
                swapped = True
                if swapped:
                    a = i
                    i = j
                    j = a

            else:
                swapped = False                                                                              

    return list


    return list

def getMarks(marks):
    i = 1
    file = open('marks_file.txt', 'r')
    while i <= 10:
        marks.append(int(file.readline()[:2]))
        i += 1
    file.close()
    print(marks)
    sorted_list = sortList(marks)
    print(sorted_list)    

getMarks(marks)
