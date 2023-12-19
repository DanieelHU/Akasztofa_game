import random

def randomWordGen() -> str:
    wordsList = ["alma", "körte", "barack", "szilva", "narancs", "eper", "citrom", "mandula", "datolya", "eperfa"]
    return random.choice(wordsList)

wordtemplate = list()
word = randomWordGen()
#print(word)
for i in range(len(word)):
    wordtemplate.append("_")
    
    
print()
print("  ".join(wordtemplate))

print("\nTaláld ki a gondolt szót! 10 lehetőséged van.")
tip = input("Az ön betűje: ")

if tip not in word:
    print("Hát ez bizony rossz ötlet volt, 2 percen belül kopog a TEK.")
else:
    for i in range(len(word)):
        if word[i] == tip:
            wordtemplate[i] = tip
            
print("  ".join(wordtemplate)
      