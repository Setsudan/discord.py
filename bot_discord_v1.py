import discord
from discord.ext import commands

client = commands.Bot(command_prefix="!", description="Bot Daiiruin")

### Class de l'arbre ###

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

### Notre arbre ###

first_node =Node("Salut, je suis le bot qui va t'aider !\nOn va voir ce qu'on peut faire...\nTu veut un tuto ou une documentation ?" , "start",
[Node("Sur quel language tu as besoin d'un tuto?" , "tuto" , [Node("Voilà ton tuto pour html !","html",["https://www.youtube.com/watch?v=qsbkZ7gIKnc"]), Node("Voilà ton tuto pour python !","python",["https://www.youtube.com/watch?v=oUJolR5bX6g"])]),
Node("Sur quel language tu as besoin d'une documentation?" , "documentation" , [Node("Voilà ta documentation pour html !","html",["https://developer.mozilla.org/fr/docs/Web/HTML"]),Node("Voilà ta documentation pour python !","python",["https://docs.python.org/fr/3/"])])])

### Attendre le print dans la console pour être sûr que tout est bon ###

@client.event
async def on_ready():
    print("Le bot est prêt !")

### Juste des tests ###

@client.command()
async def test(ctx):
    print("test effecuté")
    await ctx.send(first_node.list_child_node[0].list_child_node[0].list_child_node)
    await ctx.send(first_node.list_child_node[0].list_child_node[0].keyword)

### Commande d'aide pour un language de programmation ( "!" )###

@client.command()
async def aide(ctx):
    await ctx.send(first_node.question)

    ### Fonction pour voir si le message viens bien de la personne en question et pas une autre ###
    def check(message):
        return message.author == ctx.message.author
    
    ### On attend la réponse de l'utilisateur
    reponse = await client.wait_for("message", check = check)
    ### On regarde si le message est dans la liste contenant le mot clé tuto
    if reponse.content in first_node.list_child_node[0].keyword:
        await ctx.send(first_node.list_child_node[0].question)
        ### On attend encore la réponse de l'utilisateur
        reponse2 = await client.wait_for("message", check = check)
        print(reponse2.content)
        ### On fait une boucle for qui vérifie si la réponse est dans la longue liste des language contenant le mot clé de celui-ci
        for i in range(0,2):
            if reponse2.content in first_node.list_child_node[0].list_child_node[i].keyword:
                await ctx.send(first_node.list_child_node[0].list_child_node[i].question)
                await ctx.send(first_node.list_child_node[0].list_child_node[i].list_child_node)
    
    ### Exactement même procésus que pour le tuto mais pour la documentation

    elif reponse.content in first_node.list_child_node[1].keyword:
        await ctx.send(first_node.list_child_node[1].question)
        reponse2 = await client.wait_for("message", check = check)
        print(reponse2.content)
        print("ok suivant")

        for i in range(0,2):
            if reponse2.content in first_node.list_child_node[1].list_child_node[i].keyword:
                await ctx.send(first_node.list_child_node[1].list_child_node[i].question)
                await ctx.send(first_node.list_child_node[1].list_child_node[i].list_child_node)

### Juste une fonction qui permettera de supprimer des messages ( ici 40... )

@client.event
async def on_message(message):
    message.content = message.content.lower()

    if message.content == "del":
        await message.channel.purge(limit=40)

    await client.process_commands(message)

client.run('OTc4MjI4ODQ0MjE5NzU2NTY0.GchmUG.aIwul33IFqLb34AQVyTa_DsDa9ntbRhxtk9vrY')