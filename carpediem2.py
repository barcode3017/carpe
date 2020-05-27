# -*- coding:utf-8 -*- 


import discord, asyncio, time, random, re
from discord.utils import get
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions

token = "NzE0NDA5NDkyMzc2MzIyMTE5.XsuQXg.Bupgoe0esetJnPzEc2oC-jCefj8"
client = discord.Client()

badwords = ["ㅄ", "ㅂㅅ", "불알", "부랄", "ㅅㅂ", "ㅅㄲ", "ㅆㅂ", "시발", "씨발", "병신","좆", "보지", "자지", "느금마", "걸레", "창년", "ㅈ같네", "자위", "걸레년", "보지년", "애미", "느금", "발기","씨1발", "시1발", "개1새끼", "자1지", "보1지", "뒤졌어", "새끼", "개간나", "간나", "개년", "개돼지", "개지랄", "느개비", "닥쳐", "똘추", "등신", "미친년", "보추", "썩을년", "썩을놈", "씹년", "씹창", "존나","후장", "한남"]


@client.event
async def on_ready(): 
  await client.change_presence(status=discord.Status.online, activity=discord.Game("봇 사용 명령어 >> !명령어 <<"))
  async def bt(games):
    await client.wait_until_ready()

    while not client.is_closed():
        for g in games:
            await client.change_presence(status = discord.Status.online, activity = discord.Game(g))
            await asyncio.sleep(15)
  print("[ Bot Start ] \n-- 봇이 시작되었습니다 -- \n봇 제작자 : 바코드 #1741\n")
  print(("""[ Bot Info ]\n[1] Bot Name : {} \n[2] Bot Discord ID : {}""").format(client.user.name, client.user.id))
  await bt(['제작자 : 바코드#1741', '>> !명령어 <<', 'CarpeDiem'])

  
