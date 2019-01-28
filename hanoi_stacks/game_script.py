#!/usr/bin/python3
from stack import Stack
'''
Towers of Hanoi!!
-----------------
There are three stacks. The game begins with all of the disks on the
left stack. The disks must be moved one at a time until the disks are all on
the right most stack. A disk may only be stacked on top of a disk of larger
size.
'''
print("\nLet's play Towers of Hanoi!!")

#Create the Stacks
stacks = []
left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")
stacks.extend([left_stack, middle_stack, right_stack])
#Set up the Game
# Initialize the disks.
num_disks = int(input("\nHow many disks do you want to play with?\n"))
# Validate that the user chose 3 or more disks.
while num_disks < 3:
  num_disks = int(input("Enter a number greater than or equal to 3\n"))
# Push the disks to the left stack for the initial game state.
for i in range(num_disks, 0, -1):
  left_stack.push(i)
# Calculate the fewest moves to win and print to the screen.
num_optimal_moves = (2**num_disks) - 1
print("\nThe fastest you can solve this game is in {moves} moves".format(moves=num_optimal_moves))
#Get User Input
def get_input():
  '''
  Generates a list of choices corresponding to a stack.
  Takes input of a letter (L, R, M) and converts that
  to stack in the 'stacks' list that correspondes to
  the appropriate letter. Then returns that stack.
  '''
  # Generate list of choices.
  choices = [stack.get_name()[0] for stack in stacks]
  while True:
    for i in range(len(stacks)):
      # Print out the choices and the corresponding stacks.
      name = stacks[i].get_name()
      letter = choices[i]
      print("Enter {letter} for {name}".format(
      letter=letter, name=name))
    user_input = input("").upper()
    # Validate the choice and return the corresponding stack.
    if user_input in choices:
      for i in range(len(stacks)):
        if user_input == choices[i]:
          return stacks[i]
#Play the Game
num_user_moves = 0
# The game will continue until the right_stack contains all of the disks (end game state).
while right_stack.get_size() != num_disks:
  # Print out the current game state.
  print("\n\n\n...Current Stacks...")
  for stack in stacks:
    stack.print_items()
  while True:
    # Ask the user which to stack to move and disk from and then the stack to move the disk to.
    print("\nWhich stack do you want to move from?\n")
    from_stack = get_input()
    print("\nWhich stack do you want to move to?\n")
    to_stack = get_input()
    # Check if the from stack is empty.
    if from_stack.is_empty():
      print("\n\nInvalid Move. Try Again.")
    # Case 1: The to stack is empty or the from stack disk
    # is smaller than the top disk of the to stack meaning
    # that we are allowed to push that disk onto the to stack.
    elif to_stack.is_empty() or from_stack.peek() < to_stack.peek():
      # Pop the disk from the from stack.
      disk = from_stack.pop()
      # Push it to the to_stack.
      to_stack.push(disk)
      # Increment the number of user moves.
      num_user_moves += 1
      break
    # Case 2: The user tries to move a larger disk onto a smaller disk.
    else:
      print("\n\nInvalid Move. Try Again")

# After the game has ended.
print("\n\nYou completed the game in {user_moves} and the optimal"
     " number of moves is {optimal_moves}".format(
         user_moves=num_user_moves, optimal_moves=num_optimal_moves ))
