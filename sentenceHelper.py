def buildSentenceObj(sentence):

    sentenceArray = sentence.split(" ")
    sentence_obj = []
    count = 0

    for word in sentenceArray:
        sentence_obj.append({
            "word": word,
            "orig_index": count
        })

        count = count + 1

    return sentence_obj

#bubble sort to sort sentence from shortest to longest
def sortSentence(sentence_arr):
    n = len(sentence_arr) 
  
    # Traverse through all array elements 
    for i in range(n-1): 
    # range(n) also work but outer loop will repeat one time more than needed. 
  
        # Last i elements are already in place 
        for j in range(0, n-i-1): 
  
            # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element 
            j_len = len(sentence_arr[j]["word"])
            j_next_len = len(sentence_arr[j+1]["word"])
            if j_len > j_next_len : 
                sentence_arr[j], sentence_arr[j+1] = sentence_arr[j+1], sentence_arr[j]
    
    return sentence_arr