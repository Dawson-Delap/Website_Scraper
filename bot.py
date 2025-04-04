import discord
import random
import asyncio
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set intents and initialize bot
intents = discord.Intents.default()
bot = discord.Bot(intents=intents)

# Initialize streaks and money
streaks = {}
money = {}

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

# Slash Commands Below

@bot.slash_command(description="Simple ping command")
async def ping(ctx):
    await ctx.respond("pong")

@bot.slash_command(description="Add two numbers")
async def add(ctx, a: int, b: int):
    await ctx.respond(f"The sum is {a + b}")

@bot.slash_command(description="Subtract two numbers")
async def sub(ctx, a: int, b: int):
    await ctx.respond(f"The difference is {a - b}")

@bot.slash_command(description="Multiply two numbers")
async def mult(ctx, a: int, b: int):
    await ctx.respond(f"The product is {a * b}")

@bot.slash_command(description="Divide two numbers")
async def divi(ctx, a: int, b: int):
    if b == 0:
        await ctx.respond("Division by zero error.")
    else:
        await ctx.respond(f"The quotient is {a // b}")

@bot.slash_command(description="Russian Roulette")
async def rr(ctx):
    user = ctx.author
    user_eliminated = random.randint(1, 6) == 1
    bot_eliminated = random.randint(1, 6) == 1

    result_message = []

    if user_eliminated:
        result_message.append(f'💥🔫 BANG! {user.mention} lost!')
        streaks[user.id] = 0  # Reset streak if user loses
    else:
        result_message.append(f"🔫 *click*... {user.mention} survived! 🔥")
        streaks[user.id] = streaks.get(user.id, 0) + 1  # Increment streak

    if bot_eliminated:
        result_message.append(f'💥🔫 BANG! The bot lost!')
    else:
        result_message.append(f"🔫 *click*... One less in the chamber.")

    await ctx.respond("\n".join(result_message))

@bot.slash_command(description="Check your roulette streak")
async def streak(ctx):
    user = ctx.author
    user_streak = streaks.get(user.id, 0)
    await ctx.respond(f"{user.mention}, your survival streak is {user_streak}!")

@bot.slash_command(description="Play slots")
async def slots(ctx, bet: int = 10):
    user = ctx.author
    if user.id not in money:
        money[user.id] = 1000  # Initialize money for the user if not present

    current_money = money[user.id]

    if bet > current_money:
        await ctx.respond(f"❌ You don't have enough money to bet {bet}. Current balance: {current_money}")
        return

    msg = await ctx.respond("|V|V|V|")
    await asyncio.sleep(0.3)

    slot1 = random.randint(1, 5)
    await msg.edit(content=f"|{slot1}|0|0|")
    await asyncio.sleep(0.3)

    slot2 = random.randint(1, 5)
    await msg.edit(content=f"|{slot1}|{slot2}|0|")
    await asyncio.sleep(0.3)

    slot3 = random.randint(1, 5)
    await msg.edit(content=f"|{slot1}|{slot2}|{slot3}|")
    await asyncio.sleep(0.3)

    if slot1 == slot2 == slot3:
        money[user.id] += bet
        await ctx.send(f"🎉 YOU WON!!!! +{bet}\nNew balance: {money[user.id]}")
    else:
        money[user.id] -= bet
        await ctx.send(f"💀 You lost. -{bet}\nNew balance: {money[user.id]}")

# Best Buy Scraper

def bestbuy_search_and_scrape(query):
    driver = webdriver.Safari()
    driver.get("https://www.bestbuy.com/")

    try:
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "gh-search-input"))
        )
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)

        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".sku-item"))
        )
        time.sleep(2)

        first_product = driver.find_element(By.CSS_SELECTOR, ".sku-item .sku-title a")
        product_name = first_product.text
        product_link = first_product.get_attribute("href")

        price_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".priceView-hero-price span, .priceView-customer-price span"))
        )
        product_price = price_element.text

    except Exception as e:
        product_name = f"Error: {e}"
        product_link = ""
        product_price = ""

    driver.quit()
    return product_name, product_link, product_price

@bot.slash_command(description="Search Best Buy and get the first result")
async def bestbuy(ctx, *, query: str):
    await ctx.respond(f"🔎 Searching Best Buy for `{query}`...")
    loop = asyncio.get_event_loop()
    name, link, price = await loop.run_in_executor(None, bestbuy_search_and_scrape, query)

    if link:
        await ctx.send(f"**Product:** [{name}]({link})\n**Price:** {price}")
    else:
        await ctx.send(f"❌ Error: {name}")




# Run the bot
bot.run("")