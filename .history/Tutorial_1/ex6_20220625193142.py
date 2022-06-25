marks = []


def sortList(list):
   
    for i,n in enumerate(list):
        for j,m in enumerate(list):
            if i > j:
                a = list[i]
                list[i] = list[j]
                list[j] = a
            else:
                continue                                                                        
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
