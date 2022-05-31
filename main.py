import discord
import json
from discord.ext import commands
from decouple import config

## Récupère la token dans le .env ##
DiscordToken = config("TOKEN")

## Charge le dictionnaire de donnée de data.json ##
with open("data.json") as json_data:
    data = json.load(json_data)

## Initialise comment fonctionne le bot ##
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

# ? Création procédurale de la liste des tuto à partir de data.json

docu_list = []
tuto_list = []
all_lang = data.keys()
## Boucle rajoutant tout les possibilité à l'arbre de donnée ##
for lang in all_lang:
    tuto_list.append(Node(f"Voilà ton tuto pour {lang}",data[lang]["typo"],data[lang]["tuto"]))
    docu_list.append(Node(f"Voilà ta documentation pour {lang}",data[lang]["typo"],data[lang]["documentation"]))


## ? Composition de l'arbres de donnée semi-procédurale ##

first_node = Node(
"Salut, je suis le bot qui va t'aider !\nOn va voir ce qu'on peut faire...\nTu veut un tuto ou une documentation ?\nSi tu ne sait pas, écrit '!liste'" , "start",
[
     Node("Sur quel language tu as besoin d'un tuto?" , "tuto" , tuto_list),
     Node("Sur quel language tu as besoin d'une documentation?" ,"documentation" ,docu_list)
])

## * Dit le nombre de languages disponibles  avant initialisations ##
print(str(len(data.keys())) + " languages disponibles")

### * Préviens quand le bot est près ###

@client.event
async def on_ready():
    print(f'\n\Connecté au compte: {client.user} \nVersion de discord: {discord.__version__}\n')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="coding tutorials"))

### ? Liste des commandes ###

@client.command()
async def test(ctx):
    print("test effecuté")
    await ctx.send(first_node.list_child_node[0].list_child_node[0].list_child_node)
    await ctx.send(first_node.list_child_node[0].list_child_node[0].keyword)

## * Envoie une carte d'utilisateur avec la liste des roles correspondant##
@client.command()
async def me(ctx):
    await ctx.channel.purge(limit=1)
    author = ctx.author
    roles_list = []
    for role in author.roles:
        roles_list.append(role.name)
    roles_list.pop(0)
    roles = "\n - ".join(roles_list)
    memberSince = "Membre depuis " + str(author.created_at)
    embed=discord.Embed(title=author.display_name, description=memberSince, color=author.color)
    embed.set_thumbnail(url=author.avatar_url)
    embed.add_field(name="Roles", value=roles, inline=True)
    await ctx.send(embed=embed)

## * Envoie la liste des languages disponible ##

@client.command()
async def liste(ctx):
    embed= discord.Embed(title="Liste des languages disponibles",description="liste des docus et tuto dispo")
    for lang in all_lang:
        linkToVideo =  data[lang]["tuto"]
        linkToVideo = "\n - ".join(linkToVideo)
        linkToDocu = data[lang]["documentation"]
        linkToDocu = "\n - ".join(linkToDocu)
        desc = "Lien vers la vidéo : \n" + linkToVideo + "\n" + "Lien vers la docu : \n" + linkToDocu
        embed.add_field(name=lang, value=str(desc), inline=False)
    await ctx.send(embed=embed)
    

###*  Commande d'aide pour un language de programmation ( "!" )###

@client.command()
async def aide(ctx):
    await ctx.send(first_node.question)

    ###? Fonction pour voir si le message viens bien de la personne en question et pas une autre ###
    def check(message):
        return message.author == ctx.message.author
    
    ###? On attend la réponse de l'utilisateur
    reponse = await client.wait_for("message", check = check)
    ###? On regarde si le message est dans la liste contenant le mot clé tuto
    if first_node.list_child_node[0].keyword in reponse.content:
        await ctx.send(first_node.list_child_node[0].question)
        ###? On attend encore la réponse de l'utilisateur
        reponse2 = await client.wait_for("message", check = check)
        print(reponse2.content)
        ###? On fait une boucle for qui vérifie si la réponse est dans la longue liste des language contenant le mot clé de celui-ci
        for i in range(0,len(data.keys())):
            if reponse2.content in first_node.list_child_node[0].list_child_node[i].keyword:
                await ctx.send(first_node.list_child_node[0].list_child_node[i].question)
                await ctx.send(first_node.list_child_node[0].list_child_node[i].list_child_node)
    
    ###? Exactement même procésus que pour le tuto mais pour la documentation

    elif first_node.list_child_node[1].keyword in reponse.content:
        await ctx.send(first_node.list_child_node[1].question)
        reponse2 = await client.wait_for("message", check = check)
        print(reponse2.content)
        print("ok suivant")

        for i in range(0,len(data.keys())):
            if reponse2.content in first_node.list_child_node[1].list_child_node[i].keyword:
                await ctx.send(first_node.list_child_node[1].list_child_node[i].question)
                await ctx.send(first_node.list_child_node[1].list_child_node[i].list_child_node)

###? fonction permettant de supprimer 40 messages

@client.event
async def on_message(message):
    message.content = message.content.lower()

    if message.content == "del":
        await message.channel.purge(limit=40)

    await client.process_commands(message)

##? Fin du code et lancement du bot ##
client.run(DiscordToken)