import renderer

def execute(str):
    action = str.split()[0]
    arg = str.split()
    arg.pop(0)

    if action == "look":
        renderer.render("looks around")