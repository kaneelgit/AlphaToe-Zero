#!/usr/bin/env python
# coding: utf-8

# In[ ]:



class Node:
    
    def __init__(self, move, parent):
        
        self.move = move
        self.parent = parent
        self.children = []
        self.wins = 0
        self.visits = 0
        
        print(self.move)
        