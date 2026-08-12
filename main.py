import game, loader

while True:
    print("Enter save slot number")
    plr_slot = input(">") or 1

    data = loader.load_json("data/save_slots/" + str(plr_slot) + ".json")
    if data:
        break
    else:
        print("No save slot found!")

while True:
    cmd = input(">") or "look"
    result = game.game.run(cmd, plr_slot)

    for text in result:
        print(text)
