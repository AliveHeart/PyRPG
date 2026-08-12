import commands, player, world, renderer

class Game:
    def __init__(self):
        self.running = True

        self.world = world.World()
        
        self.running = True
        
    def run(self, command, plrid):
        return commands.execute(
                self,
                command,
                plrid
            )

game = Game()