#bot.py
import os
import discord
from dotenv import load_dotenv
from esipysi import EsiPysi


esi = EsiPysi("https://esi.evetech.net/_latest/swagger.json?datasource=tranquility", user_agent="Cailean Blackies")

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
guild = os.getenv('DISCORD_GUILD')



              
eventstring1 = "!structures"
              


client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == guild:
            break
                
    print('connected to server:'+ " " + guild.name)

        

@client.event
async def on_message(message):
    if (message.content == eventstring1):
    
        
        await message.channel.send("Pulling Structure Info")
                                   
    
    
    

client.run(token)
