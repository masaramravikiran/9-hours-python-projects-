print("welcome to my computer quiz!")

playing = input("Do you want to play? ")
if playing.lower() != "yes":
    quit()

print("Okay! Lets play😊😊")
score = 0

answer = input("what does CPU stands for? ")
if answer == "Central processing unit":
  print("Correct!👍👍👍👍👍")
  score += 1
else:
  print("Incorrect!😕😕😕😕😕")
  
  answer = input("what does EE stands for? ")
if answer == "Energy engine":
  print("Correct!👍👍👍👍👍")
  score += 1
else:
  print("Incorrect!😕😕😕😕😕")

  answer = input("what does IP stands for? ")
if answer == "Internet protocol":
  print("Correct!👍👍👍👍👍")
  score += 1
else:
  print("Incorrect!😕😕😕😕😕")

print(("You got " +str(score/3) *100)+ "questions correct!")


  
