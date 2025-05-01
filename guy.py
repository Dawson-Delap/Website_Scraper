import discord
import random
import asyncio
import datetime

# Set intents and initialize bot
intents = discord.Intents.default()
bot = discord.Bot(intents=intents)
allowed_mentions=discord.AllowedMentions(everyone=True)
@bot.event
async def on_message(message):
    respond = random.randint(0,100)
    if respond == 34:
        whatPic = random.randint(0,5)
        if whatPic == 0:
            await message.channel.send(f"https://tenor.com/view/flightreacts-flight-spin-flight-driving-driving-gif-14821482636596098762")
        elif whatPic == 1:
            await message.channel.send(f"https://tenor.com/view/flight-waffle-house-waffle-house-flightreacts-gif-291001867069513835")
        elif whatPic == 2:
            await message.channel.send(f"https://tenor.com/view/flight-shoe-gif-1842982099687274858")
        elif whatPic == 3:
            await message.channel.send(f"https://tenor.com/view/yh-gif-25406060")
        elif whatPic == 4:
            await message.channel.send(f"https://tenor.com/view/nerd-emoji-nerd-emoji-avalon-play-avalon-gif-24241051")
        elif whatPic == 5:
            await message.channel.send(f"https://tenor.com/view/low-tier-god-awesome-mario-twerking-gif-23644561")
            
            
    # Don't respond to ourselves
    if message.author == bot.user:
        return
    if message.author.id == 810679946670112768 or message.author.id == 832086256350789642:
        # Check if the message is inside a guild (server)
        if message.guild:
            try:
                # Timeout the user for 5 minutes (300 seconds)
                timeout_duration = datetime.timedelta(minutes=1)

                await message.author.timeout_for(timeout_duration)

                await message.channel.send(
                    f"KYS {message.author.mention}"
                )

            except discord.Forbidden:
                await message.channel.send("I don't have permission to timeout this user!")
            except Exception as e:
                await message.channel.send(f"Error: {e}")
    if message.author.id == 984333768976367726:
        message.channel.send("@everyone Logan Has Returned!!!")
    # Check if the bot is mentioned
    if bot.user in message.mentions:
        await message.channel.send(f"KYS {message.author.mention}")
        whatPic = random.randint(0,5)
        if whatPic == 0:
            await message.channel.send(f"https://tenor.com/view/flightreacts-flight-spin-flight-driving-driving-gif-14821482636596098762")
        elif whatPic == 1:
            await message.channel.send(f"https://tenor.com/view/flight-waffle-house-waffle-house-flightreacts-gif-291001867069513835")
        elif whatPic == 2:
            await message.channel.send(f"https://tenor.com/view/flight-shoe-gif-1842982099687274858")
        elif whatPic == 3:
            await message.channel.send(f"https://tenor.com/view/yh-gif-25406060")
        elif whatPic == 4:
            await message.channel.send(f"https://tenor.com/view/nerd-emoji-nerd-emoji-avalon-play-avalon-gif-24241051")
        elif whatPic == 5:
            await message.channel.send(f"https://tenor.com/view/low-tier-god-awesome-mario-twerking-gif-23644561")
            
    
    

# Initialize streaks and money
streaks = {}
money = {}
voice_channel = bot.get_channel(1353827847818711050)
@bot.slash_command(description="laugh")
async def vc(ctx, newvc: str = 1353827847818711050):
    global voice_channel
    newvc = int(newvc)
    print(newvc)
    #1365410616113889335
    voice_channel = bot.get_channel(newvc)
    await ctx.respond(f"Changed vc to {voice_channel}", ephemeral=True)
@bot.slash_command(description="low tier god")
async def kys(ctx):
    global voice_channel
    try:
        vc = await voice_channel.connect()
        vc.play(discord.FFmpegPCMAudio("Now.mp3"))
        while vc.is_playing():
            await asyncio.sleep(2)

        await vc.disconnect()
        await ctx.respond(f"played sound", ephemeral=True)

    except discord.ClientException as e:
        await ctx.followup.send(f"Error: {e}", ephemeral=True)


@bot.slash_command(description="laugh")
async def laugh(ctx):
    global voice_channel
    try:
        vc = await voice_channel.connect()
        vc.play(discord.FFmpegPCMAudio("goof.mp3"))
        while vc.is_playing():
            await asyncio.sleep(2)

        await vc.disconnect()
        await ctx.respond(f"played sound", ephemeral=True)

    except discord.ClientException as e:
        await ctx.followup.send(f"Error: {e}", ephemeral=True)

@bot.slash_command(description="adlib")
async def ahh(ctx):
    global voice_channel
    try:
        vc = await voice_channel.connect()
        vc.play(discord.FFmpegPCMAudio("AHH Adlib.mp3"))
        while vc.is_playing():
            await asyncio.sleep(2)

        await vc.disconnect()
        await ctx.respond(f"played sound", ephemeral=True)

    except discord.ClientException as e:
        await ctx.followup.send(f"Error: {e}", ephemeral=True)
@bot.slash_command(description="random")
async def ranplay(ctx):
    global voice_channel
    ranSound = random.randint(0,5)
    try:
        vc = await voice_channel.connect()
        if ranSound == 0:
            vc.play(discord.FFmpegPCMAudio("Now.mp3"))
        if ranSound == 1:
            vc.play(discord.FFmpegPCMAudio("goof.mp3"))
        if ranSound == 2:
            vc.play(discord.FFmpegPCMAudio("Ghost.mp3"))
        if ranSound == 3:
            vc.play(discord.FFmpegPCMAudio("Kenny Scream.mp3"))
        if ranSound == 4:
            vc.play(discord.FFmpegPCMAudio("Speed.mp3"))
        if ranSound == 5:
            vc.play(discord.FFmpegPCMAudio("AHH adlib.mp3"))
        while vc.is_playing():
            await asyncio.sleep(2)

        await vc.disconnect()
        await ctx.respond(f"played sound", ephemeral=True)

    except discord.ClientException as e:
        await ctx.followup.send(f"Error: {e}", ephemeral=True)


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