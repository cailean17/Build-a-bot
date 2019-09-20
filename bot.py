#bot.py
import os
import discord
from dotenv import load_dotenv
from esipysi import EsiPysi
from esipysi import EsiAuth
import requests
from esipysi import EsiAuth
import asyncio
import aiohttp
import time







load_dotenv()
token = os.getenv('DISCORD_TOKEN')
guild = os.getenv('DISCORD_GUILD')



headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Basic MGM4YzI0MTYwY2QyNDFiMmI2N2EzYzRlM2I2NDkxNjU6RUZLRHZNVVpSeHZvYU14UHNIeXJwNEduZzU3Z0lOM2xrZ1dnYUlZYQ==',
}

data = '{"grant_type":"authorization_code", "code":"_0qJOz47pKnEX9eWenXXamiaDQlhM3fxz_fYs_XCzd1Y9xbhSEWjgNl3Qro7xAn-"}'

response = requests.post('https://login.eveonline.com/oauth/token', headers=headers, data=data)

print(response.text)






              
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
    if ( message.content == eventstring1):
    
        #this checks if the the eventstring!(!structures) has been sent in discord chat then sends a message and calls the api to gain information
        #right now im trying to get simple character info from eve.
        #Error shows up saying   "op =  await esi.get_operation("get_search") TypeError: object EsiOp can't be used in 'await' expression"
        
        await message.channel.send("Pulling Structure Info")
        esi = EsiPysi("https://esi.evetech.net/_latest/swagger.json?datasource=tranquility", user_agent="Cailean Blackies")
        op =  await esi.get_operation("get_search")
        auth =  await  EsiAuth.from_refresh_token("0c8c24160cd241b2b67a3c4e3b649165", "EFKDvMUZRxvoaMxPsHyrp4Gng57gIN3lkgWgaIYa", "fPV3YRBc8hvU6Cs22_tENN8cm3VEoHrmpxYTMLDZT_A")
        op.set_auth(auth)
        result = await op.execute(categories="character", search="Cailean BLACKIES")
        print(result)

        
                                   
    
    
     

client.run(token)
