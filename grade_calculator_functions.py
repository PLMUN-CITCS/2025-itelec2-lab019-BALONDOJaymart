# Ask the person for their test score
their_score = input("Enter your score: ")

# Turn what they typed into a number
score_as_number = int(their_score)

# Figure out the letter grade
if score_as_number >= 90:
  letter_grade = "A"
elif score_as_number >= 80:
  letter_grade = "B"
elif score_as_number >= 70:
  letter_grade = "C"
elif score_as_number >= 60:
  letter_grade = "D"
else:
  letter_grade = "F"

# Tell them their grade
print("Your Grade is: ", letter_grade)