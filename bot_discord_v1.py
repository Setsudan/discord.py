import discord
from discord.ext import commands

client = commands.Bot(command_prefix="!", description="Bot Daiiruin")
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
    def lang_list(self):
        availiable_list = []
        for child in self.list_child_node:
            availiable_list.append(first_node.list_child_node[0].list_child_node[0].list_child_node[0])
        return availiable_list;

tuto_msg = "Voilà ton tuto pour"
docu_msg = "Voilà ta docu pour"

first_node = Node("Salut, je suis le bot qui va t'aider !\nOn va voir ce qu'on peut faire...\nTu veut un tuto ou une documentation ?" , "start",
[
Node("Sur quel language tu as besoin d'un tuto?" , "tuto" , 
[Node(tuto_msg, ["html","html5"],["https://www.youtube.com/watch?v=qsbkZ7gIKnc"]),
 Node(tuto_msg,  ["css"],["https://youtu.be/gXLjWRteuWI"]),
 Node(tuto_msg,["javascript","js"],["https://youtu.be/PkZNo7MFNFg"]),
 Node(tuto_msg,["scss","sass"],["https://youtu.be/_a5j7KoflTs"]),
 Node(tuto_msg,["react","reactjs"],["https://youtu.be/bMknfKXIFA8"]),
 Node(tuto_msg,["vue","vuejs"],["https://youtu.be/FXpIoQ_rT_c"]),
 Node(tuto_msg,["next","nextjs"],["https://youtu.be/1WmNXEVia8I"]),
 Node(tuto_msg,["remix","remixjs","remixrun"],["https://youtu.be/3CAqFdVlbUA"]),
 Node(tuto_msg,["prisma"],["https://youtu.be/_iFec6mZg24"]),
 Node(tuto_msg,["typescript","ts"],["https://youtu.be/gp5H0Vw39yw"]),
 Node(tuto_msg,["php"],["https://youtu.be/2eebptXfEvw"]),
 Node(tuto_msg,["sql"],["https://youtu.be/Cz3WcZLRaWc"]),
 Node(tuto_msg,["strapi"],["https://youtube.com/playlist?list=PL4cUxeGkcC9h6OY8_8Oq6JerWqsKdAPxn"]),
 Node(tuto_msg,["tailwind","tailwindcss"],["https://youtube.com/playlist?list=PL4cUxeGkcC9gpXORlEHjc5bgnIi5HEGhw"]),
 Node(tuto_msg,["bootstrap","bootstrap 5"],["https://youtu.be/O_9u1P5YjVc"]),
 Node(tuto_msg,["c"],["https://youtu.be/KJgsSFOSQv0"]),
 Node(tuto_msg,["c++","c plus plus"],["https://youtu.be/vLnPwxZdW4Y"]),
 Node(tuto_msg,["c#","csharp","c sharp"],["https://youtu.be/GhQdlIFylQ8"]),
 Node(tuto_msg,["markdown","md"],["https://youtu.be/HUBNt18RFbo"]),
 Node(tuto_msg,["git","github"],["https://youtu.be/RGOj5yH7evk"]),
 Node(tuto_msg,["node","nodejs"],["https://youtube.com/playlist?list=PL4cUxeGkcC9jsz4LDYc6kv3ymONOKxwBU"]),
 Node(tuto_msg,["postgresSQL","postgres"],["https://youtu.be/qw--VYLpxG4"]),
 Node(tuto_msg,["svelte"],["https://youtu.be/ujbE0mzX-CU"]),
 Node(tuto_msg,["java"],["https://youtu.be/grEKMHGYyns"]),
 Node(tuto_msg,["flutter"],["https://youtu.be/VPvVD8t02U8"])
 ]),
Node("Sur quel language tu as besoin d'une documentation?" , "documentation" , 
[Node(docu_msg,"html",["https://developer.mozilla.org/fr/docs/Web/HTML"]),
Node(docu_msg,"python",["https://docs.python.org/fr/3/"]),
 Node(docu_msg,  ["css"],["https://devdocs.io/css/"]),
 Node(docu_msg,["javascript","js"],["https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide"]),
 Node(docu_msg,["scss","sass"],["https://sass-lang.com/guide"]),
 Node(docu_msg,["react","reactjs"],["https://reactjs.org/docs/getting-started.html"]),
 Node(docu_msg,["vue","vuejs"],["https://vuejs.org/guide/introduction.html"]),
 Node(docu_msg,["next","nextjs"],["https://nextjs.org/docs/getting-started"]),
 Node(docu_msg,["remix","remixjs","remixrun"],["https://remix.run/docs/en/v1"]),
 Node(docu_msg,["prisma"],["https://www.prisma.io/docs"]),
 Node(docu_msg,["typescript","ts"],["https://devdocs.io/typescript/typescript-from-scratch"]),
 Node(docu_msg,["php"],["https://www.freecodecamp.org/news/build-a-website-from-start-to-finish-using-wordpress-and-php"]),
 Node(docu_msg,["sql"],["https://docs.microsoft.com/en-us/sql/?view=sql-server-ver16"]),
 Node(docu_msg,["strapi"],["https://strapi.io/resource-center"]),
 Node(docu_msg,["tailwind","tailwindcss"],["https://tailwindcss.com/docs/installation"]),
 Node(docu_msg,["bootstrap","bootstrap 5"],["https://getbootstrap.com/docs/5.2/getting-started/introduction"]),
 Node(docu_msg,["c"],["https://docs.microsoft.com/en-us/cpp/c-language/?view=msvc-170"]),
 Node(docu_msg,["c++","c plus plus"],["https://docs.microsoft.com/en-us/cpp/cpp/?view=msvc-170"]),
 Node(docu_msg,["c#","csharp","c sharp"],["https://docs.microsoft.com/en-us/dotnet/csharp/"]),
 Node(docu_msg,["markdown","md"],["https://www.markdownguide.org"]),
 Node(docu_msg,["git","github"],["https://training.github.com/"]),
 Node(docu_msg,["node","nodejs"],["https://nodejs.org/api/documentation.html"]),
 Node(docu_msg,["postgresSQL","postgres"],["https://www.postgresql.org/docs"]),
 Node(docu_msg,["svelte"],["https://svelte.dev/docs"]),
 Node(docu_msg,["java"],["https://docs.oracle.com/en/java/"]),
 Node(docu_msg,["flutter"],["https://docs.flutter.dev/"])
])
,Node("Voici une liste de tout les languages disponible",["je sais pas","je ne sais pas","jsp"],Node.lang_list())
])

