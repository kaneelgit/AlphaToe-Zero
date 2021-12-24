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


#monte carlo tree search for tic tac toe
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

class MCTS(Node):

    def __init__(self, node):
        self.current_node = node

    def traverse(self):
        """
        This function traverse until a leaf node is met
        """
        if self.current_node.is_terminal: #if current node is terminal 
            print('terminal')

        if self.current_node.children is None: #if current node has no children means leaf node
            print('met leaf node')
            #move to simulation

        else: #if current node has children continue to traverse
            return self.traverse()

        
    def choose_rand_move(self):
        """
        This function choose a random move give the current state
        """
        #get available moves and randomly choose a move
        avail_moves = np.where(np.array(self.current_node.state) == 0)[0]
        rand_move = np.random.choice(avail_moves)
        
        return rand_move
               
        
#example state
state = [0, 0, 0, 0, 0, 0, 0, 0, 0]
root_node = Node(state) 

mcts = MCTS(root_node)
mcts.traverse()


    
    



