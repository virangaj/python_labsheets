from asyncio import constants


def getFile():
    file = open('words_file.txt','r')
    content = file.read()
    content_1 = content.replace(',',' ')
    content_1 = content_1.replace('-', ' ')
    word_list = content_1.split()
  
    print(len(word_list))


getFile() 