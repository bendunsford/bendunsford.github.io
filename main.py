import os
import requests
import discord
from replit import db
from discord import app_commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.environ.get('DISCORD_TOKEN')
GUILD = os.environ.get('DISCORD_GUILD')
GUILD_2 = os.environ.get("GUILD_2")
GUILD_ID = os.environ.get("GUILD_ID")
GUILD_ID_2 = os.environ.get("GUILD_ID_2")

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@tree.command(name = "militaries", description = "Returns .txt of unit numbers, quality and capacity", guild=discord.Object(GUILD_ID))
async def military(interaction):
  file=open("mil.txt",'w')
  file.write('')
  file.close()
  API_KEY=db[f"{interaction.user.id}"]
  def mil(API_KEY):
    link=''.join(["http://diplomacyandstrifeapi.com/api/AllianceMilitary?APICode=", str(API_KEY)])
    mil=requests.get(link)
    mil=mil.json()
    mil=list(mil)
    l=len(mil)
    file = open("mil.txt", "a")
    for x in range(l):
      milx=mil[x]
      inf=milx["Infantry"]
      infq=milx["InfantryQuality"]
      natid=milx["NationId"]  
      a=(str(milx["NationName"]) + " " + str(natid) + "\n")
      file.writelines(a)
      a=("Infantry: " + str(inf) + " Quality: "+ str(infq)+"\n")
      file.writelines(a)
      a=("Support Vehicles: " + str(milx["SupportVehicles"]) + " Quality: " + str(milx["SupportVehiclesQuality"])+"\n")
      file.writelines(a)
      a=("Max Infranty Capacity: " + str(milx["InfantryCapacity"]) + " Used Infantry Capacity: " + str(milx["UsedInfantryCapacity"])+"\n")
      file.writelines(a)
      a=("Artillery: " + str(milx["Artillery"]) + " Quality: " + str(milx["ArtilleryQuality"])+ "\n")
      file.writelines(a)
      a=("Missile Launchers: " + str(milx["MissileLaunchers"]) + " Quality: " + str(milx["MissileLaunchersQuality"])+"\n") 
      file.writelines(a)
      a=("Max Artillery Capacity: " + str(milx["ArtilleryCapacity"]) + " Used Artillery Capacity: " + str(milx["UsedArtilleryCapacity"])+"\n")
      file.writelines(a)
      a=("Light Tanks: " + str(milx["LightTanks"]) + " Quality: " + str(milx["LightTanksQuality"])+"\n")
      file.writelines(a)
      a=("Medium Tanks: " + str(milx["MediumTanks"]) + " Quality: " + str(milx["MediumTanksQuality"])+"\n")
      file.writelines(a)
      a=("Heavy Tanks: " + str(milx["HeavyTanks"]) + " Quality: " + str(milx["HeavyTanksQuality"])+"\n") 
      file.writelines(a)
      a=("Light Mechs: " + str(milx["LightMechs"]) + " Quality: " + str(milx["LightMechsQuality"])+"\n")
      file.writelines(a)
      a=("Heavy Mechs: " + str(milx["HeavyMechs"]) + " Quality: " + str(milx["HeavyMechsQuality"])+'\n') 
      file.writelines(a)
      a=("Precursor Mechs: " + str(milx["PrescusarMech"]) + " Quality: " + str(milx["PrescusarMechQuality"])+"\n") 
      file.writelines(a)
      a=("Max Armor Capacity: " + str(milx["ArmourCapacity"]) + " Used Armor Capacity: " + str(milx["UsedArmourCapacity"])+"\n") 
      file.writelines(a)
      a=("Fighters: " + str(milx["Fighters"]) + " Quality: " + str(milx["FightersQuality"])+"\n") 
      file.writelines(a)
      a=("Bombers: " + str(milx["Bombers"]) + " Quality: " + str(milx["BombersQuality"])+'\n') 
      file.writelines(a)
      a=("Helicopters: " + str(milx["Helicopters"]) + " Quality: " + str(milx["HelicoptersQuality"])+"\n") 
      file.writelines(a)
      a=("Drones: " + str(milx["Drones"]) + " Quality: " + str(milx["DronesQuality"])+"\n") 
      file.writelines(a)
      a=("Stealth Fighters: " + str(milx["StealthFighters"]) + " Quality: " + str(milx["StealthFightersQuality"])+"\n")
      file.writelines(a)
      a=("Stealth Bombers: " + str(milx["StealthBombers"]) + " Quality: " + str(milx["StealthBombersQuality"])+'\n')
      file.writelines(a)
      a=("Max Air Capacity: " + str(milx["AirCapacity"]) + " Used AIr Capacity: " + str(milx["UsedAirCapacity"])+'\n')
      file.writelines(a)
      a=("Destroyers: " + str(milx["Destroyers"]) + " Quality: " + str(milx["DestroyersQuality"])+'\n')
      file.writelines(a)
      a=("Submarines: " + str(milx["Subs"]) + " Quality: " + str(milx["SubsQuality"])+'\n') 
      file.writelines(a)
      a=("Cruisers: " + str(milx["Cruisers"]) + " Quality: " + str(milx["CruisersQuality"])+"\n") 
      file.writelines(a)
      a=("Battleships: " + str(milx["Battleships"]) + " Quality: " + str(milx["BattleshipsQuality"])+'\n') 
      file.writelines(a)
      a=("Carriers: " + str(milx["Carriers"]) + " Quality: " + str(milx["CarriersQuality"])+'\n') 
      file.writelines(a)
      a=("Max Naval Capacity: " + str(milx["NavalCapacity"]) + " Used Naval Capacity: " + str(milx["UsedNavalCapacity"])+'\n') 
      file.writelines(a)
      a=('\n')
      file.writelines(a)
    file.close()
  mil(API_KEY)
  with open("mil.txt","r") as file:
    await interaction.response.send_message("Our militaries are:", file=discord.File(file, "mil.txt"))
  file=open("mil.txt",'w')
  file.write('')
  file.close()

