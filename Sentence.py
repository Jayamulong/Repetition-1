#Create a program that ask for a sentence as input.
#Display the number of words, vowels and consonants in the input 

#Ask for a word sentence from the user.
Sentence = input("Insert your sentence: ")

#Count the space from the sentence to know the words.
def space_Count(Sentence):
    count = 1
    for i in range(0, len(Sentence)):
        if Sentence[i] == " ":
            count += 1
    return count

print(f"Words:",space_Count(Sentence))

#Count the vowels from the sentence.
#Count the consonants from the sentence.
lowercase = Sentence.lower()
vowels = 0
consonants = 0

for i in range(0,len(lowercase)):
    if lowercase[i] in ('a',"e","i","o","u"):
        vowels += 1
    elif lowercase[i] in ('b',"c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"):
        consonants += 1

#Display the output
print(f"Vowels: {vowels}")
print(f"Consonants: {consonants}")