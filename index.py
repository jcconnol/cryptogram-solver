import sentenceHelper

'''
order words by shortest to longest, find possible letter matches to words in shortest to longest
because that will limit possibilities
'''

#setup A marker for all the possibilites, 0 unk, 1 no, 2 yes
alphabet = ['A', 'B', 'C', 'D','E', 'F', 'G', 'H','I', 'J', 'K', 'L','M', 'N', 'O', 'P','Q', 'R', 'S', 'T','U', 'V', 'W', 'X', 'Y', 'Z']
letter_marker = {}

for i in range(len(alphabet)):
    for j in range(len(alphabet)-1, -1, -1):
        if alphabet[i] != alphabet[j]:
            letter_pair = alphabet[i] + alphabet[j]
            letter_marker[letter_pair] = 0

dict_file = open('en_US.txt', 'r')
Lines = dict_file.readlines()


cryptogram_file = open('cryptograms/short_test.txt', 'r')
crypt_Lines = cryptogram_file.readlines()

for line in crypt_Lines:

    sentence_obj = sentenceHelper.buildSentenceObj(line)
    sorted_sent_obj = sentenceHelper.sortSentence(sentence_obj)

    