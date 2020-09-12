"""Holds the match object"""
# No imports


class Match:
    """Represents a Match at a competition"""

    def __init__(
        self,
        team_number: int,
        num_balls: int,
        alliance_color: str,
        match_num: int,
    ):
        """Constructor Function"""
        self.team_number = team_number
        self.num_balls = num_balls
        if alliance_color in ["red", "blue"]:
            self.alliance_color = alliance_color
        self.match_num = match_num

    def get_info(self):
        """Returns a formatted string of information about the match"""
        return f"""Number of Balls Scored: {self.num_balls}
                  \nAlliance Color: {self.alliance_color}
                  \nMatch Number: {self.match_num}
                  \nTeam Number: {self.team_number}"""

    def to_dict(self):
        """Returns a dictionary representing the match object"""
        return {
            "team_number": self.team_number,
            "num_balls": self.num_balls,
            "alliance_color": self.alliance_color,
            "match_num": self.match_num,
        }
