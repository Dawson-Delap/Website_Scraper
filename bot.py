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
doublenum = 2
doubled = True
dmsg = ""
class DoubleView(discord.ui.View):
    @discord.ui.button(label="Double", style=discord.ButtonStyle.primary, disabled=False)
    async def button_callback(self, button, interaction):
        global doublenum
        global dmsg
        dorn = random.randint(0, 5)
        if dorn == 2:
            await dmsg.edit(content=f"YOU LOST AT {doublenum}")
            button.disabled = True
        else:
            doublenum *= 2
            await dmsg.edit(content=f"{doublenum}")
            
        await interaction.response.edit_message(view=self)


@bot.slash_command()
async def doubleornothing(ctx):
    global dmsg
    global doublenum
    doublenum = 2
    dmsg = await ctx.respond("Double or Nothing", view=DoubleView())

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

@bot.event
async def on_message(message):
    # Don't respond to ourselves
    if message.author == bot.user:
        return

    # Check if the bot is mentioned
    if bot.user in message.mentions:
        await message.channel.send(f"KYS {message.author.mention}")

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
    await ctx.defer()

    user = ctx.author
    bullet_spot = random.randint(1, 6)
    chamber = 6
    shot = False
    player = True

    for i in range(6):
        if shot:
            break

        if player:
            if chamber == bullet_spot:
                await ctx.send(f'💥🔫 BANG! {user.mention} lost!')
                shot = True
            else:
                await ctx.send(f"💨🔫 *click*... {user.mention} survived! 🔥")
                player = False
        else:
            if chamber == bullet_spot:
                await ctx.send(f'💥🔫 BANG! The bot lost!')
                shot = True
            else:
                await ctx.followup.send(f"💨🔫 *click*... Bot survived!")
                player = True

        chamber -= 1
        await asyncio.sleep(0.5)

    await ctx.followup.send("🎮 GAME OVER")

@bot.slash_command(description="Play slots")
async def slots(ctx, bet: int = 10):
    user = ctx.author
    if user.id not in money:
        money[user.id] = 1000  # Initialize money for the user if not present

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
heads = 0
tails = 0
@bot.slash_command(description="Flip a Coin")
async def flip(ctx):
    global tails
    global heads
    hort = random.randint(0, 1)
    if hort == 0:
        await ctx.respond("Tails")
        tails += 1
    elif hort == 1:
        await ctx.respond("Heads")
        heads += 1
    else:
        await ctx.respond("Landed on the side")
@bot.slash_command(description="Flip a Coin")
async def checkflip(ctx):
    global tails
    global heads
    await ctx.respond(f"Tails amount: {tails}, Heads amount: {heads}")


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


def newegg_search_and_scrape(query):
    driver = webdriver.Safari()  # Or switch to Chrome if needed
    try:
        driver.get("https://www.newegg.com/")
        
        # Close the pop-up if it appears
        try:
            close_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "close"))
            )
            close_button.click()
        except:
            pass  # No popup

        # Search
        search_box = WebDriverWait(driver, 10).until(
           EC.presence_of_element_located((By.CSS_SELECTOR, '[title="Search Site"]'))
        )
        search_box.send_keys(query)
        time.sleep(2)
        search_box.send_keys(Keys.RETURN)

        # Wait for search results
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".item-cell"))
        )
        time.sleep(2)

        # First product
        first_product = driver.find_element(By.CSS_SELECTOR, ".item-cell")

        # Product link
        product_link = first_product.find_element(By.CSS_SELECTOR, "a.item-title").get_attribute("href")

        # Product price (may be in several spans)
        try:
            price_whole = first_product.find_element(By.CSS_SELECTOR, ".price-current strong").text
            price_fraction = first_product.find_element(By.CSS_SELECTOR, ".price-current sup").text
            product_price = f"${price_whole}{price_fraction}"
        except:
            product_price = "Price not found"

    except Exception as e:
        print("Error:", e)
        product_link = ""
        product_price = ""
    finally:
        driver.quit()

    return product_link, product_price

@bot.slash_command(description="Search Best Buy and get the first result")
async def search(ctx, *, query: str):
    await ctx.respond(f"🔎 Searching Best Buy and Newegg for `{query}`...")
    loop = asyncio.get_event_loop()
    name, link, price = await loop.run_in_executor(None, bestbuy_search_and_scrape, query)

    if link:
        await ctx.send(f"**Bestbuy Product:** [{name}]({link})\n**Bestbuy Price:** {price}")
    else:
        await ctx.send(f"❌ Error: {name}")
    
    loop = asyncio.get_event_loop()
    link, price = await loop.run_in_executor(None, newegg_search_and_scrape, query)

    if link:
        await ctx.send(f"**Newegg Product:** ({link})\n**Newegg Price:** {price}")
    else:
        await ctx.send(f"❌ Error: {name}")

    await ctx.send(f"**Prices could be from diffent products because search is too broad**")




# Run the bot
bot.run("")