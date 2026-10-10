import time
import json
import os

# Functions

def show_player(player_data):
    print("---- Player Info ----")
    print(f"Name: {player_data['name']}")
    print(f"Age: {player_data['age']}")
    print(f"Gender: {player_data['gender']}")
    print(f"Job: {player_data['jobs']}")
    print("---- Skills Info ----")
    print(f"Skill 1: {player_data['one_skill']}")
    print(f"Skill 2: {player_data['two_skill']}")
    print(f"Skill 3: {player_data['three_skill']}")
    print(f"Useless Skill: {player_data['useless_skill']}")
    print("---- Game State ----")
    print(f"Kills: {player_data['kills_player']}")
    print(f"Deaths: {player_data['death_player']}")
    print(f"Food: {player_data['food_eat']}")
    print(f"Water: {player_data['water_ate']}")
    print(f"Money: {player_data['money_bank']}")
    print()

# A Text Editor
def text_editor(player_data, book_list):
    has_skill = "reading and writing" in (
        player_data["one_skill"],
        player_data["two_skill"],
        player_data["three_skill"],
    )
    if not has_skill:
        print("You don't know Reading and Writing, so you can't write anything.")
        return

    print("Do not name your page one of these names.")
    for name in book_list:
        print(name)

    while True:
        print()
        file_soon = input("Enter filename: ").strip().lower()
        print()
        if file_soon and file_soon not in book_list:
            filename = file_soon
            break
        else:
            print("What did I tell you about names?\n")

    path = f"{filename}.txt"
    try:
        with open(path, "r") as file:
            text = file.read()
        print("\nCurrent file contents:")
        print()
        print(text)
    except FileNotFoundError:
        text = ""
        print("\nFile does not exist. Creating a new file.")

    print("\nType your text below.")
    print("Type SAVE on a new line when finished.\n")
    print()
    new_text = []
    while True:
        line = input()
        if line == "SAVE":
            break
        new_text.append(line)

    with open(path, "w") as file:
        file.write("\n".join(new_text))
    print("\nText is Saved.")

# Opens a .txt file
def open_book(book_list):
    for name in book_list:
        print(name)

    print()
    file_soon = input("Type a piece of media you want read: ").strip().lower()
    print()
    if file_soon in book_list:
        try:
            with open(f"{file_soon}.txt", "r") as file:
                content = file.read()
            print(content)
        except FileNotFoundError:
            print("That book doesn't have any written content yet.")
    else:
        print("That book hasn't been created yet, or you SUCK at spelling.")
        time.sleep(4)
        for number_books in range(101):
            print("You SUCK at spelling")

# Waits
def wait(long):
    time.sleep(long)

# This counts time
def time_counter(long):
    elapsed = 0
    while elapsed < long:
        time.sleep(0.5)
        elapsed += 0.5
        print(f"Wasted {elapsed:.1f} seconds")

    print("Done!")

# Save Point
def save_point(player_data):
    print("Saving Point......")
    print()
    time_counter(2.5)

    print("Five More Seconds......")
    print()
    time_counter(5)

    print("I forgot something, wait some more......")
    print()
    time_counter(2.5)

    with open("data_game.json", "w") as file:
        json.dump(player_data, file, indent=4)

    print("I got it! Game saved.")

def show_town(town, town_data):
    info = town_data[town]
    print(f"Town: {info['names'][0]}")

    for fact in info["facts"]:
        print("-", fact)

    print("\nNearby Towns")

    for place, miles in info["neighbors"].items():
        print(f"{place}: {miles} miles")
    print()
