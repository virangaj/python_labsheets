from asyncio import constants


def getFile():
    file = open('words_file.txt','r')
    content = file.read()
    content_1 = content.replace(',',' ')
    word_list_1 = content.split()
  
    print(len(word_list_1) + len(word_list_2))


getFile() 