import turtle
import time


WIDTH, HEIGHT = 700, 600
COLORS = ['red', 'green', 'blue', 'orange','yellow', 'black','purple','pink','brown','cyan']



def get_number_of_racers():
  racers = 0
  while True:
    racers = input('enter the number of racers ( 1 - 10): ')
    if racers.isdigit():
      racers = int(racers)
    else:
      print('input is not numeric...Try again!')
      continue
    if 2 <= racers <= 10:
      return racers
    else:
      print('input is not in range 2 - 10 ...Try again!')
      
def race(colors):
  turtles = create_turtles(colors)
  
  while True:
    for racer in turtles:
      distance = random.randrange(1, 20)
      racer.forward(distance)
      
      x,y = racer.pos()
      if y >= HEIGHT //2 - 10:
        return colors[turtles.index(racer)]
      
['blue','red']
[Turtle1, Turtle2]

      
def create_turtle(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i  + 1) * spacingx, -HEIGHT//2 + 20)
        racer.pendown()
        turtles.append(racer)
    return turtles
    
    
def init_turtles():
    screen = turtle.screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('Turtle Racing!')
  
  

    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('Turtle Racing!')

racers = get_number_of_racers()
init_turtle()

random.shuffle(COLORS)
colors = COLORS[:racers]

winner = race(colors)
print("The winner is the turtle with color:", winner)
time.sleep(5)



