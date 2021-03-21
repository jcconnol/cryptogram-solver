US_dict_file = open('en_US.dic', 'r')
Lines = US_dict_file.readlines()

en_dictionary = {}
en_array = []

count = 0

for line in Lines:
    count = count + 1
    line = line.split("/", 1)[0].replace('\n','')
    en_dictionary[line] = 1
    en_array.append(line.strip() + '\n')

#print(en_array)

with open("en_US.txt", 'r+') as f:
    f.writelines(en_array)
    f.truncate()

print(count)

print("whaasud" in en_dictionary)

print("what" in en_dictionary)

cryptogram_file = open('cryptograms/test.txt', 'r')
crypt_Lines = cryptogram_file.readlines()

#for line in crypt_Lines:
#    print(line)
