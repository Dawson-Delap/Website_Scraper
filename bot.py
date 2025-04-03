import discord
import requests
import json
import time
import random
from bs4 import BeautifulSoup
from discord.ext import commands

# Set up bot with intents
intents = discord.Intents.default()
intents.message_content = True  

bot = commands.Bot(command_prefix="/", intents=intents)
result = "woah"

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return  
    if "white" in message.content.lower():
        await message.channel.send(f"{message.author.display_name} is a cracker")  

    if "black" in message.content.lower():
        await message.channel.send(f"{message.author.display_name} is a basketball person") 

    if "something" in message.content.lower():
        await message.channel.send("https://tenor.com/view/low-tier-god-awesome-mario-twerking-gif-23644561")

    await bot.process_commands(message)  

@bot.command
async def ping(ctx):
    await ctx.send("pong") #Copypaste for more command setup

@bot.command
async def add(ctx, a: int, b: int):
    await ctx.send(f"The sum is {a + b}")

@bot.command
async def sub(ctx, a: int, b: int):
    await ctx.send(f"The difference is {a - b}")

@bot.command
async def mult(ctx, a: int, b: int):
    await ctx.send(f"The product is {a * b}")

@bot.command
async def divi(ctx, a: int, b: int):
    await ctx.send(f"The quotient is {a // b}") 

#The basic maths ^^ for ease

@bot.command
async def RR(ctx):
    user = ctx.author

    streak = streak.get(user.id, 0)

    chamber = [6,5, 4, 3, 2, 1]

    user_chamber = chamber[min(streak, len(chamber) - 1)]
    user_eliminated = random.randint(1, user_chamber) == 1
    bot_eliminated = random.randint(1) == 1

    result_message = []

    if user_eliminated:
        streak[user.id] = 0
        result_message.append(f'💥🔫 BANG! {user.mention} sucks, streak reset to 0.')

    else:
        streak[user.id] = streak + 1
        result_message.append(f"🔫 *click*... {user.mention} survived! Streak: {streak[user.id]} 🔥")
    
    if bot_eliminated:
        result_message.append(f'💥🔫 BANG! Bad luck')
    else:
         result_message.append(f"🔫 *click*... one less in the chamber")
    
    await ctx.send("\n".join(result_message))

    #Code for RR before putting into bot

@bot.command()
async def streak(ctx):
    user = ctx.author
    user_streak = streak.get(user.id, 0)
    await ctx.send(f"{user.mention}, your survival streak is {user_streak}!")

@bot.command()
async def slots(ctx, bet: int = 10):
    global money
    slot1 = 0
    slot2 = 0
    slot3 = 0
    await ctx.send("|V|V|V|")
    msg = await ctx.send("|0|0|0|")
    await ctx.send("|V|V|V|")
    time.sleep(.3)
    slot1 = random.randint(1, 5)
    await msg.edit(content=f"|{slot1}|0|0|")
    time.sleep(.3)
    slot2 = random.randint(1, 5)
    await msg.edit(content=f"|{slot1}|{slot2}|0|")
    time.sleep(.3)
    slot3 = random.randint(1, 5)
    await msg.edit(content=f"|{slot1}|{slot2}|{slot3}|")
    time.sleep(.3)
    if slot1 == slot2 and slot2 == slot3:
        await ctx.send(f"YOU WON!!!! +{bet}")
        money += bet
        await ctx.send(f"Money: {money}")
    else:
        await ctx.send(f"You Lost ;( -{bet}")
        money -= bet
        await ctx.send(f"Money: {money}")



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import asyncio


# Function to search Best Buy and scrape product details
def bestbuy_search_and_scrape(query):
    driver = webdriver.Safari()  # ✅ Uses Safari WebDriver
    driver.get("https://www.bestbuy.com/")

    try:
        # ✅ Find search box and type query
        search_box = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "gh-search-input"))
        )
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)
        time.sleep(1)
        search_box.send_keys(Keys.RETURN)  # Press Enter

        # ✅ Wait for search results to load
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".sku-item"))
        )
        time.sleep(1)
        # ✅ Get first product link
        first_product = driver.find_element(By.CSS_SELECTOR, ".sku-item .sku-title a")
        product_name = first_product.text
        product_link = first_product.get_attribute("href")

        # ✅ Click the first product
        driver.get(product_link)

        # ✅ Wait for product page to load
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.TAG_NAME, "h1"))
        )

        # ✅ Extract product name (double-checking in case layout changes)
        product_name = driver.find_element(By.TAG_NAME, "h1").text

        # ✅ Extract product price (fixes price selector issue)
        try:
            product_price = driver.find_element(By.CSS_SELECTOR, '[data-testid="customer-price"]').text
        except:
            product_price = "Price not found"

    except Exception as e:
        product_name = f"Error: {e}"
        product_link = ""
        product_price = ""

    driver.quit()  # Close Safari
    return product_name, product_link, product_price

@bot.command()
async def bestbuy(ctx, *, query: str):
    """Search Best Buy, get first product name & price"""
    await ctx.send(f"🔎 Searching Best Buy for: `{query}`...")

    # Run Selenium in a separate thread
    loop = asyncio.get_event_loop()
    product_name, product_link, product_price = await loop.run_in_executor(None, bestbuy_search_and_scrape, query)

    if product_link:
        await ctx.send(f"**Product:** [{product_name}]({product_link})\n**Price:** {product_price}")
    else:
        await ctx.send(f"**Error:** {product_name}")

# Run the bot
bot.run("")