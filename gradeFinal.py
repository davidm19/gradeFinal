def grade():

  albumTitle = input("What's the album called? ")
  albumArtist = input("Who is the album by? ")

  bannedArtistList = ["Tori Amos", "Captain Beefheart and His Magic Band", "Captain Beefheart", "Eatmewhileimhot"]

  for artist in bannedArtistList:
    if albumArtist == bannedArtistList:
      print("Fuck off.")

  try:
    totalNumber = int(input("How many songs are there? "))
    favNumber = int(input("How many songs were your favorite? "))
    goodNumber = int(input("How many songs did you think were good? "))
    mehNumber = int(input("How many songs did you think were neither good nor bad but 'meh'? "))
    badNumber = int(input("How many songs did you not like? "))
  except ValueError:
    print("SYKE... that's the wrong number")

  favs = input("Which songs were your favorites? ")
  bad = input("Which songs were your least favorites? ")

  comments = input("Anything else you wanna say about the album? ")

  approxgrade = ""

  f1 = favNumber * 7
  g1 = goodNumber * 6
  m1 = mehNumber * 3

  score = (f1 + g1 + m1 + badNumber) / (totalNumber)

  approxgrade = score * 10
  approxgrade = approxgrade / 7

  print( albumArtist + " - " + albumTitle + "; " + "Score: " + str(round(approxgrade, 1)) + "; " + comments + " (Favs: " + favs + "; Least Favs: " + bad + ")")

if __name__ == "__main__":
  grade()
