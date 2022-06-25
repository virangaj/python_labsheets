from codecs import utf_16_decode


file = open('sample_file.txt', utf_16_decode)
file.read()
file.close()
