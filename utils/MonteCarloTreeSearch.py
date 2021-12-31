#!/usr/bin/env python
# coding: utf-8

"""
Monte carlo tree search for tic tac toe in Python.
Author: Kaneel Senevirathne. 
Date: December 23rd, 2021

"""

import numpy as np
from collections import defaultdict
import math
import copy

from numpy.core.numeric import Inf 

#create node class
class Node(object):

    def __init__(self, state):        
        self.state = state
        self.parent = None
        self.is_terminal = False
        self.children = []
        self.W = 0
        self.N = 0
        self.Q = 0
        self.U = 0             
        
#monte carlo tree search for tic tac toe
class MCTS:

    def __init__(self, node, player):
        self.root_node = node
        self.current_node = node
        self.player = player
        self._player_ = copy.deepcopy(player) #keep a copy of player

    def expand(self):
        """
        This function is performing the expansion of the MCTS
        """
        rand_move = self.choose_rand_move(self.root_node.state) #select random move
        new_state = copy.deepcopy(self.root_node.state) #create the new state
        new_state[rand_move] = self.player #create new state
        self.change_player() #change player after the move
                
        #create the child node and append it to parent
        self.child_node = Node(new_state)
        self.child_node.parent = self.root_node #set child nodes parent to current node
        self.root_node.children.append(self.child_node) #append child node to current_nodes children

    def simulate(self):
        """
        This function is performing the simulation after the search hits a leaf node
        """
        #get the new child node and expand it
        state = copy.deepcopy(self.child_node.state)
        
        while True:
            rand_move = self.choose_rand_move(state) #create a new move
            state[rand_move] = self.player #move
            self.change_player() #change player

            #find if terminal
            self._terminal_ = self.is_terminal(state)

            #if terminal            
            if (self._terminal_ == 1) or (self._terminal_ == 2) or (self._terminal_ == 0):
                self.print_board(state) #print board before breaking
                break
    
    def backprop(self):
        """
        this function backpropagate and update the values
        """
        global _state_

        #final state
        _state_  = self.child_node

        while _state_ != self.root_node:
            
            #if the player won
            if self._terminal_ == self._player_: #if winner is the current player
                _state_.N += 1
                _state_.Q += 1
            else:
                _state_.N += 1

            #change the state to parent
            _state_ = _state_.parent
    
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
            
    def traverse(self):
        """
        This function traverse until a leaf node is met
        """
        if self.is_terminal(self.current_node.state) == 1: #if current node is terminal 
            print('terminal')
            

        elif not self.current_node.children: #if current node has no children means leaf node
            print('met leaf node')

            #expand
            self.expand()

            #simulate
            self.simulate()

            #backpropagate
            self.backprop()

        else: #if current node has children continue to traverse
            print('looking for children')

            #copy child node, select max uct node
            _state_ = self.current_node
            _state_ = self.max_uct(_state_.children)
            print(_state_.state)
            self.current_node = _state_
            self.child_node = _state_             

            return self.traverse()
    
    def max_uct(self, children):
        """
        find the node with max uct value given node
        """
        #max uct val
        max_uct_val = -Inf
        max_uct_node = None

        for child in children:

            pass

        #for now just use random child
        return np.random.choice(children)

    def uct(self, node):
        """
        calculate the uct value fot this node
        """
        return None


    def change_player(self):
        """
        change the player. This is used in simulation to simulate the game till terminal state. 
        """
        if self.player == 1:
            self.player = 2
        else:
            self.player = 1
    
    def choose_rand_move(self, state):
        """
        This function choose a random move give the current state
        """
        #get available moves and randomly choose a move
        avail_moves = np.where(np.array(state) == 0)[0]
        rand_move = np.random.choice(avail_moves)
        
        return rand_move

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


#testing MCTS
#example state
state = [0, 0, 0, 0, 0, 0, 0, 0, 0]
# state = [1, 1, 1, 0, 0, 0, 0, 0, 0]
root_node = Node(state) 

#create two child states
child_state1 = [0, 0, 0, 0, 0, 0, 0, 0, 1]
child_state2 = [0, 0, 0, 0, 0, 0, 0, 1, 0]
child_state3 = [0, 1, 0, 0, 0, 0, 0, 0, 0]

cn1 = Node(child_state1)
cn2 = Node(child_state2)
cn3 = Node(child_state3)

child_state4 = [0, 1, 2, 0, 0, 0, 0, 0, 0]

cn3.children.append(child_state4)

root_node.children.append(cn1)
root_node.children.append(cn2)
root_node.children.append(cn3)

mcts = MCTS(root_node, 1)
mcts.traverse()


    
    



