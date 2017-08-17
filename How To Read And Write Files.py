file_open = open('sampe.txt', 'w')
file_open.write('Writing ome shit in this fucking text file\n')
file_open.write('I fuck children\n')
file_open.close()

file_read = open('sampe.txt', 'r')
text = file_read.read()
print(text)
file_read.close()