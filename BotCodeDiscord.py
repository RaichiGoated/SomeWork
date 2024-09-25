

import discord
from discord.ext import commands, tasks
from discord.ui import Button, View
from discord import app_commands
import asyncio
import requests

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.members = True

client = commands.Bot(command_prefix="$", intents = discord.Intents.all())
bot=client

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

    try:
        synced = await client.tree.sync()
        print(f"synced {len(synced)} command(s)")
        print("-------------------")
    except Exception as e:
        print(e)

api_key = "API NINJA"




@client.tree.command(name="random_word", description="Get a random word")
async def DadJokeCommand(interaction: discord.Interaction):
    api_url = 'https://api.api-ninjas.com/v1/randomword'
    response = requests.get(api_url, headers={'X-Api-Key': f'{api_key}'})
    if response.status_code == requests.codes.ok:

        data = response.json()  
        word = data.get("word")[0]
        
        await interaction.response.send_message(f"Here is your Random Word!\n\n{word}")
    else:
        print("Error:", response.status_code, response.text)


@client.tree.command(name="air_quality", description="Get the Air Quality from a City!")
@app_commands.describe(city="The city you want to check the Air Quality on")
async def AirQualityCommand(interaction: discord.Interaction, city: str):
    try:
        city = city.lower() 
    except Exception as e:
        await interaction.response.send_message("Couldn't process the city name.")
        return

    api_url = 'https://api.api-ninjas.com/v1/airquality?city={}'.format(city)
    response = requests.get(api_url, headers={'X-Api-Key': f'{api_key}'})

    if response.status_code == requests.codes.ok:
        data = response.json() 
        
        air_quality_report = f"Air Quality Report for {city.title()}:\n"
        
        pollutant_names = {
            "CO": "Carbon Monoxide",
            "NO2": "Nitrogen Dioxide",
            "O3": "Ozone",
            "SO2": "Sulfur Dioxide",
            "PM2.5": "Particulate Matter (2.5μm)",
            "PM10": "Particulate Matter (10μm)"
        }

        for pollutant, details in data.items():
            if pollutant in pollutant_names:
                air_quality_report += f"{pollutant_names[pollutant]}: AQI = {details['aqi']}, Concentration = {details['concentration']}\n"

        if "overall_aqi" in data:
            air_quality_report += f"\nOverall AQI: {data['overall_aqi']}\n"
        
        await interaction.response.send_message(air_quality_report)

    else:
        await interaction.response.send_message(f"Error: Could not fetch data for {city.title()}. Please try again.")



@client.tree.command(name="bany_name", description=f"Get some Beautiful Baby names")
@app_commands.describe(gender="What Gender is your baby? Boy, Girl or Neutral")
async def BabyNamesCommand(interaction: discord.Interaction, gender: str):
    gender.lower()

    if gender == "boy":
        api_url = 'https://api.api-ninjas.com/v1/babynames?gender={}'.format(gender)
        response = requests.get(api_url, headers={'X-Api-Key': api_key})
        if response.status_code == requests.codes.ok:
            names = response.json()
            formatted_names = ", ".join(names)
            message = f"Here are some beautiful {gender} baby names:\n {formatted_names}"
            await interaction.response.send_message(message)
        else:
            print("Error:", response.status_code, response.text)


    elif gender == "girl":
        api_url = f'https://api.api-ninjas.com/v1/babynames?gender={gender}'
        response = requests.get(api_url, headers={'X-Api-Key': api_key})

        if response.status_code == requests.codes.ok:
            names = response.json()
            formatted_names = ", ".join(names)
            message = f"Here are some beautiful {gender} baby names:\n {formatted_names}"
            await interaction.response.send_message(message)
        else:
            print("Error:", response.status_code, response.text)


    elif gender == "neutral":
        api_url = f'https://api.api-ninjas.com/v1/babynames?gender={gender}'
        response = requests.get(api_url, headers={'X-Api-Key': api_key})

        if response.status_code == requests.codes.ok:
            names = response.json()
            formatted_names = ", ".join(names)
            message = f"Here are some beautiful {gender} baby names:\n {formatted_names}"
            await interaction.response.send_message(message)
        else:
            print("Error:", response.status_code, response.text)

    else:
        await interaction.response.send_message("Please write the correct gender of your baby. \n\n- Boy\n- Girl\n- Neutral")


@client.tree.command(name="chuck_norris_fact", description=f"Get a random chuck norris fact")
async def ChuckNorrisFactCommand(interaction: discord.Interaction):
    api_url = 'https://api.api-ninjas.com/v1/chucknorris'
    response = requests.get(api_url, headers={'X-Api-Key': api_key})
    if response.status_code == requests.codes.ok:
        data = response.json()
        word = data.get("joke")
        await interaction.response.send_message(f"{word}")
    else:
        print("Error:", response.status_code, response.text)


client.run(discord token)
