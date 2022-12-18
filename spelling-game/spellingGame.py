from textblob import Word
import random

#Quiddler
#the first round has a three-card hand,the dealer deals out three cards to each player.
# the second round has a four-card hand,
# and so on until the game ends with a ten-card hand.

class Quiddler:
    def __init__(self):
        self.POINTSCON = [8,8,5,6,6,7,2,13,8,3,5,5,6,15,5,3,3,11,10,12,4,14]
        self.LETTERSCON = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]

        self.POINTSVOWEL = [2,2,2,2,4]
        self.LETTERSVOWEL = ["a","e","i","o","u"]

        self.indexesCon = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        self.indexesVowels = [0,1,2,3,4]

        self.types = ["consonant", "vowel", "consonant"]
        self.round = 1
        self.lettersHand = []
        self.totalPoints = 1

    def randNumCon(self):
        random.shuffle(self.indexesCon)
        random.shuffle(self.indexesVowels)
        random.shuffle(self.types)

        return self.indexesCon[0]

    def randNumVowel(self):
        random.shuffle(self.indexesVowels)
        random.shuffle(self.indexesCon)
        random.shuffle(self.types)

        return self.indexesVowels[0]

    def newCard(self):
        random.shuffle(self.types)

        if (self.types[0] == "consonant"):
            idx = self.randNumCon()
            card = self.LETTERSCON[idx]
            self.lettersHand.append(card)

        else:
            idx = self.randNumVowel()
            card = self.LETTERSVOWEL[idx]
            self.lettersHand.append(card)

    def firstHand(self):
        idx = self.randNumCon()
        card = self.LETTERSCON[idx]
        self.lettersHand.append(card)

        idx = self.randNumVowel()
        card = self.LETTERSVOWEL[idx]
        self.lettersHand.append(card)
            
    def playing(self):

        while self.round < 11:
            self.newCard()
            print(f"\nRound: {self.round}. Your letters are:")
            print(self.lettersHand)

            self.turn()

            if len(self.lettersHand) == 0:
                print("You played all your cards for an automatic 50 point bonus!")
                self.totalPoints+=50
                self.round = 12
            else: 
                self.round+=1
            
        if self.round >= 11:
            print(f"\nGreat job! You ended with {self.totalPoints} points.")   

    def turn(self):
        print("\nWould you like to play a word?")

        response = input("""y/n or q to quit. Your choice: """)

        if (response != "y" and response != "n" and response != "q"):
            print("\nPlease choose y/n or q:")
            self.turn()

        if response == "y":
            word = Word(input("\nWhat is your word? "))
            if word == "" or len(word) == 1:
                print("Full word not entered.")
                self.turn()
            else:
                obj = Word(word).spellcheck()
                    
            if (obj[0][1] < 1):
                print("\nPlease play a correct word.")
                self.turn()
                    
            else:
                for letter in word:
                    if letter in self.LETTERSVOWEL:
                        idx = self.LETTERSVOWEL.index(letter)
                        self.totalPoints += self.POINTSVOWEL[idx]
                        idx = self.lettersHand.index(letter)
                        del self.lettersHand[idx]

                    else:
                        idx = self.LETTERSCON.index(letter)
                        self.totalPoints += self.POINTSCON[idx]
                        idx = self.lettersHand.index(letter)
                        del self.lettersHand[idx]

                print("\nGreat word!")
                print(f"You now have: {self.totalPoints} points.")

        if response == "q":
            self.round = 11

newHand = Quiddler()

print("Welcome Player!")
print("You have 10 rounds\nto make as many words as you can.")
print("Words must be two letters in length.")
print("Good luck!")

newHand.firstHand()
newHand.playing()