client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    print("Le bot est prêt !")

@client.command()
async def test(ctx):
    print("test effecuté")
    await ctx.send(first_node.list_child_node[0].list_child_node[0].list_child_node)
    await ctx.send(first_node.list_child_node[0].list_child_node[0].keyword)

@client.command()
async def aide(ctx):
    await ctx.send(first_node.question)

    def check(message):
        return message.author == ctx.message.author
    
    reponse = await client.wait_for("message", check = check)
    if reponse.content in first_node.list_child_node[0].keyword:
        await ctx.send(first_node.list_child_node[0].question)
        reponse2 = await client.wait_for("message", check = check)
        print(reponse2.content)
        print("ok suivant")

        for i in len.Node.availiable_list:
            if reponse2.content in first_node.list_child_node[0].list_child_node[i].keyword:
                await ctx.send(first_node.list_child_node[0].list_child_node[i].question)
                await ctx.send(first_node.list_child_node[0].list_child_node[i].list_child_node)
    
    
    elif reponse.content in first_node.list_child_node[1].keyword:
        await ctx.send(first_node.list_child_node[1].question)
        reponse2 = await client.wait_for("message", check = check)
        print(reponse2.content)
        print("ok suivant")

        for i in len.Node.availiable_list:
            if reponse2.content in first_node.list_child_node[1].list_child_node[i].keyword:
                await ctx.send(first_node.list_child_node[1].list_child_node[i].question)
                await ctx.send(first_node.list_child_node[1].list_child_node[i].list_child_node)

@client.event
async def on_message(message):
    message.content = message.content.lower()

    if message.content == "del":
        await message.channel.purge(limit=40)

    await client.process_commands(message)

client.run('OTc4MjI4ODQ0MjE5NzU2NTY0.GchmUG.aIwul33IFqLb34AQVyTa_DsDa9ntbRhxtk9vrY')