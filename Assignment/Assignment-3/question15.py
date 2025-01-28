# 15.Find the position of the first occurrence of the word 'because' in the following sentence: 'You 
# cannot end a sentence with because because because is a conjunction'


sentence = "You cannot end a sentence with because because because is a conjunction"

word_to_find = "because"

first_occurrence = sentence.find(word_to_find)

if first_occurrence != -1:
    print(f"The word '{word_to_find}' first occurs at position: {first_occurrence}")
else:
    print(f"The word '{word_to_find}' was not found in the sentence.")
