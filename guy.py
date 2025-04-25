import discord
import random
import asyncio

# Set intents and initialize bot
intents = discord.Intents.default()
bot = discord.Bot(intents=intents)

@bot.event
async def on_message(message):
    # Don't respond to ourselves
    if message.author == bot.user:
        return

    # Check if the bot is mentioned
    if bot.user in message.mentions:
        await message.channel.send(f"KYS {message.author.mention}")
        whatPic = random.randint(0,2)
        if whatPic == 0:
            await message.channel.send(f"https://tenor.com/view/flightreacts-flight-spin-flight-driving-driving-gif-14821482636596098762")
        elif whatPic == 1:
            await message.channel.send(f"https://tenor.com/view/flight-waffle-house-waffle-house-flightreacts-gif-291001867069513835")
        elif whatPic == 2:
            await message.channel.send(f"https://tenor.com/view/flight-shoe-gif-1842982099687274858")
    respond = random.randint(0,100)
    if respond == 34:
        whatPic = random.randint(0,2)
        if whatPic == 0:
            await message.channel.send(f"https://tenor.com/view/flightreacts-flight-spin-flight-driving-driving-gif-14821482636596098762")
        elif whatPic == 1:
            await message.channel.send(f"https://tenor.com/view/flight-waffle-house-waffle-house-flightreacts-gif-291001867069513835")
        elif whatPic == 2:
            await message.channel.send(f"https://tenor.com/view/flight-shoe-gif-1842982099687274858")

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


@bot.slash_command(description= "Double or Nothin")
async def doubleornothing(ctx):
    global dmsg
    global doublenum
    doublenum = 2
    dmsg = await ctx.respond("Double or Nothing", view=DoubleView())

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

@bot.slash_command(description= "Random Ghost")
async def ghost(ctx):
    ghosts = ["Spirit","Wraith","Phantom","Poltergeist","Banshee","Jinn","Mare","Revenant","Shade","Demon","Yurei","Oni","Yokai","Hantu","Goryo","Myling","Onryo","The Twins","Raiju","Obake","The Mimic","Moroi","Deogen","Thaye"]
    randghost = random.randint(0,23)
    await ctx.respond(f"Ghost is: {ghosts[randghost]}")

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
async def russianroulette(ctx, extra1: str = "none", extra2: str = "none"):
    await ctx.defer()
    user = ctx.author
    bullet_spot = random.randint(1, 6)
    chamber = 1
    shot = False
    players = 0
    if extra1 != "none" and extra2 != "none":
        players = 3
    elif extra1 != "none":
        players = 2
    elif extra1 == "none" and extra2 == "none":
        players = 1
    while not shot:
        if shot:
            break
        if players >= 1:
            if chamber == bullet_spot:
                await ctx.send(f'💥🔫 BANG! {user.mention} lost!')
                shot = True
            else:
                await ctx.send(f"💨🔫 *click*... {user.mention} survived! 🔥")
            chamber += 1
        if shot:
            break
        if players >= 2:
            if chamber == bullet_spot:
                await ctx.send(f'💥🔫 BANG! {extra1} lost!')
                shot = True
            else:
                await ctx.send(f"💨🔫 *click*... {extra1} survived! 🔥")
            chamber += 1
        if shot:
            break
        if players >= 3:
            if chamber == bullet_spot:
                await ctx.send(f'💥🔫 BANG! {extra2} lost!')
                shot = True
            else:
                await ctx.send(f"💨🔫 *click*... {extra2} survived! 🔥")
            chamber += 1
        if chamber == bullet_spot:
            await ctx.send(f'💥🔫 BANG! Bot lost!')
            shot = True
        else:
            await ctx.send(f"💨🔫 *click*... Bot survived! 🔥")
        chamber += 1

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

# Run the bot
bot.run("")