@tree.command(name = "militaries", description = "Returns .txt of unit numbers, quality and capacity", guild=discord.Object(GUILD_ID_2))
async def military(interaction):
  file=open("mil.txt",'w')
  file.write('')
  file.close()
  API_KEY=db[f"{interaction.user.id}"]
  def mil(API_KEY):
    link=''.join(["http://diplomacyandstrifeapi.com/api/AllianceMilitary?APICode=", str(API_KEY)])
    mil=requests.get(link)
    mil=mil.json()
    mil=list(mil)
    l=len(mil)
    file = open("mil.txt", "a")
    for x in range(l):
      milx=mil[x]
      inf=milx["Infantry"]
      infq=milx["InfantryQuality"]
      natid=milx["NationId"]  
      a=(str(milx["NationName"]) + " " + str(natid) + "\n")
      file.writelines(a)
      a=("Infantry: " + str(inf) + " Quality: "+ str(infq)+"\n")
      file.writelines(a)
      a=("Support Vehicles: " + str(milx["SupportVehicles"]) + " Quality: " + str(milx["SupportVehiclesQuality"])+"\n")
      file.writelines(a)
      a=("Max Infranty Capacity: " + str(milx["InfantryCapacity"]) + " Used Infantry Capacity: " + str(milx["UsedInfantryCapacity"])+"\n")
      file.writelines(a)
      a=("Artillery: " + str(milx["Artillery"]) + " Quality: " + str(milx["ArtilleryQuality"])+ "\n")
      file.writelines(a)
      a=("Missile Launchers: " + str(milx["MissileLaunchers"]) + " Quality: " + str(milx["MissileLaunchersQuality"])+"\n") 
      file.writelines(a)
      a=("Max Artillery Capacity: " + str(milx["ArtilleryCapacity"]) + " Used Artillery Capacity: " + str(milx["UsedArtilleryCapacity"])+"\n")
      file.writelines(a)
      a=("Light Tanks: " + str(milx["LightTanks"]) + " Quality: " + str(milx["LightTanksQuality"])+"\n")
      file.writelines(a)
      a=("Medium Tanks: " + str(milx["MediumTanks"]) + " Quality: " + str(milx["MediumTanksQuality"])+"\n")
      file.writelines(a)
      a=("Heavy Tanks: " + str(milx["HeavyTanks"]) + " Quality: " + str(milx["HeavyTanksQuality"])+"\n") 
      file.writelines(a)
      a=("Light Mechs: " + str(milx["LightMechs"]) + " Quality: " + str(milx["LightMechsQuality"])+"\n")
      file.writelines(a)
      a=("Heavy Mechs: " + str(milx["HeavyMechs"]) + " Quality: " + str(milx["HeavyMechsQuality"])+'\n') 
      file.writelines(a)
      a=("Precursor Mechs: " + str(milx["PrescusarMech"]) + " Quality: " + str(milx["PrescusarMechQuality"])+"\n") 
      file.writelines(a)
      a=("Max Armor Capacity: " + str(milx["ArmourCapacity"]) + " Used Armor Capacity: " + str(milx["UsedArmourCapacity"])+"\n") 
      file.writelines(a)
      a=("Fighters: " + str(milx["Fighters"]) + " Quality: " + str(milx["FightersQuality"])+"\n") 
      file.writelines(a)
      a=("Bombers: " + str(milx["Bombers"]) + " Quality: " + str(milx["BombersQuality"])+'\n') 
      file.writelines(a)
      a=("Helicopters: " + str(milx["Helicopters"]) + " Quality: " + str(milx["HelicoptersQuality"])+"\n") 
      file.writelines(a)
      a=("Drones: " + str(milx["Drones"]) + " Quality: " + str(milx["DronesQuality"])+"\n") 
      file.writelines(a)
      a=("Stealth Fighters: " + str(milx["StealthFighters"]) + " Quality: " + str(milx["StealthFightersQuality"])+"\n")
      file.writelines(a)
      a=("Stealth Bombers: " + str(milx["StealthBombers"]) + " Quality: " + str(milx["StealthBombersQuality"])+'\n')
      file.writelines(a)
      a=("Max Air Capacity: " + str(milx["AirCapacity"]) + " Used AIr Capacity: " + str(milx["UsedAirCapacity"])+'\n')
      file.writelines(a)
      a=("Destroyers: " + str(milx["Destroyers"]) + " Quality: " + str(milx["DestroyersQuality"])+'\n')
      file.writelines(a)
      a=("Submarines: " + str(milx["Subs"]) + " Quality: " + str(milx["SubsQuality"])+'\n') 
      file.writelines(a)
      a=("Cruisers: " + str(milx["Cruisers"]) + " Quality: " + str(milx["CruisersQuality"])+"\n") 
      file.writelines(a)
      a=("Battleships: " + str(milx["Battleships"]) + " Quality: " + str(milx["BattleshipsQuality"])+'\n') 
      file.writelines(a)
      a=("Carriers: " + str(milx["Carriers"]) + " Quality: " + str(milx["CarriersQuality"])+'\n') 
      file.writelines(a)
      a=("Max Naval Capacity: " + str(milx["NavalCapacity"]) + " Used Naval Capacity: " + str(milx["UsedNavalCapacity"])+'\n') 
      file.writelines(a)
      a=('\n')
      file.writelines(a)
    file.close()
  mil(API_KEY)
  with open("mil.txt","r") as file:
    await interaction.response.send_message("Our militaries are:", file=discord.File(file, "mil.txt"))
  file=open("mil.txt",'w')
  file.write('')
  file.close()

