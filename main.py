import discord
from discord.ext import commands

TOKEN = ""
url = "https://twitch.tv/tanzverbot"
# definition of client
client = commands.Bot(command_prefix=">>>", self_bot=True)
client.remove_command('help')


# client events
@client.event
async def on_ready():
    print("Logged in as " + client.user.name)
    print("I'm ready")


@client.event
async def on_message(msg):
    await client.process_commands(msg)


# command error handling
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.reply("Please pass all required arguments", mention_author=False)


# activity command
@client.command(pass_context=True)
async def rpc(ctx, activity, name):
    if ctx.message.author.id != client.user.id:
        return
    else:
        if activity == 'p' or activity == 'P':
            game = discord.Game(name)
            await client.change_presence(activity=game)
            await ctx.reply("Updated Discord RPC to playing " + name, mention_author=False)
        if activity == 'l' or activity == 'L':
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=name))
            await ctx.reply("Updated Discord RPC to listening to " + name, mention_author=False)
        if activity == 'w' or activity == 'w':
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=name))
            await ctx.reply("Updated Discord RPC to watching " + name, mention_author=False)
        if activity == 's' or activity == 'S':
            await client.change_presence(activity=discord.Streaming(name=name, url=url))
            await ctx.reply("Updated Discord RPC to streaming " + name, mention_author=False)


@client.command()
async def ping(ctx):
    print(f'Pong! In {round(client.latency * 1000)}ms')


# Run the bot with the token
client.run(TOKEN, bot=False)
