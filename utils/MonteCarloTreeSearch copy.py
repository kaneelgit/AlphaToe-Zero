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
        self.children = defaultdict(int)
        self.W = 0
        self.N = 0
        self.Q = 0
        self.U = 0

class MCTS(object):
    def __init__(self, exploration_weight = 1):
        self.Q = defaultdict(int)
        self.N = defaultdict(int)
        self.W = defaultdict(int)
        self.U = defaultdict(int)
        self.children = dict()
        self.exploration_weight = exploration_weight

    def choose(self, node):
        #check if its the terminal node
        if node.is_terminal():
            pass
        
        #check if node is not in children
        if node not in self.children:
            #not in children. new node reached
            return node
        
        #if node is in self.children select the node with the maximum score
        def score(n):
            if self.N[n] == 0:
                return float("-inf")
            return self.Q[n] /self.N[n]

        return max(self.children[node], key = score)

    def rollout(self, node):
        path = self._select_(node)
        leaf = path[-1]
        self._expand_(leaf)
        reward = self._simulate_(leaf)
        self._backpropagate_(path, reward)

    def _select_(self, node):
        #find an unexplored descendant
        path = []
        while True:
            path.append(node)
            if node not in self.children or not self.children[node]:
                return path
            
            unexplored = self.children[node] - self.children.keys()

            if unexplored:
                n = unexplored.pop()
                path.append(n)
                return path
            node = self._uctselect_(node)

    def _expand_(self, node):

        if node in self.children:
            pass
        self.children[node] = node.find_children()

    def _simulate_(self, node):
        invert_reward = True
        while True:
            if node.is_terminal():
                reward = node.reward()
                return 1 - reward if invert_reward else reward

            node = node.find_random_child()
            invert_reward = not invert_reward

    def _backpropagate_(self, path, reward):

        for node in reversed(path):
            self.N[node] += 1
            self.Q[node] += reward
            self.U[node] = None
            self.W[node] = None
            reward = 1 - reward

    def _uctselect_(self, node):

        assert all(n in self.children for n in self.children[node])

        log_N = math.log(self.N[node])

        def uct(n):

            return self.Q[n]/self.N[n] + self.exploration_weight * math.sqrt(log_N / self.N[n])

        return max(self.children[node], key = uct)

class Node()

