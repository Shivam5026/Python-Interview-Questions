def print_even_length_words(sentence):
    words = sentence.split()
    even_words = [word for word in words if len(word) % 2 == 0]
    print("Even length words:", even_words)
    
s = input("Enter a sentence: ")
print_even_length_words(s)