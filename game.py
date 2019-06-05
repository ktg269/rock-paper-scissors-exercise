# game.py

print("Rock, Paper, Scissors, Shoot!")

# CAPTURE INPUTS


user_choice = input("Please choose one of the following options: 'rock', 'paper', or 'scissors' (without the quotes):")
print("---------")
print("USER CHOICE:",user_choice)

# VALIDATE INPUTS




if user_choice not in["rock", "Paper", "scissors"]:
    print("INVALID SELECTION. PLEASE TRY IT AGAIN")
    exit()


# GENERATE COMPUTER SELECTION

print("GENERATING...")

# DETERMINE THE WINNER

# DISPLAY FINAL OUTPUTS/OUTCOMES