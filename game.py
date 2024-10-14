import random
user= str(input("Please Enter your choice (Rock/Paper/Scisoor)"))
ai= random.choice("Rock"or"Paper"or"Scesoor")
print("You: ",user, "ai: ",ai)
if ai=="Rock" and user=="Paper":
    print("User win")
elif ai=="Paper" and user=="Scisoor":
    print("User win")
elif ai=="Scisoor" and user=="Rock":
    print("User win")
elif ai=="Paper" and user=="Paper":
    print("Tie")
elif ai=="Rock" and user=="Rock":
    print("Tie")
elif ai=="Scisoor" and user=="Scisoor":
    print("Tie")
else:
    print("Ai win")