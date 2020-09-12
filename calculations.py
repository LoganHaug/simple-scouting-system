"""Holds the Calculations class which performs calculations"""
# Internal Imports
import database
import match
import team


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
                    comp_match["num_balls"],
                    comp_match["alliance_color"],
                    comp_match["match_num"],
                )
            )
        self.teams = []
        teams = self.db.find_documents("scouting_system", "teams", {})
        for comp_team in teams:
            self.teams.append(
                team.Team(
                    comp_team["team_number"],
                    comp_team["team_name"],
                    comp_team["rookie_year"],
                )
            )

    def _update_matches(self):
        """Updates matches in the match list

        Returns None"""
        self.matches = []
        comp_matches = self.db.find_documents("scouting_system", "matches")
        for comp_match in comp_matches:
            self.matches.append(
                match.Match(
                    comp_match["team_number"],
                    comp_match["num_balls"],
                    comp_match["alliance_color"],
                    comp_match["match_num"],
                )
            )

    def _update_teams(self):
        """Updates the team list"""
        self.teams = []
        teams = self.db.find_documents("scouting_system", "teams", {})
        for comp_team in teams:
            self.teams.append(
                team.Team(
                    comp_team["team_number"],
                    comp_team["team_name"],
                    comp_team["rookie_year"],
                )
            )
    
    def _update(self):
        """Updates the team and match list"""
        self._update_matches()
        self._update_teams()

    def _is_in_comp(self, team_number):
        """Checks if a team is in the current competition"""
        in_comp = False
        for team in self.teams:
            if team.team_number == team_number:
                in_comp = True
        return in_comp

    def _played_matches(self, team_number):
        """Checks if a team has played matches yet"""
        played_matches = False
        for comp_match in self.matches:
            if comp_match.team_number == team_number:
                played_matches = True
        return played_matches

    def get_calculations(self):
        """Returns a string that states the calculations to be served to a user"""
        return """\nRequires a team number:\n
        - 'most balls'\n
        - 'least balls'\n
        - 'total balls'\n
        - 'average balls'\n
        - 'matches played'\n
        - 'team info'\n
Requires a team number and a match number:\n
        - 'match info'\n
Don't require anything:\n
        - 'list teams'\n
        - 'list matches'\n"""

    def total_balls(self, team_number: int):
        """Returns the total balls scored by a team"""
        self._update()
        if not self._is_in_comp(team_number):
            return f"\n{team_number} is not in the teams collection"
        if not self._played_matches(team_number):
            return f"{team_number} has not played any matches yet"
        total_balls = 0
        for comp_match in self.matches:
            if comp_match.team_number == team_number:
                total_balls += comp_match.num_balls
        return total_balls

    def num_matches(self, team_number: int):
        """Returns the number of matches played by a team"""
        self._update()
        if not self._is_in_comp(team_number):
            return f"\n{team_number} is not in the teams collection\n"
        if not self._played_matches(team_number):
            return f"\n{team_number} has not played any matches yet\n"
        match_list = set()
        for comp_match in self.matches:
            if comp_match.team_number == team_number:
                match_list.add(comp_match.match_num)
        match_string = "\n"
        for match in match_list:
            match_string += f"{match}\n"
        return match_string

    def average_balls(self, team_number: int):
        """Returns the average balls scored by a team"""
        self._update()
        if not self._is_in_comp(team_number):
            return f"{team_number} is not in the teams collection"
        if not self._played_matches(team_number):
            return f"{team_number} has not played any matches yet"
        match_count = 0
        for comp_match in self.matches:
            if comp_match.team_number == team_number:
                match_count += 1
        return self.total_balls(team_number) / match_count
        

    def most_balls(self, team_number):
        """Returns the most balls scored by a team"""
        self._update()
        if not self._is_in_comp(team_number):
            return f"{team_number} is not in the teams collection"
        if not self._played_matches(team_number):
            return f"{team_number} has not played any matches yet"
        most_balls = 0
        for comp_match in self.matches:
            if comp_match.team_number == team_number:
                if comp_match.num_balls > most_balls:
                    most_balls = comp_match.num_balls
        return most_balls

    def least_balls(self, team_number):
        """Returns the least balls scored by a team"""
        self._update()
        if not self._is_in_comp(team_number):
            return f"{team_number} is not in the teams collection"
        if not self._played_matches(team_number):
            return f"{team_number} has not played any matches yet"
        least_balls = None
        for comp_match in self.matches:
            if least_balls is None:
                least_balls = least_balls = comp_match.num_balls
            elif comp_match.team_number == team_number:
                if comp_match.num_balls < least_balls:
                    least_balls = comp_match.num_balls
        return least_balls

    def match_info(self, team_number, match_number):
        """Gets match info for a team in a match"""
        self._update_matches()
        if not self._is_in_comp(team_number):
            return f"{team_number} is not in the teams collection"
        if not self._played_matches(team_number):
            return f"{team_number} has not played any matches yet"
        for comp_match in self.matches:
            if (
                comp_match.team_number == team_number
                and comp_match.match_num == match_number
            ):
                return comp_match.get_match_info()
        return "Could not find the match"

    def list_teams(self):
        """Lists all team numbers"""
        self._update_teams()
        team_list = "\n"
        teams = self.db.find_documents("scouting_system", "teams", {})
        for team in teams:
            team_list += team["team_name"] + ": " + str(team["team_number"]) + "\n"
        if teams == []:
            return "\nNo teams in database\n"
        return team_list

    def team_info(self, team_number):
        self._update_teams()
        """Displays info about a team"""
        team_dict = self.db.find_documents(
            "scouting_system", "teams", {"team_number": team_number}
        )
        if team_dict != []:
            team_dict = team_dict[0]
            user_team = team.Team(
                team_dict["team_number"],
                team_dict["team_name"],
                team_dict["rookie_year"],
            )
            return user_team.get_info()
        return f"Could not find team: {team_number}"

    def list_matches(self):
        self._update_matches()
        """Lists all match numbers"""
        self._update_matches()
        if self.matches == []:
            return "\nNo matches found\n"
        matches = set()
        for match in self.matches:
            matches.add(match.match_num)
        matches = list(matches)
        sorted(matches)
        match_string = "\n"
        for match in matches:
            match_string += str(match) + "\n"
        return match_string
