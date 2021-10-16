from discord.ext import commands
from os import getenv
import traceback
from discord.ext import tasks
from datetime import datetime, timedelta
import re
import random 
import time
from time import sleep
import threading

bot = commands.Bot(command_prefix='/')

# 接続に必要なオブジェクトを生成
client = discord.Client()
            
# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')
    
# 返信する非同期関数を定義
async def reply(message):
    reply = f'{message.author.mention} 呼んだ？^^' # 返信メッセージの作成
    await message.channel.send(reply) # 返信メッセージを送信
   

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

    
token = getenv('DISCORD_BOT_TOKEN')
bot.run(token)
