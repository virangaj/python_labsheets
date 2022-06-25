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
    
    # total
    total = 0
    for i in range(len(list)):
        total += list[i]   
    print("Total is : {}".format(total))
    
    # Mean
    print("Mean is : {}".format(total/len(list)))
    
    # Median
    middle = int(len(list)/2)
    median = (list[middle] + list[middle-1])/2
    print("Median is : {} ".format(median))

    count = 0
    max_count = 0
    mode = 0
    for i in range(len(list)):
        for j in range(len(list)):
            if list[i] == list[j]:
                count += 1
        if count > max_count:
            max_count = count
            mode  = list[i]
    
    print("Mode is : {} ".format(mode))



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