@client.event
async def on_message(message): 
  if message.author.bot: 
    return None
  

  if message.content.startswith('!이모티콘'):

    emoji = [" ꒰⑅ᵕ༚ᵕ꒱ ", " ꒰◍ˊ◡ˋ꒱ ", " ⁽⁽◝꒰ ˙ ꒳ ˙ ꒱◜⁾⁾ ", " ༼ つ ◕_◕ ༽つ ", " ⋌༼ •̀ ⌂ •́ ༽⋋ ",
                 " ( ･ิᴥ･ิ) ", " •ө• ", " ค^•ﻌ•^ค ", " つ╹㉦╹)つ ", " ◕ܫ◕ ", " ᶘ ͡°ᴥ͡°ᶅ ", " ( ؕؔʘ̥̥̥̥ ه ؔؕʘ̥̥̥̥ ) ",
                 " ( •́ ̯•̀ ) ",
                 " •̀.̫•́✧ ", " '͡•_'͡• ", " (΄◞ิ౪◟ิ‵) ", " ˵¯͒ བ¯͒˵ ", " ͡° ͜ʖ ͡° ", " ͡~ ͜ʖ ͡° ", " (づ｡◕‿‿◕｡)づ ",
                 " ´_ゝ` ", " ٩(͡◕_͡◕ ", " ⁄(⁄ ⁄•⁄ω⁄•⁄ ⁄)⁄ ", " ٩(͡ï_͡ï☂ ", " ௐ ", " (´･ʖ̫･`) ", " ε⌯(ง ˙ω˙)ว ",
                 " (っ˘ڡ˘ς) ", "●▅▇█▇▆▅▄▇", "╋╋◀", "︻╦̵̵̿╤──", "ー═┻┳︻▄", "︻╦̵̵͇̿̿̿̿══╤─",
                 " ጿ ኈ ቼ ዽ ጿ ኈ ቼ ዽ ጿ ", "∑◙█▇▆▅▄▃▂", " ♋♉♋ ", " (๑╹ω╹๑) ", " (╯°□°）╯︵ ┻━┻ ",
                 " (///▽///) ", " σ(oдolll) ", " 【o´ﾟ□ﾟ`o】 ", " ＼(^o^)／ ", " (◕‿‿◕｡) ", " ･ᴥ･ ", " ꈍ﹃ꈍ ", " ˃̣̣̣̣̣̣︿˂̣̣̣̣̣̣ ",
                 " ( ◍•㉦•◍ ) ", " (｡ì_í｡) ", " (╭•̀ﮧ •́╮) ", " ଘ(੭*ˊᵕˋ)੭ ", " ´_ゝ` ", " (~˘▾˘)~ "] # 이모티콘 배열입니다.
        
    randomNum = random.randrange(0, len(emoji)) 
    
    
    embed = discord.Embed(title="Random Emoji", description="{}".format(emoji[randomNum]), color=0x000000)
    embed.set_footer(text="Bot Made by. 바코드 #1741", icon_url="https://media.discordapp.net/attachments/703908401381376000/714396047102967849/2.png")
    await message.channel.send(embed=embed)



  if message.content == ('!전체청소'):
    i2 = message.author.guild_permissions.administrator
    if i2 is False:
      embed = discord.Embed(title="당신은 관리자가 아닙니다", description="이 명령어는 최고 관리자 이상만 사용 가능합니다", color=0xff0000)
      embed.set_footer(text="Bot Made by. 바코드 #1741", icon_url="https://discordapp.com/channels/691615852620939274/703908401381376000/711859989177958410")
      await message.channel.send(embed=embed)
    
    if i2 is True:
      await message.channel.purge(limit=99)
      await message.channel.send('최근 메시지 기록들을 모두 삭제 하고 있습니다...')
      await message.channel.purge(limit=1)
      embed = discord.Embed(title="메시지 삭제 알림", description="최근 디스코드 채팅 99개가\n관리자 {}님의 요청으로 인해 정상 삭제 조치 되었습니다".format(message.author), color=0x000000)
      embed.set_footer(text="Bot Made by. 바코드 #1741", icon_url="https://discordapp.com/channels/691615852620939274/703908401381376000/711859989177958410")
      await message.channel.send(embed=embed)
  
  
  if message.content == ('!전체삭제'):
    i2 = message.author.guild_permissions.administrator
    if i2 is False:
      embed = discord.Embed(title="당신은 관리자가 아닙니다", description="이 명령어는 최고 관리자 이상만 사용 가능합니다", color=0xff0000)
      embed.set_footer(text="Bot Made by. 바코드 #1741", icon_url="https://discordapp.com/channels/691615852620939274/703908401381376000/711859989177958410")
      await message.channel.send(embed=embed)
    
    if i2 is True:
      await message.channel.purge(limit=99)
      await message.channel.send('최근 메시지 기록들을 모두 삭제 하고 있습니다...')
      await message.channel.purge(limit=1)
      embed = discord.Embed(title="메시지 삭제 알림", description="최근 디스코드 채팅 99개가\n관리자 {}님의 요청으로 인해 정상 삭제 조치 되었습니다".format(message.author), color=0x000000)
      embed.set_footer(text="Bot Made by. 바코드 #1741", icon_url="https://discordapp.com/channels/691615852620939274/703908401381376000/711859989177958410")
      await message.channel.send(embed=embed)
  

  if message.content.startswith('!타이머'):

    Text = ""
    learn = message.content.split(" ")
    vrsize = len(learn)  
    vrsize = int(vrsize)
    for i in range(1, vrsize): 
      Text = Text + " " + learn[i]

      sec = int(Text)


      for i in range(sec, 0, -1):
          embed = discord.Embed(title="Timer", description="타이머가 작동중 입니다\n현재 남은 시간 : {}".format(str(i)+'초'), color=0x00ff79)
          embed.set_footer(text="Bot Made by. 바코드 #1741", icon_url="https://media.discordapp.net/attachments/703908401381376000/714396047102967849/2.png")
          await message.author.send(embed=embed)
          await asyncio.sleep(1)


      else:
          embed = discord.Embed(title="Timer", description="정해진 시간이 되었습니다!\n타이머 구동을 마칩니다", color=0xff0000)
          embed.set_footer(text="Bot Made by. 바코드 #1741", icon_url="https://media.discordapp.net/attachments/703908401381376000/714396047102967849/2.png")
          await message.author.send(embed=embed)


  if message.content == "!관리진":
    commander = discord.utils.get(message.guild.roles, name="Commander")
    await message.channel.send("{}\n카르페디엠 관리진 목록을 DM으로 보내드렸습니다\n**관리진을 사칭하는 경우 최대 밴 조치까지 가능하니 주의 부탁드립니다.**".format(commander.mention))
    embed = discord.Embed(title="Carpediem 관리진 명단", description="[1] 최고관리자 : 서버 총 관리 및 개발 담당\n[2] 인게임관리자 : 인게임 관리 담당\n[3] 개발자 : 서버 개발담당", color=0xff6c6c)
    embed.add_field(name="``[1] 서버 총괄 관리자 ( 최고관리자 )``", value="CarpeDiem (1), Coy (2)", inline=False)
    embed.add_field(name="``[2] 인게임 관리자``", value="D I O R (11), 데레츤 (13), 바코드 (20)", inline=False)
    embed.add_field(name="``[3] 개발자``", value="BLEAN (11833)", inline=False)
    embed.set_footer(text="Bot Made by. 바코드 #1741", icon_url="https://media.discordapp.net/attachments/703908401381376000/714396047102967849/2.png")
    await message.author.send(embed=embed)

  if message.content == "!디코":
    await message.channel.send("<< 카르페디엠 서버 디스코드 주소 >>\nhttps://discord.gg/UGAA489")

  if message.content == "!뉴비":
    await message.channel.purge(limit=1)
    await message.channel.send("뉴비 관련 내용을 DM으로 전송해드렸습니다!")
    embed = discord.Embed(title="Carpediem 뉴비 매뉴얼", description="잘 모르시겠는 정보가 있으시다면 아래 내용을 따라주세요!\n인게임 : K - 관리 - 도우미 호출 이용\n디스코드 : 질문 답변 채널 이용", color=0x00ff82)
    embed.add_field(name="``[1] 교육 이수 (지원금 지급)``", value="RP가 처음이시거나, 관련 지식을 모르시는 분이시라면, 뉴비 교육 이수 해주세요!\n( 교육 이수 신청방법 : 디스코드 '뉴비 교육 이수 신청'란에 양식에 맞게 작성 )", inline=False)
    embed.add_field(name="``[2] 직업선택``", value="처음 스폰 되는 장소인 '시청'에서 직업을 발급받은 뒤,\n자신이 선택한 직업을 직업 안내를 보고 직업에 맞는 일을 해주세요!", inline=False)
    embed.add_field(name="``[3] 다양한 RP 즐기기``", value="폭주RP, 도주RP, 차량 도난RP, 은행RP, 보석상 RP 등 RP는 무궁무진합니다!\n유저분이 하고 싶은 RP를 즐겨주세요!\n( 서버 헌법과 보호구역을 반드시 읽어보고, 숙지하신 뒤, 즐겨주시기 바랍니다 )", inline=False)
    embed.set_footer(text="Bot Made by. 바코드 #1741", icon_url="https://media.discordapp.net/attachments/703908401381376000/714396047102967849/2.png")
    await message.author.send(embed=embed)
      
  if message.content == "!채팅":
    await message.channel.purge(limit=1)
    await message.channel.send("채팅 관련 내용을 DM으로 전송해드렸습니다!")
    embed = discord.Embed(title="Carpediem 채팅 관련 지식", description="-- 아래 사항은 기초 채팅 지식으로, 정확한 지식을 알아보려면, 뉴비 교육을 이수해 주시기 바랍니다 --", color=0xff00a0)
    embed.add_field(name="``OOC (Out of character)``", value="현실과 관련된 내용(RP와 관계없는 내용)을 채팅으로 말할 때 사용됩니다\n( ex 오늘 미세먼지가 많네요, 밥 드셨어요? )\n\n명령어 사용방법 : /ooc(원거리) & /oo(근거리)", inline=False)
    embed.add_field(name="``IC(In game Character)``", value="인 게임(RP)와 관련 있는 내용을 채팅으로 말할 때 사용됩니다\n( ex 차 살려는데 어디 계시나요? )\n\n명령어 사용방법 : /sns(원거리)\n\nIC사항에서의 메타 게이밍, 죽었을 때 사용하는 것은 금지되어 있습니다\n( 메타 게이밍 : 현실에서 발음하지 않는 자음이나 모음 )", inline=False)
    embed.set_footer(text="Bot Made by. 바코드 #1741", icon_url="https://media.discordapp.net/attachments/703908401381376000/714396047102967849/2.png")
    await message.author.send(embed=embed)
  
  if message.content == "!RP":
    await message.channel.purge(limit=1)
    await message.channel.send("RP 관련 내용을 DM으로 전송해드렸습니다!")
    embed = discord.Embed(title="Carpediem RP 관련 지식", description="-- 아래 사항은 기초 RP 지식으로, 정확한 지식을 알아보려면, 서버 헌법을 참고해 주시기 바랍니다 --", color=0xfdff00)
    embed.add_field(name="``RP ( Role playing )``", value="Role playing의 약자로 역할연기를 뜻하는 단어로써, 특정 역할을 맡거나 직업을 선택한 후 그 역할에 따라 현실에 맞게 플레이하는 것을 뜻한다\n( ex 밥 먹기, 운전하기 등 )", inline=False)
    embed.add_field(name="``Non-RP``", value="RP의 반대말로, 현실에서 행할 수 없는 행동을 하거나, 서버헌법에서 지정한 논RP를 말한다 ( ex 불법 프로그램 사용, 무차별 살인 )", inline=False)
    embed.add_field(name="``Bad-RP``", value="모순된 RP로써, 현실에서 가능하지 않고, 게임에서 가능한 행위\n( ex 사람을 죽였다 살렸다 하는 행위를 여러 번 하는 것 )", inline=False)
    embed.set_footer(text="Bot Made by. 바코드 #1741", icon_url="https://media.discordapp.net/attachments/703908401381376000/714396047102967849/2.png")
    await message.author.send(embed=embed)

  if message.content == "!명령어":
    await message.channel.purge(limit=1)
    await message.channel.send("명령어 관련 내용을 DM으로 전송해드렸습니다!")
    embed = discord.Embed(title="Carpediem 명령어 목록", description="디스코드 봇이 작동하는 명령어를 알려드립니다", color=0x62c1cc)
    embed.add_field(name="――――――――――――――――――――――――――――――――――", value="[1] 서버 기본 자료\n서버 정보들을 알려주는 명령어들 입니다", inline=False)
    embed.add_field(name="``!관리진``", value="서버 관리진분들을 알려드립니다", inline=True)
    embed.add_field(name="``!디코``", value="디스코드 주소를 알려드립니다", inline=True)
    embed.add_field(name="――――――――――――――――――――――――――――――――――", value="[2] 서버 튜토리얼\n뉴비분들은 서버 튜토리얼 내용들을 숙지하고 플레이 부탁드립니다!", inline=False)
    embed.add_field(name="``!뉴비``", value="DM으로 뉴비에게 필요한 정보들을 알려드립니다", inline=True)
    embed.add_field(name="``!채팅``", value="OOC와 IC관련 내용들과 정보를 알려드립니다", inline=True)
    embed.add_field(name="``!RP``", value="RP에 대한 정보들을\n알려드립니다", inline=True)
    embed.add_field(name="――――――――――――――――――――――――――――――――――", value="[3] 기타 명령어\n편리함을 더해주는 명령어들 입니다", inline=False)
    embed.add_field(name="``!더해줘``", value="!더해줘 [A] [B]를 입력했을 시,\nA와 B를 더해줍니다", inline=True)
    embed.add_field(name="``!타이머``", value="!타이머 [A]를 입력했을 시\n[A]초를 DM으로 카운트 해줍니다", inline=True)
    embed.set_footer(text="Bot Made by. 바코드 #1741 | Bot ver : 1.0", icon_url="https://media.discordapp.net/attachments/703908401381376000/714396047102967849/2.png")
    await message.author.send(embed=embed)


 
  if message.content.startswith("!더해줘"):
    params_str = message.content.split(' ')
    params = []
    for param_str in params_str:
        if param_str.isdigit():
            params.append(int(param_str))

    result = 0
    for param in params:
        result += param
    await message.channel.send("계산 결과는 {result} 입니다.".format(result=result))
  
  for word in badwords:
    bw = (word)
    if message.content.count(word) > 0:
        print("\n욕설이 감지되어 삭제처리 되었습니다.\n욕설 사용자 ID : {}\n욕설 사용자 닉네임 : {}\n".format(message.author.id, message.author))
        await message.channel.purge(limit=1)
        
        channel = client.get_channel(697456423751385089)
        embed = discord.Embed(title="욕설이 감지되었습니다", description="아래는 욕설 사용자에 대한 정보입니다.\n관리자 채널과 사용 유저에게 DM이 전송 완료 되었습니다.", color=0xff0000)
        embed.add_field(name="――――――――――――――――――――――――――――――――――", value="욕설 사용자 정보", inline=False)
        embed.add_field(name="``이용자 디스코드 ID``", value="ID : {}".format(message.author.id), inline=True)
        embed.add_field(name="``이용자 디스코드 닉네임``", value="NickName : {}".format(message.author), inline=True)
        embed.add_field(name="――――――――――――――――――――――――――――――――――", value="욕설 사용 정보", inline=False)
        embed.add_field(name="``이용자 사용 단어``", value="Word : {}".format(bw), inline=True)
        embed.add_field(name="``이용자 욕설 사용 채널``", value="Channel : {}".format(message.channel), inline=True)
        embed.set_footer(text="Bot Made by. 바코드 #1741 | Bad word detection Support by. MOS 엘크님", icon_url="https://media.discordapp.net/attachments/703908401381376000/714396047102967849/2.png")
        await channel.send (embed=embed)

        embed = discord.Embed(title="욕설이 감지되었습니다", description="아래는 욕설 사용자에 대한 정보입니다.\n지속적인 욕설 사용 시 제재 대상입니다.\n욕설 사용 시 자동적으로 로그가 생성되며, 관리진분이 확인 가능합니다", color=0xff0000)
        embed.add_field(name="――――――――――――――――――――――――――――――――――", value="욕설 사용자 정보", inline=False)
        embed.add_field(name="``이용자 디스코드 ID``", value="ID : {}".format(message.author.id), inline=True)
        embed.add_field(name="``이용자 디스코드 닉네임``", value="NickName : {}".format(message.author), inline=True)
        embed.add_field(name="――――――――――――――――――――――――――――――――――", value="욕설 사용 정보", inline=False)
        embed.add_field(name="``이용자 사용 단어``", value="Word : {}".format(bw), inline=True)
        embed.add_field(name="``이용자 욕설 사용 채널``", value="Channel : {}".format(message.channel), inline=True)
        embed.set_footer(text="Bot Made by. 바코드 #1741 | Bad word detection Support by. MOS 엘크님", icon_url="https://media.discordapp.net/attachments/703908401381376000/714396047102967849/2.png")
        await message.author.send(embed=embed)



