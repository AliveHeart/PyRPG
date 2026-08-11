import game, loader

while True:
    print("Enter save slot number")
    plr_slot = input(">") or 1

    data = loader.load_json("data/save_slots/" + str(plr_slot) + ".json")
    if data:
        break

while True:
    cmd = input(">") or "look"
    game.game.run(cmd, plr_slot)
