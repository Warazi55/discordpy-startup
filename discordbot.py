from discord.ext import commands
from os import getenv
import traceback

bot = commands.Bot(command_prefix='/')


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
        if re.search(r'おみくじ',message.content):
       num = random.randint(0,60)
       if num < 2:
           await message.channel.send("大吉！")
           print(message.id) #メッセージのid
           print(message.content) #メッセージのcntent
       elif 2 <= num < 10:
           await message.channel.send("中吉！")
           print(message.id) #メッセージのid
           print(message.content) #メッセージのcntent
       elif 10 <= num < 20:
           await message.channel.send("小吉！")
           print(message.id) #メッセージのid
           print(message.content) #メッセージのcntent
       elif 20 <= num < 40:
           await message.channel.send("吉！")
           print(message.id) #メッセージのid
           print(message.content) #メッセージのcntent
       elif 40 <= num < 50:
           await message.channel.send("末吉！")
           print(message.id) #メッセージのid
           print(message.content) #メッセージのcntent
       elif 50 <= num < 55:
           await message.channel.send("凶！")
           print(message.id) #メッセージのid
           print(message.content) #メッセージのcntent
       elif 55 <= num < 58:
           await message.channel.send("中凶！")
           print(message.id) #メッセージのid
           print(message.content) #メッセージのcntent
       else:
           await message.channel.send("大凶！")
           print(message.id) #メッセージのid
           print(message.content) #メッセージのcntent

    
@bot.command()
async def ping(ctx):
    await ctx.send('ﾎﾟｵｵｵｵﾝ!!!!')    
    
token = getenv('DISCORD_BOT_TOKEN')
bot.run(token)
