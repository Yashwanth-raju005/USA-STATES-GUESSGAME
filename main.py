import turtle
import pandas

screen=turtle.Screen()
screen.title("U.S. States Game")

img="blank_states_img.gif"
screen.addshape(img)

turtle.shape(img)

data=pandas.read_csv("50_states.csv")
all_states=data.state.to_list()
guessed_states=[]



while len(guessed_states) < 50:
    answer_states=screen.textinput(title=f"{len(guessed_states)}/50 States Correct",prompt="Whats another state").title()
    if answer_states=="Exit":
        missing_states=[]
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data=pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_states in all_states:
        guessed_states.append(answer_states)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=data[data.state==answer_states]
        t.goto(state_data.x.item(),state_data.y.item())
        t.write(answer_states)



screen.exitonclick()