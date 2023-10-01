class Player:
  def play (self):
      print ("the player is playing cricket.")

class Batsman(Player):
  def Play (self):
      print ("the batsman is bating")

class Bowler(Player):
  def play(self):
      print(" the bowler is bowling")

batsman=Batsman()
bowler=Bowler()

batsman.Play()
bowler.play()