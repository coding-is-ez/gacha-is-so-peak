from guizero import App, Box, Text

window = App(title = "Scores")

subjects = ["Math", "Literature", "English"]
scores = [8, 9, 10]

main_box = Box(window, layout = "grid")

title_box = Box(main_box, grid = [0, 0], border = 2, layout = "grid")
title = Text(title_box, grid = [0, 0, 3, 1], text = "Test scores")

box1 = Box(window, layout = "grid", border = 2, grid = [0, 1])  # Titles / subjects

txt1 = Text(box1, text = "Subject", grid = [0, 0, 3, 1])

for i in range(len(subjects)):
    Text(box1, text = subjects[i], grid = [0, i + 1, 3, 1])

box2 = Box(main_box, layout = "grid", grid = [1, 1])

txt2 = Text(box2, text = "Score", grid = [0, 0, 3, 1])

for j in range(len(scores)):
    Text(box2, text = str(scores[j]), grid = [0, j + 1, 3, 1])

average_box = Box(main_box, layout = "grid", grid = [0, 5])

avr_score = round(sum(scores) / len(scores), 2)

average = Text(average_box, grid = [0, 0, 3, 1], text = str(avr_score))

window.display()