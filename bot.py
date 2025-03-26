import discord
import requests
import json
import time
import threading
import random
from bs4 import BeautifulSoup
from discord.ext import commands

# Set up bot with intents
intents = discord.Intents.default()
intents.message_content = True  

bot = commands.Bot(command_prefix="!", intents=intents)
result = "woah"
money = 100
@bot.event
async def on_ready():
    channel = bot.get_channel(1353899972860444714)  # Replace with your channel ID
    await channel.send("Hello, this is a bot message!")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return  
    
    if "elon" in message.content.lower():
        await message.channel.send(f"L {message.author.display_name}")  

    if "something" in message.content.lower():
        await message.channel.send("https://tenor.com/view/low-tier-god-awesome-mario-twerking-gif-23644561")

    await bot.process_commands(message)  
website = "https://www.bestbuy.com/site/toshiba-65-class-c350-series-led-4k-uhd-smart-fire-tv/6532123.p?skuId=6532123"
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
    slot1 = random.randint(1, 3)
    await msg.edit(content=f"|{slot1}|0|0|")
    time.sleep(.3)
    slot2 = random.randint(1, 3)
    await msg.edit(content=f"|{slot1}|{slot2}|0|")
    time.sleep(.3)
    slot3 = random.randint(1, 3)
    await msg.edit(content=f"|{slot1}|{slot2}|{slot3}|")
    time.sleep(.3)
    if slot1 == slot2 and slot2 == slot3:
        await ctx.send(f"YOU WON!!!! +${bet}")
        money += bet
        await ctx.send(f"Money: {money}")
    else:
        await ctx.send(f"You Lost ;( -${bet}")
        money -= bet
        await ctx.send(f"Money: ${money}")
@bot.command()
async def money34(ctx, bet: int = 10):
    global money
    money += 1000000
    await ctx.send(f"Money: ${money}")
    
@bot.command()
async def checkmoney(ctx, bet: int = 10):
    global money
    await ctx.send(f"Money: ${money}")

@bot.command()
async def url(ctx, url: str = "nothing"):
    website = url
    await ctx.send(f"Set website to: {website} 😊")
    result = check_product(url)
    send_webhook_message(result)

WEBHOOK_URL = "https://discord.com/api/webhooks/1353843712630849666/ct-QDBjeJ1muFzBVk5IdIMSz_8_F-9neeXs7ddfab9-26GHGnMlRshnOziYmjzuz_UiO"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
}

def check_product(web):
    response = requests.get(web, headers=HEADERS)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Extract the price
        price_element = soup.find("div", class_="priceView-hero-price priceView-customer-price")  # This class might change, inspect element in your browser
        if price_element:
            price = price_element.find("span").text.strip()
            smallprice = price.split("$")[-1]
        else:
            price = "Price not found"
        maxprice_element = soup.find("div", class_="pricing-price__regular-price sr-only")  # General class name
        if maxprice_element:
            global maxpricetext
            maxpricetext = maxprice_element.text.strip()
            trimmed_price = maxpricetext.split("$")[-1]  # Extracts the part after "$"
            saving = f"${trimmed_price}"
        else:
            saving = "No Savings"
        if saving == "No Savings":
            return f"💰 Price: **{price}**\n🔗 [Product Link]({web})"
        else:
            high_price = f"${float(trimmed_price) - float(smallprice)}"
            return f"⬇️ Price: **{price}**\n\n💥 Saving: **{high_price}**\n⬆️ Original Price: **{saving}**\n🔗 [Product Link]({web})"

    else:
        return f"⚠️ Error fetching product page (Status Code: {response.status_code})"

def send_webhook_message(message):
    data = {"content": message}
    requests.post(WEBHOOK_URL, data=json.dumps(data), headers={"Content-Type": "application/json"})


def is_real_link(url):
    try:
        response = requests.head(url, allow_redirects=True, timeout=5)
        return response.status_code == 200
    except requests.RequestException:
        return False
    

@bot.command()
async def repeatcheck(ctx, user: discord.Member, limit: int = 10):
    """Fetch past messages from a specific user."""
    async for message in ctx.channel.history(limit=100):  # Fetch more to filter
        price = message.content.split("Price: $")[-1]
        if price == maxpricetext:
            return True
        
def product_check_loop():
    global result
    while True:
        lastresult = result
        result = check_product(website)
        if lastresult != result:
            send_webhook_message(result)
        time.sleep(300)  # Wait 5 minutes before checking again

# Start the product check in a separate thread
threading.Thread(target=product_check_loop, daemon=True).start()

# Run the bot
bot.run("")