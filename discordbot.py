import discord
import googletrans
import os
from pprint import pprint
# 輸入自己Bot的TOKEN碼
TOKEN = os.environ['MTA4OTc5MTkyMjY2MDQ0NjI2OA.G2irjp.5itnM4edBbOy4lNaUofyjXRLb8Hig6_2Z9gAZM']
SRCLanguage=os.environ['']
DSTLanguage=os.environ['zh-TW']

client = discord.Client()

# 起動時呼叫
@client.event
async def on_ready():
    print('成功登入')

# 收到訊息時呼叫
@client.event
async def on_message(message):
    # 送信者為Bot時無視
    if message.author.bot:
        return
    
    if client.user in message.mentions: # @判定
        translator = googletrans.Translator()
        robotName = client.user.name
        first, space, content = message.clean_content.partition('@'+robotName+' ')
        
        if content == '':
            content = first
        if translator.detect(content).lang == DSTLanguage:
            return
        if translator.detect(content).lang == SRCLanguage or SRCLanguage == '':
            remessage = translator.translate(content, dest='zh-tw').text
            await message.reply(remessage) 

# Bot起動
client.run(TOKEN)
