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
from asgiref.sync import sync_to_async

esi = EsiPysi("https://esi.evetech.net/_latest/swagger.json?datasource=tranquility", user_agent="Cailean Blackies")






load_dotenv()
token = os.getenv('DISCORD_TOKEN')
guild = os.getenv('DISCORD_GUILD')



headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Basic MGM4YzI0MTYwY2QyNDFiMmI2N2EzYzRlM2I2NDkxNjU6RUZLRHZNVVpSeHZvYU14UHNIeXJwNEduZzU3Z0lOM2xrZ1dnYUlZYQ==',
}

data = '{"grant_type":"authorization_code", "code":"0Na3WjTPCWe6DMFFKZwYKlBGSTf7EzIlwYSqfLZuF_Vu6rKkXzRs9sgnI21OSicU"}'

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
    if( message.content == eventstring1):
    
          #dont have required corp roles in game to view full list of structures and other info.
         op = esi.get_operation("get_corporations_corporation_id_structures")
         auth = await EsiAuth.from_refresh_token("0c8c24160cd241b2b67a3c4e3b649165", "EFKDvMUZRxvoaMxPsHyrp4Gng57gIN3lkgWgaIYa", "1aiS0Kg3d8Xqk6T3ky1aAID81R7fE6D_ZWgEHJbQ55c")
         op.set_auth(auth)
         result =  await op.execute(corporation_id = "98565967")

       



        

        
                                   
    
    
     

client.run(token)
