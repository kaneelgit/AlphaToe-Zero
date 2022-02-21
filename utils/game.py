from MonteCarloTreeSearch import MCTS, Node
import numpy as np


class tic_tac_toe:
    
    def __init__(self):

        starting_player = np.random.choice([0, 1])

        if np.random.choice([0, 1]) == 1:
            self.player = 1
        else:
            self.player = 2

        self.play_game()

    def play_game(self):
        
        self.current_state = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        while True:
            
            if self.is_terminal(self.current_state) == 0 or self.is_terminal(self.current_state) == 1 or \
                self.is_terminal(self.current_state) == 2:
                print('Game over')
                new_game = input('Do you want to start a new game: (y/n)')
                if new_game == 'y':
                    self.play_game()
                else:
                    break

            if self.player == 1:
                print("Computer move")
                self.computer_move(self.current_state)
                self.print_board(self.current_state)
                self.change_player()
            else:
                print('Human move')
                self.human_move(self.current_state)
                self.print_board(self.current_state)
                self.change_player()

    def computer_move(self, state):
        """
        Function that select the best move from human
        """

        root_node = Node(state)
        mcts = MCTS(root_node, 2)
        mcts.rollout(500)
        self.current_state = mcts.max_uct(root_node.children).state 
    
    def human_move(self, state):
        """
        get human move
        """
        move = input('Enter your move: ')
        self.current_state[int(move)] = 2
    
    def is_terminal(self, state):
        """
        check if state is a terminal state
        """
        #for now just random terminal
        for i in [1, 2]:

            for s in [(1, 2, 3), (1, 4, 7), (7, 8, 9), (3, 6, 9), (1, 5, 9), (3, 5, 7), (2, 5, 8), (4, 5, 6)]:

                if (state[s[0]-1] == i and state[s[1]-1] == i and state[s[2]-1] == i): #subtracting 1 to get correct list indices
                    
                    return i
                    
        if not np.any(np.array(state) == 0):
            
            return 0
    
    def change_player(self):
        """
        change the player. This is used in simulation to simulate the game till terminal state. 
        """
        if self.player == 1:
            self.player = 2
        else:
            self.player = 1
    
    def print_board(self, state):
        """
        this function takes in a state and prints out the board.
        """
        
        #initialize the board        
        print('    |    |   ')
        print('',state[0],' |',state[1],' |',state[2])
        print('____|____|___')
        print('    |    |  ')
        print('',state[3],' |',state[4],' |',state[5])
        print('____|____|___')
        print('    |    |  ')
        print('',state[6],' |',state[7],' |',state[8])
        print('    |    |  ')


if __name__ == "__main__":
    game = tic_tac_toe()