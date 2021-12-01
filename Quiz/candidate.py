from typing import Annotated, NewType


ELECTORAL_VOTES = {'AZ': 11, 'CA': 55, 'FL': 29, 'IA': 6, 'MA': 11, 'OH': 18, 'PA': 20, 'TX': 38}


class Candidate:
    """The presidential candidate"""

    def __init__(self, name, winning_states=None, votes=0):
        """Initialize candidate.
        name: string
        winning_states: a list of strings representing initial winning state(s) (even before voting).
        votes: integer, representing number of votes
        """
        self.name = name
        self.winning_states = winning_states
        if self.winning_states is not None:
            for a,b in ELECTORAL_VOTES.items():
                if a in self.winning_states:
                    votes +=b
        self.votes = votes

    def __str__(self):
        """Return a string representation of this candidate,
        including name and winning state(s).
        """
        if self.winning_states == None:
            return f'{self.name} has not won any state yet.'
        new_str1 = str(self.winning_states).replace("'",'')
        new_str2 = new_str1.replace('[','')
        new_str3 = new_str2.replace(']','')
        return f'{self.name} has won {new_str3}.'

# Attempt 1: successfully calculated trump's votes, but not biden's
    # def __gt__(self, another):
    #     """Overloads ">" operator """
    #     for a,b in ELECTORAL_VOTES.items():
    #         if a in self.winning_states:
    #             self.votes +=b
    #     print(self.votes)
    #     # print(another.votes) why this is 0?
    #     return self.votes > another.votes

    # def win_state(self, state):
    #     """Add a state to winning_states and update votes.
    #     state: a string of state abbreviation
    #     """
    #     self.votes=0
    #     self.winning_states.append(state) # this line added votes together, so that's why I reset the self.votes before into 0
    #     print(self.votes)
    #     return self.winning_states and self.votes

# Attempt 2 succesfully calculated both's votes, but failed to return the values. Changes: added self.votes in the __init__ section
    def __gt__(self, another):
        """Overloads ">" operator """
        # print(self.votes) # this line is 0 since the self.votes value has not been returned.
        return self.votes > another.votes

    def win_state(self, state):
        """Add a state to winning_states and update votes.
        state: a string of state abbreviation
        """
        self.winning_states.append(state)
        for a,b in ELECTORAL_VOTES.items():
            if a in self.winning_states:
                self.votes +=b
        # print(self.votes)
        return self.winning_states, self.votes

# # Attempt 3
#     def win_state(self, state):
#         self.winning_states.append(state)
#         for a,b in ELECTORAL_VOTES.items():
#             if a in self.winning_states:
#                 self.votes +=b



###########################################
# Please DO NOT change code in main method!
###########################################
def main():
    trump = Candidate('Donald Trump', winning_states=['TX', 'FL'])
    biden = Candidate('Joe Biden', winning_states=['CA', 'MA'])
    west = Candidate('Kanye West')
    print('Before voting:')
    print(trump)
    print(biden)
    print(west)
    print('Does Trump win?')
    print(trump > biden)
    print()
    print('After election day:')
    trump.win_state('OH')
    trump.win_state('IA')
    biden.win_state('PA')
    biden.win_state('AZ')
    print(trump)
    print(biden)
    print('Does Trump win?')
    print(trump > biden)


if __name__ == '__main__':
    main()