@client.event
async def on_member_join(member):
    await member.add_roles(get(member.guild.roles, name="여행객"))
    await member.send("**카르페디엠 서버에 오신 것을 환영합니다 !**\n먼저, 아래 사항들을 정독해 주세요")
    embed = discord.Embed(title="Carpediem 인증 신청 방법", description="아래 사항을 보고도 모르시는게 있다면,\n인게임에서 ``K - 관리 - 도우미호출`` 부탁 드립니다", color=0xfdff00)
    embed.add_field(name="``[1] 고유번호 & 닉네임 확인하기``", value="- 고유번호 : 서버에 들어오는 순서대로 나열되는 번호\n- 닉네임 : 자신이 선정한 스팀 or FiveM 닉네임\n\n- 확인 방법 : 인게임 오른쪽 하단 확인 & T를 누르고 /ooc 입력", inline=False)
    embed.add_field(name="``[2] 선택한 직업 확인하기``", value="- 직업 : 자신이 시청에서 선택 한 직업\n\n- 확인 방법 : 오른쪽 위 상단 하얀색 글씨 확인", inline=False)
    embed.add_field(name="``[3] 디스코드 전체화면 스크린샷 찍기``", value="디스코드가 전체화면이 나올 수 있도록 스크린샷을 찍어 첨부합니다\n\n( 방법 1 )\n윈도우를 사용하시는 분이시라면 '캡처 도구'를 사용하시면 편리합니다\n[ 사용 방법 : 새로 만들기 클릭 - 디스코드 전체화면 드래그 - 붙여넣기로 첨부 ]\n\n( 방법 2 )\nF12키 오른쪽 PrtSc 키를 눌러 스크린샷을 찍은 후\n디스코드 메세지 입력 창에 Ctrl + V를 눌러 붙여넣는다.", inline=False)
    embed.add_field(name="``[4] 닉네임 변경하기``", value="카르페디엠 디스코드 채널 '닉네임 변경 방법'을 참고하여\n디스코드 닉네임을 변경 해주세요! ( 고유번호 | 닉네임 | 직업 순 )", inline=False)
    embed.add_field(name="``[5] 입력 하기``", value="고유번호, 닉네임, 직업과 자신이 찍은 스크린샷을 모두 입력 해주세요!\n입력이 완료되었다면, 인증 도우미 분들이 확인을 해주실 것 입니다.\n모르는 부분이 있다면 도우미분에게 개인DM으로 질문해 주세요!", inline=False)
    embed.set_footer(text="Bot Made by. 바코드 #1741", icon_url="https://media.discordapp.net/attachments/703908401381376000/714396047102967849/2.png")
    await member.send(embed=embed)
    
   

    channel = client.get_channel(676924992696352833)
    await channel.send("{}\n**카르페디엠 서버에 오신 것을 환영합니다!**\nDM으로 보내드린 정보들을 참고 하여 인증신청 부탁드립니다 !".format(member.mention))


@client.event
async def on_member_left(member):
    channel = client.get_channel(588343329532674048)
    await channel.send("{}\n님이 서버를 나가셨습니다.".format(member.mention))


client.run(token)