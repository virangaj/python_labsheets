def getFile():
    file = open('words_file.txt','r')
    content = file.read()

    word_list_1 = content.split()
    word_list_2 = content.split('-')
    word_list_3 = content.split(',')
    print(len(word_list_1) + len(word_list_2) + len(word_list_3))


getFile() 