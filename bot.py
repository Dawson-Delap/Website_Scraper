import discord
import requests
import json
import time
import threading
from bs4 import BeautifulSoup
from discord.ext import commands

# Set up bot with intents
intents = discord.Intents.default()
intents.message_content = True  

bot = commands.Bot(command_prefix="!", intents=intents)
result = "woah"
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

    if "black" in message.content.lower():
        await message.channel.send(f"{message.author.display_name} is a nigger") 

    if "something" in message.content.lower():
        await message.channel.send("https://tenor.com/view/low-tier-god-awesome-mario-twerking-gif-23644561")

    await bot.process_commands(message)  
website = "https://www.bestbuy.com/site/asus-zenbook-s-14-14-3k-oled-touch-laptop-copilot-pc-intel-core-ultra-7-16gb-memory-1tb-ssd-zumaia-gray/6595522.p?skuId=6595522"
@bot.command()
async def url(ctx, url: str = "nothing"):
    website = url
    await ctx.send(f"Set website to: {website} 😊")
    result = check_product(url)
    send_webhook_message(result)

@bot.command()
async def HardR(ctx, bet: int = 10):
    

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