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

#create node class. each node stores information about its state, parent, children etc.
class Node(object):
    """
    creates a node given the state of the tic tac toe board
    """
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
        """
        takes inputs root node and current player (1 or 2)
        """
        self.root_node = node
        self.current_node = node
        self.player = player
        self._player_ = copy.deepcopy(player) #keep a copy of original player

    def expand(self):
        """
        This function is performing the expansion of the MCTS. If the terminal 
        """
        rand_move = self.choose_rand_move(self.current_node.state) #select random move
        new_state = copy.deepcopy(self.current_node.state) #create the new state
        self.change_player() #change player before the move
        new_state[rand_move] = self.player #create new state
        
                
        #create the child node and append it to the parent
        self.child_node = Node(new_state)
        self.child_node.parent = self.current_node #set child nodes parent to current node
        self.current_node.children.append(self.child_node) #append child node to current_nodes children

    def simulate(self):
        """
        This function is performing the simulation after the search hits a leaf node
        """
        #get the new child node and expand it
        state = copy.deepcopy(self.child_node.state)
        
        while True:
            rand_move = self.choose_rand_move(state) #create a new move
            self.change_player() #change player before move
            state[rand_move] = self.player #move            
            print(state)
            #find if terminal
            self._terminal_ = self.is_terminal(state)

            #if terminal state (game has ended)         
            if (self._terminal_ == 1) or (self._terminal_ == 2) or (self._terminal_ == 0):
                self.print_board(state) #print board before breaking
                break
    
    def backprop(self):
        """
        this function backpropagate and update the values
        """
        #final state
        _node_ = self.child_node

        while _node_.state != self.root_node.state:
            
            #if the player won

            if self._terminal_ == self._player_: #if winner is the current player
                _node_.N += 1
                _node_.Q += 1
                
            else:
                _node_.N += 1
                
            #change the state to parent
            _node_ = _node_.parent
    
            
    def traverse(self):
        """
        This function traverse until a leaf node is met
        """
        if self.is_terminal(self.current_node.state) == 1: #if current node is terminal 
            #print('terminal') #not correct yet
            pass
            

        elif not self.current_node.children: #if current node has no children means leaf node
            #print('met leaf node')

            #expand
            self.expand()

            #simulate
            self.simulate()

            #backpropagate
            self.backprop()          
            
        else: #if current node has children continue to traverse
            
            #print('looking for children')
            self.current_node = self.max_uct(self.current_node.children)        
            self.change_player() #change player after selecting a child node
            
            return self.traverse()
    
    def rollout(self, n_rollouts):
        """
        performs the rollout given the input number of rollouts (n_rollouts)
        """
        for n in range(n_rollouts):
            #traverse n times
            print(f'rollout {n}')
            self.traverse()
            


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
root_node = Node(state) 

#create two child states
child_state1 = [0, 0, 0, 0, 0, 0, 0, 0, 1]
child_state2 = [0, 0, 0, 0, 0, 0, 0, 1, 0]
child_state3 = [0, 1, 0, 0, 0, 0, 0, 0, 0]

#create child nodes
cn1 = Node(child_state1)
cn2 = Node(child_state2)
cn3 = Node(child_state3)

#assign parent node for children
cn1.parent = root_node
cn2.parent = root_node
cn3.parent = root_node

#new child for cn3
child_state4 = [0, 1, 2, 0, 0, 0, 0, 0, 0]
cn4 = Node(child_state4)
cn3.children.append(cn4)
cn4.parent = cn3

#append the nodes to root node
root_node.children.append(cn1)
root_node.children.append(cn2)
root_node.children.append(cn3)

mcts = MCTS(root_node, 2)
#mcts.traverse()
mcts.rollout(5)

# print(cn1.N)
# print(cn2.N)
# print(cn3.N)
    
#player is not changin during rollout. 1/3/2022

