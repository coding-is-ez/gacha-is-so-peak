from guizero import App, Box, PushButton, Text

window = App(title = "Changing lights")

# Box n' buttons
state = "red"

cd = 10

box = Box(window, layout = "grid")

p1 = PushButton(box, grid = [0, 0], text = "", width = 10, height = 5, enabled = False)
p2 = PushButton(box, grid = [0, 1], text = "", width = 10, height = 5, enabled = False)
p3 = PushButton(box, grid = [0, 2], text = "", width = 10, height = 5, enabled = False)

p1.bg = "red"
p2.bg = p3.bg = "white"
def destroyapp():
    window.destroy()

txt = Text(window, text = f"Changes after: {cd} s")

destroy = PushButton(window, command = destroyapp)

def countdown_timer():
    global cd
    global txt
    cd -= 1
    txt.value = f"Changes after: {cd} s"
    if cd == 0:
        change_light()
    else:
        window.after(1000, countdown_timer)

    
def change_light():
    global state
    global cd
    global p1
    global p2
    global p3
    if state == "red":
        p1.bg = "red"
        p2.bg = p3.bg = "white"
        state = "yellow"
    elif state == "yellow":
        p2.bg = "yellow"
        p1.bg = p3.bg = "white"
        state = "green"
    elif state == "green":
        p3.bg = "green"
        p1.bg = p2.bg = "white"
        state = "red"

    cd = 10
    txt.value = f"Changes after: {cd} s"
    window.after(1000, countdown_timer) # Start counting down

change_light() # Start the inf cycle

window.display()


