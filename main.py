import asyncio, discord
from discord.ext import commands
import random

Token = "NjM5MTgxODc1NDkxMTEwOTIy.Xbnigg.AhP-1c-gPnlBrXeEvFkrLwOO4EU"

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='김민 ', intents=intents)

@bot.event
async def on_ready():
    print('We have logged in as', bot.user)

@bot.command(aliases=['도와줘', '안녕', 'ㅎㅇ', '안녕하세요', '하이'])
async def hello(ctx):
    await ctx.reply('안녕, 나는 김민 봇\n 명령어를 알고싶으면 \'김민 명령어\'\n')

@bot.command(aliases=['명령어'])
async def commands(ctx):
    embed = discord.Embed(title="김민봇의 명령어", description="다음과 같습니다", color=0xc11e1e)
    embed.set_thumbnail(url="https://imgnn.seoul.co.kr/img/upload/2016/09/05/SSI_20160905144252_V.jpg")
    embed.add_field(name="1. 로또", value="로또번호 뽑기 기능: 1부터 45까지의 숫자중 6개의 숫자를 골라줍니다.", inline=False)
    embed.add_field(name="2 가위바위보", value="가위바위보 게임입니다. ```  김민 가위바위보 가위  ``` 의 형식으로 사용합니다", inline=False)
    await ctx.send(embed=embed)

@bot.command(aliases=['ㅗ', 'ㅗㅗ', 'ㅄ', 'ㅂㅅ', '병신', '시발'])
async def yeot(ctx):
    rudewords = ['시발아', '사발련아', '족까', 'ㅗ', '개시기야', '돌았나','뭐고 이 잡종은','여물어','개마을래 ㅋㅋ','엿 쳐무라 ㅋㅋ','꼬라박아',
                 '어디 맞을래??','혼내줄까','뭔데 이 bitch는','야이 개센치야','야이 십센치야','콱 토미 간식으로 던져줘뿌까','일단 조무래기는 빠지고ㅋㅋ','콱 씨 ㅋㅋ','몇긴데??','뒤질래??']
    for i in range(5):
        randrude = random.choice(rudewords)
        await ctx.send("{} {}".format(ctx.author.mention, randrude))

    await asyncio.sleep(3)

    await ctx.send("ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ {}아 끝난줄 알았지 ㅋㅋㅋㅋ".format(ctx.author.mention))
    for i in range(3):
        randrude = random.choice(rudewords)
        await ctx.send("{} {}".format(ctx.author.mention, randrude))

@bot.command(name='로또')
async def lotto(ctx):
    num_list = []
    win_num_list = []
    for i in range(5):
        for i in range(1, 46):
            num_list.append(i)
        win_list = []
        for i in range(0, 6):
            r_seed = random.randrange(0, len(num_list))
            win_num = num_list.pop(r_seed)
            win_list.append(win_num)
        win_list.sort()
        win_num_list.append(win_list)

    await asyncio.sleep(0.5)
    await ctx.send("음... 어디보자~ . .")
    await asyncio.sleep(3)
    await ctx.send("아 이번호는 **무조건**이지ㅋㅋㅋ")
    await asyncio.sleep(2)
    await ctx.send("이거면 되겠다 ㅋㅋ")
    await asyncio.sleep(3)
    embed = discord.Embed(title="자~ 받아 적어라잉ㅋㅋ", description='====================', color=0xc11e1e)
    embed.set_thumbnail(url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRgvlSVOUXawKLaH1bw_XjLjdl_CTB1Vq541A&usqp=CAU')
    embed.add_field(name='{}'.format(win_num_list[0]), value='====================', inline=False)
    embed.add_field(name='{}'.format(win_num_list[1]), value='====================', inline=False)
    embed.add_field(name='{}'.format(win_num_list[2]), value='====================', inline=False)
    embed.add_field(name='{}'.format(win_num_list[3]), value='====================', inline=False)
    embed.add_field(name='{}'.format(win_num_list[4]), value='====================', inline=False)
    embed.add_field(name='이건 무조건인데', value='당첨금으로 뭐 할지 생각해둬라 ㅋㅋ 안되면 말고 ㅋㅋ', inline=False)
    await ctx.send(embed=embed)

@bot.command(name='가위바위보')
async def gameRPS(ctx, player):
    computer = random.choice(['가위', '바위', '보'])
    if computer == '가위':
        await ctx.send('컴퓨터는 가위를 냈습니다.')
        if player == '가위':
            await ctx.send('플레이어는 가위를 냈습니다.')
            await asyncio.sleep(0.5)
            await ctx.send('```무승부```')
        elif player == '바위':
            await ctx.send('플레이어는 바위를 냈습니다.')
            await asyncio.sleep(0.5)
            await ctx.send('```플레이어 승리```')
        elif player == '보':
            await ctx.send('플레이어는 보를 냈습니다.')
            await asyncio.sleep(0.5)
            await ctx.send('```컴퓨터 승리```')
    elif computer == '바위':
        await ctx.send('컴퓨터는 바위를 냈습니다.')
        if player == '가위':
            await ctx.send('플레이어는 가위를 냈습니다.')
            await asyncio.sleep(0.5)
            await ctx.send('```컴퓨터 승리```')
        elif player == '바위':
            await ctx.send('플레이어는 바위를 냈습니다.')
            await asyncio.sleep(0.5)
            await ctx.send('```무승부```')
        elif player == '보':
            await ctx.send('플레이어는 보를 냈습니다.')
            await asyncio.sleep(0.5)
            await ctx.send('```플레이어 승리```')
    elif computer == '보':
        await ctx.send('컴퓨터는 보를 냈습니다.')
        if player == '가위':
            await ctx.send('플레이어는 가위를 냈습니다.')
            await asyncio.sleep(0.5)
            await ctx.send('```플레이어 승리```')
        elif player == '바위':
            await ctx.send('플레이어는 바위를 냈습니다.')
            await asyncio.sleep(0.5)
            await ctx.send('```컴퓨터 승리```')
        elif player == '보':
            await ctx.send('플레이어는 보를 냈습니다.')
            await asyncio.sleep(0.5)
            await ctx.send('```무승부```')

bot.run(Token)