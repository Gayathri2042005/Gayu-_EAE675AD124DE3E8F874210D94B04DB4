class player:
    def play(self):
        print("the player is playing cricket.")
class Batsman(player):
    def playn(self):
        print("the betsman is betting.")
class Bowler(player):
    def play(self):
        print("the bowler is bowling.")
batsman=Batsman()
bowler=Bowler()
batsman.play()
bowler.play()              

                