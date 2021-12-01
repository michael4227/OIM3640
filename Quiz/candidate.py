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
        self.votes = votes

    def __str__(self):
        """Return a string representation of this candidate,
        including name and winning state(s).
        """
        new_str = ''
        for i in self.winning_states():
            new_str += f'\n\t{i}'
        return f'{self.name} has won in {new_str}'

    def __gt__(self, another_Candidate):
        """Overloads ">" operator """
        return self.votes > another_Candidate.votes


    def win_state(self, state):
        """Add a state to winning_states and update votes.
        state: a string of state abbreviation
        """
        self.winning_states.append(state)
        return self.winning_states
    
    def votes(self):
        for i in self.winning_states:
            self.votes += ELECTORAL_VOTES[self.winning_states]
        return self.votes


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