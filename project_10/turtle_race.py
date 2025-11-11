import turtle
import time
import random

WIDTH, HEIGHT = 500, 500
COLORS = ["red", "green", "blue", "orange", "yellow", "black", "purple", "pink", "brown", "cyan"]


def get_number_of_turtles(min_n: int = 2, max_n: int = 10, input_fn=input) -> int:


    while True:
        s = input_fn(f"Enter the number of turtles ({min_n}–{max_n}): ").strip()
        try:
            racers = int(s)
        except ValueError:
            print("Enter numeric values only.")
            continue  

        if min_n <= racers <= max_n:
            return racers
        print(f"The number of turtles must be between {min_n} and {max_n} (inclusive).")

def race(colors,screen,fps=30, step_max=12):
    turtles = create_turtles(colors)
    finish_y = HEIGHT // 2 - 10
    frame_ms = int(1000 / fps)

    def tick():
        for r in turtles:
            r.forward(random.randrange(1, step_max))
        screen.update()
        

        crossed = [i for i, r in enumerate(turtles) if r.ycor() >= finish_y]
        if crossed:
            winner_idx = max(crossed, key=lambda i: turtles[i].ycor())
            print("The Winner is ", colors[winner_idx])
        else:
            screen.ontimer(tick, frame_ms)

    tick()


def create_turtles(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1 )
    negative_offset = -WIDTH // 2
    vertical_offset = -HEIGHT // 2 + 30

    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.left(90)
        racer.penup()
        racer.setpos(negative_offset + (i + 1) * spacingx, vertical_offset)
        racer.pendown()
        turtles.append(racer)

    return turtles

def init_turtle():
        
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing")
    screen.tracer(0,0)
    return screen

racers = get_number_of_turtles()
screen  = init_turtle()

random.shuffle(COLORS)
colors = COLORS[:racers]



winner = race(colors, screen)
turtle.mainloop()
print(f"======= The winner is {winner} =======")



