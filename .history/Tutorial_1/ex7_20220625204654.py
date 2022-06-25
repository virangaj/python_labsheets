def getFile():
    file = open('words_file.txt','r')
    content = file.read()

    print(content)


getFile() 