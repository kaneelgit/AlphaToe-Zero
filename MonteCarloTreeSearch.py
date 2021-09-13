#!/usr/bin/env python
# coding: utf-8

# In[ ]:

class Node:
    
    def __init__(self, move = None, parent = None):
        
        self.move = move
        self.parent = parent
        self.children = {}
        self.wins = 0
        self.N = 0
        self.Q = 0
        
    def add_children(self, children):
        
        for child in children:
            
            self.children[child.move] = child
            
    def value(self, explore):
        
        