import discord
from discord.ext.commands import Bot
from discord_components import DiscordComponents, Button
import random
import asyncio
from discord.utils import get

bot = Bot(command_prefix = "!")

bot.remove_command('help')

token = '토큰'

@bot.event
async def on_ready():
    DiscordComponents(bot)
    print(f"{bot.user}로 로그인 완료!")

@bot.command()
async def 인증(ctx):
    try:
        member = ctx.message.author

        rol = discord.utils.get(ctx.guild.roles, name="역 할 이 름")
        if rol in member.roles:
            pass
        else:
            def check(res):
                return ctx.author == res.user and res.channel == ctx.channel 
        
            emojis = ["💌", "🎶", "🥰", "💀", "🚫", "🔞", "👏", "✅", "✝", "⭕", "☢", "😆", "😑", "😊", "🎁", "🤣", "😂", "🍙", "🧨", "🎫", "🥽", "✨", "🎇", "🎆", "🎈", "🎃", "🎉", "🧧"]
            a = random.choice(emojis)
            b = random.choice(emojis)
            ran = random.randint(1, 2)
            while a == b:
                a = random.choice(emojis)
                b = random.choice(emojis)
            if ran == 1:
                asdf = a
                asdf2 = b
            if ran == 2:
                asdf = b
                asdf2 = a
            embed = discord.Embed(title='🌍 인증하기', description=f'이 버튼을 15초 안에 눌러주세요. ({a})', colour=discord.Colour.blue())
            embed2 = discord.Embed(title='✅ 인증성공', description=f'{ctx.author.mention}, 3초 뒤 역할이 지급됩니다.', colour=discord.Colour.green())
            embed3 = discord.Embed(title='⛔ 인증실패', description=f'{ctx.author.mention}, 잘못된 버튼입니다. 다시 시도해주세요.', colour=discord.Colour.red())
            embed4 = discord.Embed(title='⛔ 인증실패', description=f'{ctx.author.mention}, 시간 초과입니다. 다시 시도해주세요.', colour=discord.Colour.red())

            await ctx.send(
                embed=embed,
                components = [
                    Button(style = 1, label = asdf), Button(style = 3, label = asdf2)
                ]
            )

            res = await bot.wait_for("button_click", check = check, timeout=15)
            u = res.component.label

            if u == a:
                await res.respond(embed = embed2)
                await asyncio.sleep(3)
                await ctx.channel.purge(limit=2)
                await member.add_roles(rol)
            elif u == b:
                await res.respond(embed = embed3)
                await asyncio.sleep(3)
                await ctx.channel.purge(limit=2)

    except:
        await ctx.channel.purge(limit=2)
        await ctx.send(embed=embed4)
        await asyncio.sleep(3)
        await ctx.channel.purge(limit=1)


bot.run(token)
