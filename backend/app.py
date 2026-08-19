from fastapi import FastAPI
from backend.core.game import game

app = FastAPI()

def exe_cmd(command, id: int):
    result = game.game.run(command, id)
    return " ".join(result)

@app.get("/")
def root():
    return {"message": "👋 Hello! I am PyRPG!"}

@app.get("/look/{player_id}")
def look(player_id: int):
    return {"response": exe_cmd("look", player_id)}

@app.get("/go/{player_id}/{location}")
def go(player_id: int, location: str):
    return {"response": exe_cmd(f"go {location}", player_id)}

@app.get("/inventory/{player_id}")
def inventory(player_id: int):
    return {"response": exe_cmd("inventory", player_id)}

@app.get("/fight/{player_id}/{enemy}")
def fight(player_id: int, enemy: str):
    return {"response": exe_cmd(f"fight {enemy}", player_id)}

@app.get("/attack/{player_id}")
def attack(player_id: int):
    return {"response": exe_cmd("attack", player_id)}

@app.get("/defend/{player_id}")
def defend(player_id: int):
    return {"response": exe_cmd("defend", player_id)}

@app.get("/run/{player_id}")
def run(player_id: int):
    return {"response": exe_cmd("run", player_id)}

@app.get("/kill/{player_id}")
def kill(player_id: int):
    return {"response": exe_cmd("kill", player_id)}

@app.get("/spare/{player_id}")
def spare(player_id: int):
    return {"response": exe_cmd("spare", player_id)}
