# Import all required libraries
import csv
import os
import random
import re

# Set name and directory of authorised users .csv file
datafilename = "authusers.csv"
datafiledir = "csv"
data_file = os.path.join(datafiledir, datafilename)

# Declare array variables to add all the usernames, passwords and highscores into. These are paralell arrays
nameList = []
passList = []
highscoreList = []

# Open the csv file which contains authorised users and write each respecitve elements to the arrays
with open(data_file, 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        nameList.append(row.get('name'))
        passList.append(row.get('password'))
        highscoreList.append(row.get('hscore'))

# login explain each sect -------------------------
userIndex = 0
loggedIn = False
while not loggedIn:
    print("Please log in so we can save your score to your profile.")
    username = input("Please enter username: ")
    if username in nameList:
        print(f"Hey, {username}.")

        userIndex = nameList.index(username)

        password = input("Please enter password: ")
        if passList[nameList.index(username)] == password:
            print("Password accepted. Thanks.")
            print(
                f"\nHey {username}. Youur current highscore is {highscoreList[userIndex]}")

            loggedIn = True
            break
        else:
            print("Password incorrect. Please check you are logging into the correct account and check the capitalisation/spelling of your password.\n")
    else:
        print("Username not found. Try again.")

songfilename = "songs.csv"
songfiledir = "csv"
song_file = os.path.join(songfiledir, songfilename)

artistList = []
songList = []

with open(song_file, 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        artistList.append(row.get('artist'))
        songList.append(row.get('song'))

score = 0

goes = 0
while goes < 2:
    if goes == 0:
        songIndex = random.randint(0, len(artistList)-1)
        chosenArtist = artistList[songIndex]
        chosenSong = songList[songIndex]
        chosenSongCheck = re.sub(r'[^\w\s]', '', chosenSong)
        chosenSongWords = chosenSong.split(" ")
        chosenSongHidden = ""
    else:
        pass

    for i in range(0, len(chosenSongWords)):
        if i != len(chosenSongWords)-1:
            chosenSongHidden += f"{chosenSongWords[i][0].upper()}? "
        else:
            chosenSongHidden += f"{chosenSongWords[i][0].upper()}?"
    if goes == 0:
        print(f"\nWhat is the song?\n{chosenSongHidden} by {chosenArtist}")
        guess = input(" - ")
    else:
        guess = input("Try again.\n - ")

    guess = re.sub(r'[^\w\s]', '', guess)

    if guess.lower() == chosenSongCheck.lower() and goes == 0:
        print("You did it on the first try! +3 points")
        score += 3
        goes = 0
    elif guess.lower() == chosenSongCheck.lower() and goes == 1:
        print("Second time round. Not bad. +1 point")
        score += 1
        goes = 0
    else:
        print("Wrong. Try again.")
        goes += 1

# Check if score is a highscore and write it to file if it is
if score > int(highscoreList[userIndex]):
    print(f"Your score, {score}, was your highscore!")
    highscoreList[userIndex] = str(score)
    # add new score to csv
    a = [["name", "password", "hscore"]]
    for i in range(len(nameList)):
        temp = [nameList[i], passList[i], highscoreList[i]]
        a.append(temp)
    with open(data_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(a)
elif score < int(highscoreList[userIndex]):
    print(f"Your score, {score}, was less than your current highscore.")
    # dont add score. end game.
elif score == int(highscoreList[i]):
    print(f"Your score, {score}, was the same as your highscore, so close!")
    # dont add score. end game.
