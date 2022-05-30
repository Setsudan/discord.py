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

first_node = Node("Salut, je suis le bot qui va t'aider !\nOn va voir ce qu'on peut faire...\nTu veut un tuto ou une documentation ?" , "start",
[Node("Sur quel language tu as besoin d'un tuto?" , "tuto" , 
[Node("Voilà ton tuto pour Html !", ["html","html5"],["https://www.youtube.com/watch?v=qsbkZ7gIKnc"]),
 Node("Voilà ton tuto pour Css !",  ["css"],["https://youtu.be/gXLjWRteuWI"]),
 Node("Voilà ton tuto pour Javascript !",["javascript","js"],["https://youtu.be/PkZNo7MFNFg"]),
 Node("Voilà ton tuto pour Scss !",["scss","sass"],["https://youtu.be/_a5j7KoflTs"]),
 Node("Voilà ton tuto pour React !",["react","reactjs"],["https://youtu.be/bMknfKXIFA8"]),
 Node("Voilà ton tuto pour Vue !",["vue","vuejs"],["https://youtu.be/FXpIoQ_rT_c"]),
 Node("Voilà ton tuto pour NextJs !",["next","nextjs"],["https://youtu.be/1WmNXEVia8I"]),
 Node("Voilà ton tuto pour Remix !",["remix","remixjs","remixrun"],["https://youtu.be/3CAqFdVlbUA"]),
 Node("Voilà ton tuto pour Prisma !",["prisma"],["https://youtu.be/_iFec6mZg24"]),
 Node("Voilà ton tuto pour Typescript !",["typescript","ts"],["https://youtu.be/gp5H0Vw39yw"]),
 Node("Voilà ton tuto pour Php !",["php"],["https://youtu.be/2eebptXfEvw"]),
 Node("Voilà ton tuto pour SQL !",["sql"],["https://youtu.be/Cz3WcZLRaWc"]),
 Node("Voilà ton tuto pour Strapi !",["strapi"],["https://youtube.com/playlist?list=PL4cUxeGkcC9h6OY8_8Oq6JerWqsKdAPxn"]),
 Node("Voilà ton tuto pour TailwindCSS !",["tailwind","tailwindcss"],["https://youtube.com/playlist?list=PL4cUxeGkcC9gpXORlEHjc5bgnIi5HEGhw"]),
 Node("Voilà ton tuto pour Bootstrap !",["bootstrap","bootstrap 5"],["https://youtu.be/O_9u1P5YjVc"]),
 Node("Voilà ton tuto pour C !",["c"],["https://youtu.be/KJgsSFOSQv0"]),
 Node("Voilà ton tuto pour C++ !",["c++","c plus plus"],["https://youtu.be/vLnPwxZdW4Y"]),
 Node("Voilà ton tuto pour CSharp !",["c#","csharp","c sharp"],["https://youtu.be/GhQdlIFylQ8"]),
 Node("Voilà ton tuto pour Markdown !",["markdown","md"],["https://youtu.be/HUBNt18RFbo"]),
 Node("Voilà ton tuto pour git !",["git","github"],["https://youtu.be/RGOj5yH7evk"]),
 Node("Voilà ton tuto pour NodeJs !",["node","nodejs"],["https://youtube.com/playlist?list=PL4cUxeGkcC9jsz4LDYc6kv3ymONOKxwBU"]),
 Node("Voilà ton tuto pour PostgreSQL !",["postgresSQL","postgres"],["https://youtu.be/qw--VYLpxG4"]),
 Node("Voilà ton tuto pour Svelte !",["svelte"],["https://youtu.be/ujbE0mzX-CU"]),
 Node("Voilà ton tuto pour Java !",["java"],["https://youtu.be/grEKMHGYyns"]),
 Node("Voilà ton tuto pour Flutter !",["flutter"],["https://youtu.be/VPvVD8t02U8"])
 ]),
Node("Sur quel language tu as besoin d'une documentation?" , "documentation" , 
[Node("Voilà ta documentation pour html !","html",["https://developer.mozilla.org/fr/docs/Web/HTML"]),
Node("Voilà ta documentation pour python !","python",["https://docs.python.org/fr/3/"]),
 Node("Voilà ta documentation pour Css !",  ["css"],["https://devdocs.io/css/"]),
 Node("Voilà ta documentation pour Javascript !",["javascript","js"],["https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide"]),
 Node("Voilà ta documentation pour Scss !",["scss","sass"],["https://sass-lang.com/guide"]),
 Node("Voilà ta documentation pour React !",["react","reactjs"],["https://reactjs.org/docs/getting-started.html"]),
 Node("Voilà ta documentation pour Vue !",["vue","vuejs"],["https://vuejs.org/guide/introduction.html"]),
 Node("Voilà ta documentation pour NextJs !",["next","nextjs"],["https://nextjs.org/docs/getting-started"]),
 Node("Voilà ta documentation pour Remix !",["remix","remixjs","remixrun"],["https://remix.run/docs/en/v1"]),
 Node("Voilà ta documentation pour Prisma !",["prisma"],["https://www.prisma.io/docs"]),
 Node("Voilà ta documentation pour Typescript !",["typescript","ts"],["https://devdocs.io/typescript/typescript-from-scratch"]),
 Node("Voilà ta documentation pour Php !",["php"],["https://www.freecodecamp.org/news/build-a-website-from-start-to-finish-using-wordpress-and-php"]),
 Node("Voilà ta documentation pour SQL !",["sql"],["https://docs.microsoft.com/en-us/sql/?view=sql-server-ver16"]),
 Node("Voilà ta documentation pour Strapi !",["strapi"],["https://strapi.io/resource-center"]),
 Node("Voilà ta documentation pour TailwindCSS !",["tailwind","tailwindcss"],["https://tailwindcss.com/docs/installation"]),
 Node("Voilà ta documentation pour Bootstrap !",["bootstrap","bootstrap 5"],["https://getbootstrap.com/docs/5.2/getting-started/introduction"]),
 Node("Voilà ta documentation pour C !",["c"],["https://docs.microsoft.com/en-us/cpp/c-language/?view=msvc-170"]),
 Node("Voilà ta documentation pour C++ !",["c++","c plus plus"],["https://docs.microsoft.com/en-us/cpp/cpp/?view=msvc-170"]),
 Node("Voilà ta documentation pour CSharp !",["c#","csharp","c sharp"],["https://docs.microsoft.com/en-us/dotnet/csharp/"]),
 Node("Voilà ta documentation pour Markdown !",["markdown","md"],["https://www.markdownguide.org"]),
 Node("Voilà ta documentation pour git !",["git","github"],["https://training.github.com/"]),
 Node("Voilà ta documentation pour NodeJs !",["node","nodejs"],["https://nodejs.org/api/documentation.html"]),
 Node("Voilà ta documentation pour PostgreSQL !",["postgresSQL","postgres"],["https://www.postgresql.org/docs"]),
 Node("Voilà ta documentation pour Svelte !",["svelte"],["https://svelte.dev/docs"]),
 Node("Voilà ta documentation pour Java !",["java"],["https://docs.oracle.com/en/java/"]),
 Node("Voilà ta documentation pour Flutter !",["flutter"],["https://docs.flutter.dev/"])
])
])

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
        for i in range(0,10):
            if reponse2.content in first_node.list_child_node[0].list_child_node[i].keyword:
                await ctx.send(first_node.list_child_node[0].list_child_node[i].question)
                await ctx.send(first_node.list_child_node[0].list_child_node[i].list_child_node)
    
    ### Exactement même procésus que pour le tuto mais pour la documentation

    elif reponse.content in first_node.list_child_node[1].keyword:
        await ctx.send(first_node.list_child_node[1].question)
        reponse2 = await client.wait_for("message", check = check)
        print(reponse2.content)
        print("ok suivant")

        for i in range(0,10):
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