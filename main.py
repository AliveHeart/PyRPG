import game, loader

while True:
    print("Enter save slot number")
    plr_slot = input(">") or 1

    data = loader.load_json("data/save_slots/" + str(plr_slot) + ".json")
    if data:
        break
    else:
        print("No save slot found!")
        game.game.run("look", plr_slot)
        print("Created new save slot!")
        break

while True:
    cmd = input(">") or "look"
    result = game.game.run(cmd, plr_slot)

    for text in result:
        print(text)

    split_cmd = cmd.split()
    if split_cmd[0] == "load" and split_cmd[1]:
        if loader.load_json("data/save_slots/" + str(plr_slot) + ".json"):
            plr_slot = split_cmd[1]
            print("loaded slot " + split_cmd[1])
        else:
            print("No save slot found!")

