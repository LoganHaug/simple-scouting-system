"""Houses the team class"""


class Team:
    """Team Class, represents one FRC Team

    get_info returns a formatted string with the relevant team info
    to_dict() represents the object's attributes as a dictionary"""
    def __init__(self, team_number: int, team_name: str, rookie_year: int):
        """Constructor Function

        team_number is the team's number
        team_name is the team's name
        rookie_year is the team's starting year"""
        if (
            isinstance(team_number, int)
            and isinstance(team_name, str)
            and isinstance(rookie_year, int)
        ):
            self.team_number = team_number
            self.team_name = team_name
            self.rookie_year = rookie_year

    def get_info(self):
        """Gets the relevant info about a team formatted in a string

        Returns a string with the essential information about the team object"""
        return f"""Team Number: {self.team_number}
            \nTeam Name: {self.team_name}
            \nRookie Year: {self.rookie_year}"""

    def to_dict(self):
        """ Returns a dictionary with all class properties"""
        return {
            "team_number": self.team_number,
            "team_name": self.team_name,
            "rookie_year": self.rookie_year,
        }
