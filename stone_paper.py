import random

def get_choice():
  player_choice = input("Enter a choice(rock,paper,scissor)")
  options = ["rock", "paper","scissors"]
  system_choice = random.choice(options)
  choices = { "player":player_choice, "system":system_choice}
  return choices

def check_win(player, system):
  print(f"You chose {player}, computer chose {system}")
  if player == system:
    return "It is a tie!"
    
  elif player=='rock':
    if system =='scissors':
      return "Rock smashes scissor! You win!!!"
    else:
      return "Paper covers rock! System wins!!!"
      
  elif player=='scissor':
    if system =='rock':
      return "Rock smashes scissor! System wins!!!"
    else:
      return "Scissors cuts paper! You win!!!"

  elif player == 'paper':
    if system == 'scissor':
      return "Scissors cuts paper! Computer win!!!"
    else:
      return "Paper covers rock! You wins!!!"
     
choices = get_choice()
  
result = check_win(choices["player"], choices["system"])
print(result)
