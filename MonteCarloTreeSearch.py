#!/usr/bin/env python
# coding: utf-8

import numpy as np


#monte carlo tree search for tic tac toe
class Node(object):    
    def __init__(self, state):        
        self.state = state
        self.parent = None
        self.children = []
        self.W = 0
        self.N = 0
        self.Q = 0
        self.U = 0

class MCTS(object):
    def __init__(self, root):
        self.root = Node(root)

    def select(self):
        """
        This function selects the best path starting from the root
        """
        return self.select_helper()

    def select_helper(self):
        """
        helper function for select. this function selects the optimal path
        """
        #max state
        max_val = -1000
        
        if self.root.children:
            for child in self.root.children:
                val = child.Q + child.U

                if val > max_val:
                    max_node = child
            return max_node
        else:
            return self.expand()

    def expand(self):
        """
        if a leaf node is reached expand to find a new node
        """
        #avail moves
        avail_moves = np.where(np.array(self.root.state) == 0)
        new_move = np.random.choice(avail_moves[0])
        
        #create new state
        new_state = self.root.state
        new_state[new_move] = 1
        print(self.root.state)

        #create new node for the new expanded state
        expanded_state = Node(new_state)
        expanded_state.parent = self.root

        #assign the new state to start states children
        self.root.children.append(expanded_state)
        
        # print(start_state.state)
        # print(expanded_state.state)

#start state
start = [1, 0, 0, 0, 0, 0, 0, 0, 0]


tree = MCTS(start)

print(tree.select())

