import discord
import json
from discord.ext import commands


with open("data.json") as json_data:
    data = json.load(json_data)

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


tuto_msg = "Voilà ton tuto pour "
docu_msg = "Voilà ta docu pour "
# ? Création procédurale de la liste des tuto à partir de data.json
tuto_list = []
all_lang = data.keys()
for lang in all_lang:
    msg = tuto_msg + lang
    tuto_list.append(Node(msg,data[lang]["typo"],data[lang]["tuto"]))

# ? Création procédurale de la liste des docus à partir de data.json
docu_list = []
for lang in all_lang:
    msg = tuto_msg + lang
    docu_list.append(Node(msg,data[lang]["typo"],data[lang]["documentation"]))

first_node = Node(
"Salut, je suis le bot qui va t'aider !\nOn va voir ce qu'on peut faire...\nTu veut un tuto ou une documentation ?\nSi tu ne sait pas, écrit '!liste'" , "start",
 [
     Node("Sur quel language tu as besoin d'un tuto?" , "tuto" , tuto_list),
     Node("Sur quel language tu as besoin d'une documentation?" ,"documentation" ,docu_list)])


availiable_list = []
count=0
for child in first_node.list_child_node[0].list_child_node:
    availiable_list.append(first_node.list_child_node[0].list_child_node[count].keyword[0])
    count += 1

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


@client.command()
async def liste(ctx):
    msg_content = ',\n '.join(data.keys())
    await ctx.send("voici la liste des languages disponible pour le moment")
    await ctx.send(msg_content)
    await ctx.send("Rappeler le bot avec !aide et dites nous votre choix parmi la liste disponible")

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
    if first_node.list_child_node[0].keyword in reponse.content:
        await ctx.send(first_node.list_child_node[0].question)
        ### On attend encore la réponse de l'utilisateur
        reponse2 = await client.wait_for("message", check = check)
        print(reponse2.content)
        ### On fait une boucle for qui vérifie si la réponse est dans la longue liste des language contenant le mot clé de celui-ci
        for i in range(0,len(availiable_list)):
            if reponse2.content in first_node.list_child_node[0].list_child_node[i].keyword:
                await ctx.send(first_node.list_child_node[0].list_child_node[i].question)
                await ctx.send(first_node.list_child_node[0].list_child_node[i].list_child_node)
    
    ### Exactement même procésus que pour le tuto mais pour la documentation

    elif first_node.list_child_node[1].keyword in reponse.content:
        await ctx.send(first_node.list_child_node[1].question)
        reponse2 = await client.wait_for("message", check = check)
        print(reponse2.content)
        print("ok suivant")

        for i in range(0,len(availiable_list)):
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