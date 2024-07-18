with open("story.txt", "r") as f:
  story = f.read()
  
word = set()
start_of_word = -1

target_start = "<"
target_end = ">"

for i, char in enumerate(story):
    if char == target_start:
      start_of_word = i
    
    if char == target_end and start_of_word != -1:
      word = story[start_of_word: i + 1]
      word.add(word)
      start_of_word = -1
      
answers = {}

for word in word:
  answer = input("ENter a word for " + word + ": ")
  answers[word] = answer

print(answers)

for word in word:
  story = story.replace(word, answers[word])
  
print(story)