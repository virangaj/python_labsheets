marks = []

# sort the list
def sortList(list):
   
    for i in range(len(list)):
        for j in range(i, len(list)):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]                                                                      
    return list

# get total mean median mode
def generate_them(list):
    total = 0
    for i in range(len(list)):
        total += list[i]
    print("Total is : {}".format(total))
    print("Mean is : {}".format(total/len(list)))



# read the data
def getMarks(marks):
    i = 1
    file = open('marks_file.txt', 'r')
    while i <= 10:
        marks.append(int(file.readline()[:2]))
        i += 1
    file.close()
    print("List : {}".format(marks))
    sorted_list = sortList(marks)
    print("Sorted list : {}".format(sorted_list))  
    generate_them(sorted_list)  

getMarks(marks)

