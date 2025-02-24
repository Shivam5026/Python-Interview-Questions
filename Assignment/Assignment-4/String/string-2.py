# Reverse Words in a Given String
def reverse_words(sentence):
    words = sentence.split()
    return " ".join(words[::-1])

# Example
s = input("Enter a sentence: ")
print("Reversed words:", reverse_words(s))