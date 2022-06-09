import turtle
import pandas


# # function to grab state coords
# def get_mouse_click_cor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_cor)
# turtle.mainloop()

screen = turtle.Screen()
screen.title("US State Guessing Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")

no_guessed = 0
guessed_correct = []
# unguessed = []
states = data.state.to_list()
# for state in states:
#     unguessed.append(state)

while len(guessed_correct) < 50:
    answer_state = screen.textinput(f"{no_guessed}/50 States Found", "Please enter the name of a US state.").title()
    if answer_state == "Exit":
        missing_states = [state for state in states if state not in guessed_correct]
        unguessed_states = pandas.DataFrame(missing_states)
        unguessed_states.to_csv("states_to_learn.csv")
        break
    if answer_state in states and answer_state not in guessed_correct:
        # unguessed.remove(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state, False, "center", ("Arial", 10, "normal"))
        guessed_correct.append(answer_state)
        no_guessed += 1
        # print_on_map = PrintState()
        # x = data[data.x == answer_state]
        # y = data[data.y == answer_state]
        # print_on_map.setpos(x, y)
        # print_on_map.write(answer_state, False, "center", ("Arial", 10, "normal"))

winner = turtle.Turtle()
winner.hideturtle()
winner.penup()
if no_guessed == 50:
    winner.write("Congratulations, you guessed all the states!")
else:
    winner.write(f"You guessed {no_guessed}/50 states.", False, "center", ("Arial", 30, "normal"))
turtle.mainloop()


