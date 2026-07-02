import commands, player, world

class Game:
    def __init__(self):
        self.running = True

        self.player = player.Player()
        self.world = world.World()
        self.running = True
        
    def run(self):
        while self.running:
            command = input("> ")
            commands.execute(
                self,
                command,
            )

game = Game()
game.run()
        