def getFile():
    file = open('words_file.txt','r')
    content = file.read()

    word_list = content.split()
    print(word_list)


getFile() 