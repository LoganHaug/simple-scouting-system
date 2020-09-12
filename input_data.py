"""Takes user input to store a match in the database"""

import database


def input_to_int(user_input: str) -> int or str:
    """Takes a string and tries to convert it to an int, if it can't print an error message"""
    if isinstance(user_input, str):
        if user_input.isnumeric():
            return int(user_input)
    print("Invalid entry")
    return None


def repeat_input(input_message):
    """Repeats user input until the user figures it out"""
    user_input = ""
    while not isinstance(user_input, int):
        user_input = input(input_message)
        user_input = input_to_int(user_input)
    return user_input


def add_match():
    """Takes user input to insert a match into the database"""
    team_number = repeat_input("Enter the team number: ")
    match_num = repeat_input("Enter the match number: ")
    db = database.Database("localhost", 27017)
    if (
        db.find_documents(
            "scouting_system",
            "matches",
            {"team_number": team_number, "match_num": match_num},
        )
        != []
    ):
        while True:
            update_info = input(
                "\nThis team has already played this match, would you like to update the match (yes / no): "
            )
            if update_info.strip().lower() in ["n", "no"]:
                return
            if update_info.strip().lower() in ["y", "yes"]:
                break
    num_balls = repeat_input("Enter the number of balls scored by the team: ")
    alliance_color = input("Enter the alliance color: ").strip()
    while alliance_color not in ["red", "blue"]:
        print("please enter red or blue")
        alliance_color = input("Enter the alliance color: ").lower()
    db.delete_documents(
        "scouting_system",
        "matches",
        {"team_number": team_number, "match_num": match_num},
    )
    db.insert_documents(
        "scouting_system",
        "matches",
        {
            "team_number": team_number,
            "num_balls": num_balls,
            "match_num": match_num,
            "alliance_color": alliance_color,
        },
    )
    if (
        db.find_documents("scouting_system", "teams", {"team_number": team_number})
        == []
    ):
        print("New team detected, please enter the following")
        db.insert_documents(
            "scouting_system",
            "teams",
            {
                "team_number": team_number,
                "team_name": input("Enter the team name: "),
                "rookie_year": repeat_input("Enter the team's rookie year: "),
            },
        )


def add_team():
    """Takes user input to insert a team into the database"""
    team_number = repeat_input("Enter the team number: ")
    db = database.Database("localhost", 27017)
    if (
        db.find_documents("scouting_system", "teams", {"team_number": team_number})
        != []
    ):
        while True:
            update_info = input(
                "Team is already in database, would you like to update it (yes / no): "
            )
            if update_info.strip().lower() in ["n", "no"]:
                return
            elif update_info.strip().lower() in ["y", "yes"]:
                break
    team_name = input("Enter the team name: ").strip()
    rookie_year = repeat_input("Enter the team's rookie year: ")
    db = database.Database("localhost", 27017)
    db.delete_documents("scouting_system", "teams", {"team_number": team_number})
    db.insert_documents(
        "scouting_system",
        "teams",
        {
            "team_number": team_number,
            "team_name": team_name,
            "rookie_year": rookie_year,
        },
    )
