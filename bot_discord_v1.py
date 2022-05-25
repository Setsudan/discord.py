import discord
import json
from discord.ext import commands

with open('data.json') as mon_fichier:
    data = json.load(mon_fichier)

class Node:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

print(data)