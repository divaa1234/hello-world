word = str(raw_input("Enter a word: "));
count = 0
for vowel in word:
    if vowel == "a" or vowel == "e" or vowel == "i" or vowel == "o" or vowel == "u":
        count=count+1
print("Number of vowels: " + str(count))