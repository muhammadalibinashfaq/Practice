word = input("Enter a letter: ")

vowels = ['a', 'e', 'i', 'o', 'u']

if word.lower() in vowels:
    print("This is a vowel")
else:
    print("This is not a vowel")