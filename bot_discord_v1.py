import discord

from discord.ext import commands

class Node :
    def __init__(self, question, keyword, list_child_node):
        self.question = question
        self.keyword = keyword
        self.list_child_node = list_child_node

    def user_response(self):
        print(self.question)
        txt = input()
        for child in self.list_child_node:
            if child.keyword in txt:
                child.user_response()

first_node =Node("Comment puis je vous aider ?" , "help" , [Node("Sur quel sujet ?" , "cours" , []) , Node("Sur quel domaine?" , "fichier" , [])])

client = commands.Bot(command_prefix="!")

@client.event

async def on_message(message):
    message.content = message.content.lower()

    if message.author == client.user:
        return

    Help_channel = client.get_channel(978270998287757312)

    if message.content.startswith("start"):
        await Help_channel.send (first_node.question)
        if message.content.startswith(first_node.keyword):
            await Help_channel.send (first_node.list_child_node)

    if message.content.startswith("bonjour"):
        await Help_channel.send("Salut, je suis le meilleur bot !")

    if message.content == "supprimer":
        await message.channel.purge(limit=10)

    await client.process_commands(message)

client.run('OTc4MjI4ODQ0MjE5NzU2NTY0.GchmUG.aIwul33IFqLb34AQVyTa_DsDa9ntbRhxtk9vrY')