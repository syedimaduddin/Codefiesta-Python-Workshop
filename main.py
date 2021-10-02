# This code is written by @syedimaduddin
# You can follow me on LinkedIn: https://www.linkedin.com/in/syed-imaduddin-227169205/

import random

round_no = 1

my_score = 0
comp_score = 0
tie = 0

while round_no<=5 :
  print()
  print("ROUND: ", round_no)

  print("1 Rock")
  print("2 Paper")
  print("3 Scissor")

  print()

  my_choice = int(input("Enter your choice between 1-3: "))

  c_choice = random.randint(1,3)

  print("Computer Choose: ", c_choice)

  if my_choice == c_choice :
    tie = tie+1
    print(tie)
  
  elif my_choice==1 and c_choice==2:
    comp_score += 1
    print("Computer Wins!")

  elif my_choice==2 and c_choice==1:
    my_score+=1
    print("I Wins!")

  elif my_choice==2 and c_choice==3:
    comp_score+=1
    print("Computer Wins!")
  
  elif my_choice==3 and c_choice==1:
    comp_score+=1
    print("Computer Wins!")

  elif my_choice==3 and c_choice==2:
    my_score+=1
    print("I Wins!")

  print()
  print("Your Score: ", my_score)
  print("Computer Score: ", comp_score)
  print("Ties: ", tie)
  print()

  round_no+=1


print()
if my_score>comp_score:
  print("Congratulations! You won")
elif comp_score>my_score:
  print("Computer Won")
else:
  print("There's a tie")


  import random

round_no=1

my_score= 0
comp_score = 0
tie = 0

while round_no<=5:
  print()
  print("ROUND : ",round_no)

  print("1 Rock")
  print("2 Paper")
  print("3 Scissor")
  print()

  my_choice = int(input("Enter your choice between 1-3: "))

  c_choice = random.randint(1,3)
  print("Computer Chose: ",c_choice)

  if my_choice==c_choice:
    tie = tie+1
    print("Tie")

  elif my_choice==1 and c_choice==2:
    comp_score+=1
    print("Computer Wins!")

  elif my_choice==1 and c_choice==3:
    my_score+=1
    print("I Win!")

  elif my_choice==2 and c_choice==1:
    my_score+=1
    print("I Win!")
  
  elif my_choice==2 and c_choice==3:
    comp_score+=1
    print("Computer Wins!")

  elif my_choice==3 and c_choice==1:
    comp_score+=1
    print("Computer Wins!")

  elif my_choice==3 and c_choice==2:
    my_score+=1
    print("I Win!")

  print()
  print("Your Score: ",my_score)
  print("Computer's Score: ",comp_score)
  print("Ties: ", tie)
  print()

  round_no+=1

print()
if my_score>comp_score:
  print("Congratulations! You won")
elif comp_score>my_score:
  print("Computer Won")
else:
  print("There's a tie")
