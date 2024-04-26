sentence=input("Enter your sentence: ")
print("USER ENTERED:\n",sentence)

word=input("Enter your word to search: ")

if word in sentence:
    print(f"The word {word} Exists in the sentence")
else:
    print(f"{word} NOT EXISTS!")