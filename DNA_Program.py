
#Alignment of DNA
print("Hello and welcome to DNA sequence alignment program!")

firstsequence= input("Please enter DNA sequence (using uppercase letters A, T, C, G and an indel symbol): ")
secondsequence= input("Please enter DNA sequence (using uppercase letters A, T, C, G and an indel symbol): ")
print (f"You entered:\n{firstsequence}\n{secondsequence}")

def is_invalid_base(var):
  return var not in ('A', 'T', 'G', '-')

while True:
    menu = input ("Select one of the following commands:\n'u' to update sequences\n's' to score the alignment\n'q' to quit\n")

    if menu == 'q':
        break

    elif menu == 's':
        if firstsequence == '' or secondsequence == '':
            print ("Invalid DNA sequences entered, please re-enter sequences")
            continue
        for y in secondsequence:
            if is_invalid_base(y):
                print("Invalid DNA sequences entered, please re-enter sequences")
            continue
        score= sum ((x == y for x, y in zip (firstsequence, secondsequence)))
        print (f"{score} matches found between {firstsequence} and {secondsequence}")

    elif menu == 'u':
        firstsequence = input ("Please enter DNA sequence (using uppercase letters A, T, C, G and an indel symbol): ")
        secondsequence = input ("Please enter DNA sequence (using uppercase letters A, T, C, G and an indel symbol): ")
        print (f"You entered:\n {firstsequence}\n{secondsequence}")

    else:
        continue

print ("Thank you! Goodbye!")

#Validation
def is_valid_dna(sequence):
  valid_bases = {'A', 'T', 'C', 'G', '-'}
  return len(sequence) > 0 and all(base in valid_bases for base in sequence)

sequence = input("Please enter DNA sequence (using uppercase letters A, T, C, G and an indel symbol): ")

if is_valid_dna(sequence):
  print(f"{sequence} is a valid DNA sequence")
else:
  print(f"{sequence} is not a valid DNA sequence")

#Score
def calculate_alignment_score(sequence1, sequence2):
  if len(sequence1) == 0 or len(sequence2) == 0:
      return 0

  if len(sequence1) != len(sequence2):
      return 0

  alignment_score = sum(a == b for a, b in zip(sequence1, sequence2))
  return alignment_score

sequence1 = input("Please enter DNA sequence (using uppercase letters A, T, C, G and an indel symbol): ")
sequence2 = input("Please enter DNA sequence (using uppercase letters A, T, C, G and an indel symbol): ")

score = calculate_alignment_score(sequence1, sequence2)
print(f"{score} match{'es' if score != 1 else ''} found between {sequence1} and {sequence2}")

#Menu
def display_menu():
  print("Select one of the following commands:")
  print("'u' to update sequences")
  print("'s' to score the alignment")
  print("'q' to quit")

def main():
  print("Hello and welcome to DNA sequence alignment program!")

main()

display_menu()

user_input = input()

while user_input != 'q':
# No message printed for anything but 'q'
  display_menu()
  user_input = input()
  if user_input == 'q':
      break

if user_input == 'q':
  print("Thank you! Goodbye!")