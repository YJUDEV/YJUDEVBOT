# discord 라이브러리 사용 선언
import discord
import time

client = discord.Client()

token_file = open("C:\\Users\\yju08\\OneDrive\\동기화폴더\\서버용폴더\\YJUDEVBOT\\private\\token.txt",encoding="utf-8")
token = token_file.read()
token_file.close()

discord_ids = {"398355473734172682":"김규민","391812113137532928":"엄지형","382763839197806613":"김우현","378764435453378561":"임정욱","380369355449303041":"이진욱","279822843238285312":"황건우","436430855515144204":"원석환"}


# 프로그램이 처음 실행되었을 때 초기 구성
@client.event
async def on_ready():
    print("YJUDEVBOT을 시작합니다")
    print(time.strftime('%Y-%m-%d', time.localtime(time.time())))
    print("===========")

    await client.change_presence(status=discord.Status.online, activity=discord.Game("/명령어를 입력하세요"))


# 봇에 메시지가 오면 수행 될 액션
@client.event
async def on_message(message):
    #봇이 보낸 메시지면 반응 안함
    if message.author.bot:
        return None


    if message.content == "/명령어":

        channel = message.channel

        embed = discord.Embed(title="명령어 안내", description="",color=0x5CD1E5)
        embed.add_field(name="/성적", value="DM으로 성적을 안내해드려요", inline=False)
        embed.add_field(name="/성적공개", value="서버 메시지로 성적을 안내해드려요", inline=False)

        await channel.send(embed=embed)


    if message.content == "/성적":
        
        #dm채널이 있으며 그대로 사용, 없으면 만들기
        if message.author.dm_channel:
            channel = message.author.dm_channel
        elif message.author.dm_channel is None:
            channel = await message.author.create_dm()

        name = discord_ids[str(message.author.id)]

        #외부인 처리
        if name == "김우현" or name == "원석환":
            channel.send("외부인은 사용이 불가능합니다")
            return None

        score_file = open("C:\\Users\\yju08\\OneDrive\\동기화폴더\\서버용폴더\\YJUDEVBOT\\score\\{}.txt".format(name),encoding="utf-8")
        score = score_file.read()
        score_file.close()

        embed = discord.Embed(title="{}님의 성적안내".format(name), description=score,color=0x5CD1E5)

        await channel.send(embed=embed)


    if message.content == "/성적공개":

        channel = message.channel
        name = discord_ids[str(message.author.id)]

        #외부인 처리
        if name == "김우현" or name == "원석환":
            channel.send("외부인은 사용이 불가능합니다")
            return None

        score_file = open("C:\\Users\\yju08\\OneDrive\\동기화폴더\\서버용폴더\\YJUDEVBOT\\score\\{}.txt".format(name),encoding="utf-8")
        score = score_file.read()
        score_file.close()

        embed = discord.Embed(title="{}님의 성적안내".format(name), description=score,color=0x5CD1E5)

        await channel.send(embed=embed)






client.run(token)