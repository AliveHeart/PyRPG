from backend.systems.commands import execute
from backend.systems.world import World

class Game:
    def __init__(self):
        self.running = True

        self.world = World()
        
        self.running = True
        
    def run(self, command, plrid):
        return execute(
                self,
                command,
                plrid
            )

game = Game()