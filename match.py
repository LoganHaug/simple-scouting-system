"""Holds the match object"""
# Internal Imports
import team


class Match(team.Team):
    """Represents a Match at a competition"""

    def __init__(
        self,
        team_number: int,
        team_name: str,
        rookie_year: int,
        num_balls: int,
        alliance_color: str,
        match_num: int,
    ):
        """Constructor Function"""
        super().__init__(team_number, team_name, rookie_year)
        if (
            isinstance(num_balls, int)
            and isinstance(alliance_color, str)
            and isinstance(match_num, int)
        ):
            self.num_balls = num_balls
            if alliance_color in ["red", "blue"]:
                self.alliance_color = alliance_color
            self.match_num = match_num

    def get_info(self):
        """Returns a formatted string of information about the match"""
        return (
            super().get_info()
            + f"""\n\nNumber of Balls Scored: {self.num_balls}
                                    \nAlliance Color: {self.alliance_color}
                                    \nMatch Number: {self.match_num}"""
        )

    def to_dict(self):
        """Returns a dictionary representing the match object"""
        return {
            "team_number": self.team_number,
            "team_name": self.team_name,
            "rookie_year": self.rookie_year,
            "num_balls": self.num_balls,
            "alliance_color": self.alliance_color,
            "match_num": self.match_num,
        }
