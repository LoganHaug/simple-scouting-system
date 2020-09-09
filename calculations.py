"""Holds the Calculations class which performs calculations"""
# Internal Imports
import database
import match


class Calculations:
    """Performs calculations on match objects"""

    def __init__(self):
        """Constructor Function

        Aqcuires and assembles all matches into match objects"""
        self.matches = []
        self.database_name = "scouting_system"
        self.db = database.Database("localhost", 27017)
        comp_matches = self.db.find_documents("scouting_system", "matches")
        for comp_match in comp_matches:
            self.matches.append(
                match.Match(
                    comp_match["team_number"],
                    comp_match["team_name"],
                    comp_match["rookie_year"],
                    comp_match["num_balls"],
                    comp_match["alliance_color"],
                    comp_match["match_num"],
                )
            )

    def _update_matches(self):
        """Updates matches in the match list

        Returns None"""
        comp_matches = self.db.find_documents("scouting_system", "matches")
        for comp_match in comp_matches:
            self.matches.append(
                match.Match(
                    comp_match["team_number"],
                    comp_match["team_name"],
                    comp_match["rookie_year"],
                    comp_match["num_balls"],
                    comp_match["alliance_color"],
                    comp_match["match_num"],
                )
            )

    def total_balls(self, team_number: int):
        """Returns the total balls scored by a team"""
        self._update_matches()
        total_balls = 0
        for comp_match in self.matches:
            if comp_match.team_number == team_number:
                total_balls += comp_match.num_balls
        return total_balls

    def num_matches(self, team_number: int):
        """Returns the number of matches played by a team"""
        self._update_matches()
        num_matches = 0
        for comp_match in self.matches:
            if comp_match.team_number == team_number:
                num_matches += 1
        return num_matches

    def average_balls(self, team_number: int):
        """Returns the average balls scored by a team"""
        return self.total_balls(team_number) / self.num_matches(team_number)

    def most_balls(self, team_number):
        """Returns the most balls scored by a team"""
        self._update_matches()
        most_balls = 0
        for comp_match in self.matches:
            if comp_match.team_number == team_number:
                if comp_match.num_balls > most_balls:
                    most_balls = comp_match.num_balls
        return most_balls

    def least_balls(self, team_number):
        """Returns the least balls scored by a team"""
        self._update_matches()
        least_balls = 0
        for comp_match in self.matches:
            if comp_match.team_number == team_number:
                if comp_match.num_balls < least_balls:
                    least_balls = comp_match.num_balls
        return least_balls

    def get_match_info(self, team_number, match_number):
        """Gets match info for a team in a match"""
        self._update_matches()
        for comp_match in self.matches:
            if (
                comp_match.team_number == team_number
                and comp_match.match_number == match_number
            ):
                return comp_match.get_match_info()
        return "Could not find the match"
