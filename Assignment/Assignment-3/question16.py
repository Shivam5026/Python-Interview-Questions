# 16.Slice out the phrase 'because because because' in the following sentence: 'You cannot end a 
# sentence with because because because is a conjunction'

# Sentence
sentence = "You cannot end a sentence with because because because is a conjunction"

phrase_to_remove = "because because because"

sliced_sentence = sentence.replace(phrase_to_remove, "")

print("Original Sentence:")
print(sentence)
print("\nSentence after removing the phrase:")
print(sliced_sentence.strip())
