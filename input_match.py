"""Takes user input to store a match in the database"""
# Internal imports
import database

def add_match():
    """Takes user input to insert a match into the database"""
    while True:
        team_number = input("Enter the team number: ")
        rookie_year = input("Enter the teams rookie year: ")
        num_balls = input("Enter the number of balls scored by the team: ")
        match_num = input("Enter the match number: ")
        alliance_color = input("Enter the alliance color: ")
        if team_number.isnumeric() and rookie_year.isnumeric() and num_balls.isnumeric() and match_num.isnumeric():
            team_number = int(team_number)
            rookie_year = int(rookie_year)
            num_balls = int(num_balls)
            match_num = int(match_num)
            if alliance_color in ["red", "blue"]:
                break
    team_name = input("Enter the team name: ")
    db = database.Database("localhost", 27017)
    db.insert_documents("scouting_system", "matches", {
        {"team_number": team_number,
         "team_name": team_name,
         "rookie_year": rookie_year,
         "num_balls": num_balls,
         "match_num": match_num,
         "alliance_color": alliance_color}})

    
