"""Takes user input to store a match in the database"""
# Internal imports
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
    # TODO: Duplicates
    # TODO: Add team to db if not already in
    team_number = repeat_input("Enter the team number: ")
    match_num = repeat_input("Enter the match number: ")
    num_balls = repeat_input("Enter the number of balls scored by the team: ")
    alliance_color = input("Enter the alliance color: ").strip()
    while alliance_color not in ["red", "blue"]:
        print("please enter red or blue")
        alliance_color = input("Enter the alliance color: ").lower()
    db = database.Database("localhost", 27017)
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


def add_team():
    """Takes user input to insert a team into the database"""
    # TODO: Duplicates
    # TODO: Update Information
    team_number = repeat_input("Enter the team number: ")
    team_name = input("Enter the team name: ").strip()
    rookie_year = repeat_input("Enter the team's rookie year: ")
    db = database.Database("localhost", 27017)
    db.insert_documents(
        "scouting_system",
        "teams",
        {
            "team_number": team_number,
            "team_name": team_name,
            "rookie_year": rookie_year,
        }
    )
