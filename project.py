import random
while True:
    my_answer=input("choose:rock,paper,scissors")
    my_answer=my_answer.lower()
    if my_answer=="quit":
        break
    if my_answer !="rock" and my_answer!="paper" and my_answer!="scissors":
        print("please choose a correct answer")
        continue
    computer_answer=random.choice(["rock","paper","scissors"])
    if my_answer==computer_answer:
        print("you tied")
        continue
    elif my_answer=="paper" and computer_answer=="rock":
        print("you won!")
    elif my_answer=="rock" and computer_answer=="scissors":
        print("you win!")
    elif my_answer=="scissors" and computer_answer=="paper":
        print("you win!")
        break
    else:
        print("you lost")





