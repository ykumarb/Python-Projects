def average():
#     sum = 0
#     len = 0
#     for i in range(0,10):
#         sum += i
#         len +=1
#     # print("Sum:",sum,"Len:",len)
#     return(sum/len)

# print("Average is:",average())
# print("Approximated average:",int(average()))

# # How to read from a file
# file = open('file.txt', 'r')
# read_lines = file.readlines()
# file.close()
# new = []
# for line in read_lines:
#     if line[-1] == '\n': # Other ways to do is strip simply with no arguments to remove \n
#         new.append(line[:-1])
#     else:
#         new.append(line)

# print(new)

# # Writing to a text file
# file = open('file.txt', 'w')
# file.write('Python is here!!!\n')
# file.write('Yes it is !!')
# file.close()