@tree.command(name = "bind_api", description = "Bind API key to discord user", guild=discord.Object(GUILD_ID))
async def bind(interaction, api: str = ''):
  db[f"{interaction.user.id}"] = f"{api}"
  await interaction.response.send_message("Bound!")

@tree.command(name = "bind_api", description = "Bind API key to discord user", guild=discord.Object(GUILD_ID_2))
async def bind(interaction, api: str = ''):
  db[f"{interaction.user.id}"] = f"{api}"
  await interaction.response.send_message("Bound!")

@tree.command(name = "unbind_api", description = "Unbind API key from discord user", guild=discord.Object(GUILD_ID))
async def unbind(interaction):
  del db[f"{interaction.user.id}"]
  await interaction.response.send_message("Unbound!")

@tree.command(name = "unbind_api", description = "Unbind API key from discord user", guild=discord.Object(GUILD_ID_2))
async def unbind(interaction):
  del db[f"{interaction.user.id}"]
  await interaction.response.send_message("Unbound!")

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
    for guild in client.guilds:
        if guild.name == GUILD_2:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
    await tree.sync(guild=discord.Object(GUILD_ID))
    print("Ready!")

    await tree.sync(guild=discord.Object(GUILD_ID_2))
    print("Ready!")

client.run(TOKEN)



