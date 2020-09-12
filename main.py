"""The main scouting system file"""

import sys

import calculations
import input_data
import team


def switch_case(switch_dict, key):
    """Function for bad switch case"""
    if key not in switch_dict.keys():
        print("Please enter a valid choice")
        function = switch_dict["default"]
    else:
        function = switch_dict[key]
    function_name = function["function_name"]
    if function["parameters"] is not None:
        function_name(*function["parameters"])
    else:
        function_name()


def take_input():
    """Takes user input to either enter data or perform calculations"""
    user_input_type = input(
        "Would you like to enter 'data', perform 'calcs', or 'quit': "
    )
    input_choice = {
        "data": {"function_name": enter_data, "parameters": None},
        "calcs": {
            "function_name": perform_calculations,
            "parameters": None,
        },
        "quit": {"function_name": sys.exit, "parameters": None},
        "default": {"function_name": take_input, "parameters": None},
    }
    switch_case(input_choice, user_input_type)


def enter_data():
    """Performs data entry based on user input"""
    user_input_choice = input(
        "Would you like to enter 'matches', enter 'teams' or 'quit': "
    )
    input_choice = {
        "matches": {"function_name": input_data.add_match, "parameters": None},
        "teams": {"function_name": input_data.add_team, "parameters": None},
        "quit": {"function_name": take_input, "parameters": None},
        "default": {"function_name": enter_data, "parameters": None},
    }
    switch_case(input_choice, user_input_choice)
    enter_data()


def perform_calculations():
    """Performs calculations based on user input"""
    user_input_type = input(
        "What calculation would you like to perform (type 'list calcs' to list calculations, or 'quit'): "
    )
    calculator = calculations.Calculations()
    user_team, user_match = 0, 0
    input_choice = ["quit", "most balls", "least balls", "match info", "total balls", "average balls", "matches played", "team info", "list teams", "list matches"]
    if user_input_type in input_choice:
        if user_input_type not in ["quit", "list calculations", "list teams", "list matches"]:
            user_team = input_data.repeat_input("Enter the team number: ")
            if user_input_type == "match info":
                user_match = input_data.repeat_input("Enter a match number: ")
    input_choice = {
        "list calcs": {
            "function_name": print,
            "parameters": [calculator.get_calculations()],
        },
        "quit": {"function_name": take_input, "parameters": None},
        "default": {"function_name": perform_calculations, "parameters": None},
        "most balls": {
            "function_name": print,
            "parameters": [calculator.most_balls(user_team)],
        },
        "least balls": {
            "function_name": print,
            "parameters": [calculator.least_balls(user_team)],
        },
        "match info": {
            "function_name": print,
            "parameters": [calculator.match_info(user_team, user_match)],
        },
        "total balls": {
            "function_name": print,
            "parameters": [calculator.total_balls(user_team)],
        },
        "average balls": {
            "function_name": print,
            "parameters": [calculator.average_balls(user_team)],
        },
        "matches played": {
            "function_name": print,
            "parameters": [calculator.num_matches(user_team)],
        },
        "team info": {
            "function_name": print,
            "parameters": [calculator.team_info(user_team)]
        },
        "list teams": {
            "function_name": print,
            "parameters": [calculator.list_teams()]
        },
        "list matches": {
            "function_name": print,
            "parameters": [calculator.list_matches()]
        }
    }
    switch_case(input_choice, user_input_type)
    perform_calculations()


take_input()
