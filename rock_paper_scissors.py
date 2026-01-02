import random
item_list = ["Rock","Paper","Scissors"]

user_choice = input( "Enter your moove = Rock,Paper,Scissor= ")
comp_choice = random.choice(item_list)

print(f"User choice ={user_choice},Computer choice ={comp_choice}")

if user_choice == comp_choice:
    print("Both chooses same: = Match Tie")

elif user_choice == "Rock":
    if comp_choice == "Paper":
        print ("Paper covers Rock = Computer Win")
    else:
        print ("Rock smashes Scissor = you win")

elif user_choice =="Paper":
    if comp_choice == "Scissor":
        print ("Scissor cuts paper,Win")
    else:
        print("paper covers rock , you win")   

elif user_choice == "Scissor":
    if comp_choice == "paper":
        print("Scissor cuts paper, you win")
    else: 
        print ("Rock smashes scissor, Computer win") 
else:
    print("Invalid input.Please choose Rock,Paper,Scissor.")

play_again = input("Do you want to play again?(yes/no):")
if play_again.lower()!= "yes":
    print("THANKS FOR PLAYING!")   
          