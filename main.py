import discord
from random import randint, choice
from discord.ext import commands
import datetime, pyowm
#import speech_recognition as sr
from discord.utils import get
import pyttsx3
import os
from urllib.request import urlopen
from time import sleep
import requests
from PIL import Image, ImageFont, ImageDraw
import io
import asyncio
import json

nickrole = 'g'
PREFIX = '.'
is_bought = False
color_role = 'f'
bad_words = [ 'кик', 'флуд', 'спам', 'бан' ]
nickroles = ['as']
client = commands.Bot( command_prefix = PREFIX )
client.remove_command( 'help' )

def draw_progress(image: Image, percent: int) -> Image:
	if percent < 0:
		return image

	if percent > 100:
		percent = 100

	width, height = image.size

	progress_width = 620 * (percent / 100)
	progress_height = 40  # Пусть будет 10% от высоты

	x0 = 260
	y0 = 136  # 80% от высоты
	x1 = x0 + progress_width
	y1 = y0 + progress_height

	image = image.copy()

	drawer = ImageDraw.Draw(image)
	drawer.rectangle(xy=[x0, y0, x1, y1], fill=(98,211,245))  # RGB, green

	return image

@client.event
async def on_ready():
	print('[CLIENT]: Connected')
	await client.change_presence( status = discord.Status.online, activity = discord.Game( 'разработку бота' ) )

@client.event
async def on_error( ctx, error ):
    print(error)
    print('[CLIENT]: Error')

@client.event
async def on_command_error( ctx, error ):
	pass
	#print(error)
    
#@client.event
#async def on_member_join( member ):
	#role = discord.utils.get( member.guild.roles, id = 837004981206253641 )
	#потом добавить
	#await member.add_roles( role )
	#await channel.send( embed = discord.Embed( description = f'Пользователь ``{ member.name }``, присоеденился к нам!', color = 0x3ec95d ) )

def debug():
	print('[Debug]: Good!')

@client.event
async def on_raw_reaction_add(payload):
	with open('coins.json','r') as f:
			coins = json.load(f)
	print(payload.emoji.id)
	message_id = payload.message_id # ID сообщения
	channel_id = payload.channel_id # ID канала
	if message_id == 848246016145883146:
		if payload.emoji.id == 843036882744770570:
			channel = client.get_channel(channel_id) # Получаем канал
			message = await channel.fetch_message(message_id) # Получаем сообщение
			author = message.author # Автор сообщения
			user_id = payload.user_id # ID пользователя, который добавил реакцию
			he_coins = int(coins[str(user_id)]['coin'])
			if he_coins >= 400:
				role = discord.utils.get(channel.guild.roles, id = 840733081740640296)
				user = channel.guild.get_member(user_id) # Пользователь, который добавил реакцию
				await payload.member.add_roles(role) # Добавляем роль пользователю
				he_coins = he_coins - 400
				coins[str(user_id)]['coin'] = str(he_coins)
				#send(embed = discord.Embed(description = f'{author.mention}, введите название роли с помощью команды "{PREFIX}название". \nУ вас на это 1 минута.'))
				await message.channel.send(embed = discord.Embed(description = f'{payload.member.mention}, введите название роли с помощью команды "{PREFIX}название". \nУ вас на это 1 минута.'))
				await asyncio.sleep(60)
				global is_bought
				if is_bought is False:
					await ctx.channel.purge( limit = 1 )
					await payload.member.remove_roles(role) # Удаляем роль пользователя
				else:
					is_bought = False
		elif payload.emoji.id == 843036185408045057:
			channel = client.get_channel(channel_id) # Получаем канал
			message = await channel.fetch_message(message_id) # Получаем сообщение
			author = message.author # Автор сообщения
			user_id = payload.user_id # ID пользователя, который добавил реакцию
			role = discord.utils.get(channel.guild.roles, id = 840733081740640296)
			user = channel.guild.get_member(user_id) # Пользователь, который добавил реакцию
			await payload.member.add_roles(role) # Добавляем роль пользователю
			he_coins = int(coins[str(user_id)]['coin'])
			#if author.roles.has(807404209146036294)
			if he_coins >= 500:
				he_coins = he_coins - 500
				coins[str(user_id)]['coin'] = str(he_coins)
				await message.channel.send(embed = discord.Embed(description = f'{payload.member.mention}, отметьте участника с помощью команды "{PREFIX}брак @user". \nУ вас на это 1 минута.'))
				await asyncio.sleep(60)
				if is_bought is False:
					await ctx.channel.purge( limit = 1 )
					await payload.member.remove_roles(role) # Удаляем роль пользователя
				else:
					is_bought = False
		with open('coins.json','w') as f:
					json.dump(coins,f)	



	elif message_id == 843054810956955698:
		if payload.emoji.id == 843046525301948426:
			channel = client.get_channel(channel_id) # Получаем канал
			message = await channel.fetch_message(message_id) # Получаем сообщение
			author = message.author # Автор сообщения
			user_id = payload.user_id # ID пользователя, который добавил реакцию
			role = discord.utils.get(channel.guild.roles, id = 839661879181967401)
			user = channel.guild.get_member(user_id) # Пользователь, который добавил реакцию
			await payload.member.add_roles(role) # Добавляем роль пользователю
		if payload.emoji.id == 843049577077538866:
			channel = client.get_channel(channel_id) # Получаем канал
			message = await channel.fetch_message(message_id) # Получаем сообщение
			author = message.author # Автор сообщения
			user_id = payload.user_id # ID пользователя, который добавил реакцию
			role = discord.utils.get(channel.guild.roles, id = 839652175278112808)
			user = channel.guild.get_member(user_id) # Пользователь, который добавил реакцию
			await payload.member.add_roles(role) # Добавляем роль пользователю
		if payload.emoji.id == 843050233289113620:
			channel = client.get_channel(channel_id) # Получаем канал
			message = await channel.fetch_message(message_id) # Получаем сообщение
			author = message.author # Автор сообщения
			user_id = payload.user_id # ID пользователя, который добавил реакцию
			role = discord.utils.get(channel.guild.roles, id = 840728045899350037)
			user = channel.guild.get_member(user_id) # Пользователь, который добавил реакцию
			await payload.member.add_roles(role) # Добавляем роль пользователю
		if payload.emoji.id == 843049888098549760:
			channel = client.get_channel(channel_id) # Получаем канал
			message = await channel.fetch_message(message_id) # Получаем сообщение
			author = message.author # Автор сообщения
			user_id = payload.user_id # ID пользователя, который добавил реакцию
			role = discord.utils.get(channel.guild.roles, id = 839662460519841830)
			user = channel.guild.get_member(user_id) # Пользователь, который добавил реакцию
			await payload.member.add_roles(role) # Добавляем роль пользователю
		if payload.emoji.id == 843050808580767764:
			channel = client.get_channel(channel_id) # Получаем канал
			message = await channel.fetch_message(message_id) # Получаем сообщение
			author = message.author # Автор сообщения
			user_id = payload.user_id # ID пользователя, который добавил реакцию
			role = discord.utils.get(channel.guild.roles, id = 840728187847835649)
			user = channel.guild.get_member(user_id) # Пользователь, который добавил реакцию
			await payload.member.add_roles(role) # Добавляем роль пользователю
		if payload.emoji.id == 843051162416840784:
			channel = client.get_channel(channel_id) # Получаем канал
			message = await channel.fetch_message(message_id) # Получаем сообщение
			author = message.author # Автор сообщения
			user_id = payload.user_id # ID пользователя, который добавил реакцию
			role = discord.utils.get(channel.guild.roles, id = 840728054921953351)
			user = channel.guild.get_member(user_id) # Пользователь, который добавил реакцию
			await payload.member.add_roles(role) # Добавляем роль пользователю
		if payload.emoji.id == 843054309271928843:
			channel = client.get_channel(channel_id) # Получаем канал
			message = await channel.fetch_message(message_id) # Получаем сообщение
			author = message.author # Автор сообщения
			user_id = payload.user_id # ID пользователя, который добавил реакцию
			role = discord.utils.get(channel.guild.roles, id = 840729472201916457)
			user = channel.guild.get_member(user_id) # Пользователь, который добавил реакцию
			await payload.member.add_roles(role) # Добавляем роль пользователю


@client.event
async def on_message( message ):
	chan = message.channel.id
	if True:
		await client.process_commands( message )
		with open('lvl.json','r') as f:
			users = json.load(f)
		with open('coins.json','r') as f:
			coins = json.load(f)
		async def update_data(users,user):
			if not user in users:
				users[user] = {}
				users[user]['exp'] = 0
				users[user]['lvl'] = 1
		async def upd_data_coin(coins, user):
			if not user in coins:
				coins[user] = {}
				coins[user]['coin'] = 0
		async def add_exp(users,user,exp):
			users[user]['exp'] += exp
		async def add_lvl(users,user, coins):
			exp = users[user]['exp']
			lvl = users[user]['lvl']
			nuth = lvl*2
			the_bot = str(836643079216824320)
			if exp > nuth and message.author.id != the_bot:
				users[user]['exp'] = 0
				users[user]['lvl'] = lvl + 1
				lvla = users[user]['lvl']
				coi = coins[user]['coin'] 
				co = lvla*2
				coins[user]['coin'] = coi + co
				coco = coins[user]['coin'] 
				chanel = client.get_channel(839567596093046864)
				embed = discord.Embed(title = 'LVL UP!:up:', color = message.author.color)
				embed.add_field(name = '**kaif zone bot :gem:**', value = f"{message.author.mention} повысил свой уровень!\nТеперь у него **{lvla} LVL**.\nНачислено **{co} kaif coin'ов**. Итог: **{coco} kaif coin'ов!**", inline=False)
				#embed.add_field(name=, value='' , inline = False)
				await chanel.send(embed = embed)
		await update_data(users,str(message.author.id))
		await upd_data_coin(coins, str(message.author.id))
		await add_exp(users,str(message.author.id),0.5)
		await add_lvl(users,str(message.author.id), coins)
		with open('lvl.json','w') as f:
			json.dump(users,f)
		with open('coins.json','w') as f:
			json.dump(coins,f)


	msg = message.content.lower()

@client.command(aliases = ['название'])
async def name_new_role(ctx, name : str = None , sec_name : str = None):
	chan = ctx.channel.id
	if chan == 838440566781640705:
		global is_bought
		is_bought = True
		if name is None:
			await ctx.channel.purge( limit = 1 )
			pass
		else:
			await ctx.channel.purge( limit = 2 )
			global nickrole
			
			if sec_name is None:
				nickrole = name
				await ctx.send(embed = discord.Embed(description = f'Название "{name}" успешно установлено!\n Теперь используя команду "{PREFIX}done" можно звершить настройку новой роли.', color = ctx.author.color))
			else:
				nickrole = name + ' ' + sec_name
				await ctx.send(embed = discord.Embed(description = f'Название "{name} {sec_name}" успешно установлено!\n Теперь используя команду "{PREFIX}done" можно звершить настройку новой роли.', color = ctx.author.color))

@client.command(aliases = ['брак'])
async def brak(ctx, member : discord.Member = None):
	chan = ctx.channel.id
	if chan == 838440566781640705:
		global is_bought
		is_bought = True
		if member is None:
			await ctx.channel.purge( limit = 1 )
		else:
			print(member.roles)
			if '807404209146036294' in member.roles or '807404209146036294' in ctx.author.roles:
				await ctx.channel.purge( limit = 2 )
				await ctx.send(embed = discord.Embed(description = f'Поздравляем! Теперь {ctx.author.mention} и {member.mention} состоят в браксочетании.', color = ctx.author.color))
				await asyncio.sleep(20)
				await ctx.channel.purge( limit = 1 )
			else:
				await ctx.send(embed = discord.Embed(description = f'Нельзя *выйти замуж*/*жениться*, если у одного из участников нет роли <@807404209146036294>', color = ctx.author.color))
				await asyncio.sleep(20)
				await ctx.channel.purge( limit = 2 )

@client.command()
async def done(ctx):
	chan = ctx.channel.id
	if chan == 838440566781640705:
		global is_bought
		if is_bought is True:
			await ctx.channel.purge( limit = 2 )
			guild = ctx.message.guild
			colour=discord.Colour(0xFFFF00)
			global nickrole
			await guild.create_role(name= nickrole, color = colour, reason = 'Покупка за kaif coin')
			message_id = ctx.message.id # ID сообщения
			channel_id = ctx.channel.id # ID канала
			channel = client.get_channel(channel_id) # Получаем канал
			author = ctx.author # Автор сообщения
			user_id = ctx.author.id # ID пользователя, который добавил реакцию
			role = discord.utils.get(channel.guild.roles, name = nickrole)
			buy_role = discord.utils.get(channel.guild.roles, id = 840733081740640296)
			user = channel.guild.get_member(user_id) # Пользователь, который добавил реакцию
			await ctx.author.add_roles(role) # Добавляем роль пользователю
			await ctx.author.remove_roles(buy_role)
			new_position = buy_role.position
			new_position = int(new_position) - 1
			await role.edit(position = new_position)
			await ctx.send(embed = discord.Embed(description = f'Роль успешно создана!:white_check_mark:', color = ctx.author.color))
			await asyncio.sleep(20)
			await ctx.channel.purge( limit = 1 )
			role_for_buy = discord.utils.get(channel.guild.roles, id = 840733081740640296)
			await payload.member.remove_roles(role_for_buy) # Удаляем роль пользователю



@client.command(aliases = ['префикс'])
@commands.has_permissions( administrator = True )
async def set_prefix(ctx, reasons = None ):
	if reasons is None:
		await ctx.send(f'{ctx.message.author.mention}, укажите префикс. Пример: .префикс ~')
	elif ctx.author.id == 553776481092763679 or ctx.author.id == 457937441039450112:
		PREFIX = reasons
		embed = discord.Embed(title = 'kaif zone bot :gem:', description = f'{ctx.message.author.mention}, Вы успешно установили {reasons} как префикс!', color = ctx.message.author.color)
		await ctx.send(embed = embed)
	else:
		ctx.send(f'Функция установки префикса доступно только разработчику/владельцу сервера!')

@client.command(aliases = ['setlvl'])
@commands.has_permissions( administrator = True )
async def set_lvl(ctx, member : discord.Member = None, amount : int = None ):
	if member.id == 457937441039450112 or member.id == 553776481092763679:
		if amount is None or member is None:
			await ctx.send(f':x:{ctx.author.mention}, ошибка в написании команды!:x:\nПример: .setlvl {ctx.author.mention} 666')
		elif amount <= 0:
			await ctx.send(f':x:{ctx.author.mention}, LVL не может быть меньше либо равно 0:x:')
		else:
			with open('lvl.json','r') as f:
				users = json.load(f)
				user = str(member.id)
			if not user in users:
				users[user] = {}
				users[user]['exp'] = 0
				users[user]['lvl'] = amount
				await ctx.send(f':warning:{ctx.author.mention}, указанный пользователь не имел уровня.:warning:\n Теперь имеет)')
			else:
				user = str(member.id)
				users[user]['lvl'] = amount
				users[user]['exp'] = 0
				await ctx.send(f':white_check_mark:{ctx.author.mention}, Вы успешно установили {member.mention} {amount} уровень:white_check_mark:')


			with open('lvl.json','w') as f:
				json.dump(users,f)
	else:
		ctx.send(':x:Вы не имеете доступа к данной команде!:x:')


@client.command(aliases = ['setexp'])
@commands.has_permissions( administrator = True )
async def set_exp(ctx, member : discord.Member = None, amount : int = None ):
	with open('lvl.json','r') as f:
				users = json.load(f)
				user = str(member.id)
				lvl_now = users[user]['lvl']
				exp_need = int(lvl_now)*2
	if member.id == 457937441039450112 or member.id == 553776481092763679:
		if amount is None or member is None:
			await ctx.send(f':x:{ctx.author.mention}, ошибка в написании команды!:x:\nПример: .setexp {ctx.author.mention} 12')
		elif amount > exp_need:
			await ctx.send(f':x:{ctx.author.mention}, exp не может быть больше, чем нужно для повышения LVL:x:')
		else:
				user = str(member.id)
				users[user]['exp'] = amount
				await ctx.send(f':white_check_mark:{ctx.author.mention}, Вы успешно установили {member.mention} {amount} exp:white_check_mark:')
	else:
		ctx.send(':x:Вы не имеете доступа к данной команде!:x:')
	with open('lvl.json','w') as f:
		json.dump(users,f)


@client.command(aliases = ['setcoins'])
@commands.has_permissions( administrator = True )
async def set_coins(ctx, member : discord.Member = None, amount : int = None ):
	if member.id == 457937441039450112 or member.id == 553776481092763679:
		if amount is None or member is None:
			await ctx.send(f':x:{ctx.author.mention}, ошибка в написании команды!:x:\nПример: .setcoins {ctx.author.mention} 666')
		elif amount < 0:
			await ctx.send(f':x:{ctx.author.mention}, не могу выдать кредит данному пользователю.:x:')
		else:
			with open('coins.json','r') as f:
				coins = json.load(f)
				user = str(member.id)
			if not user in coins:
				coins[user]['coin'] = amount
				await ctx.send(embed = discord.Embed(description = f":white_check_mark:{ctx.author.mention}, Вы успешно установили {member.mention} {amount} kaif coin'ов:white_check_mark:"))
			else:
				user = str(member.id)
				coins[user]['coin'] = amount
				await ctx.send(embed = discord.Embed(description = f":white_check_mark:{ctx.author.mention}, Вы успешно установили {member.mention} {amount} kaif coin'ов:white_check_mark:"))


			with open('coins.json','w') as f:
				json.dump(coins,f)
	else:
		ctx.send(':x:Вы не имеете доступа к данной команде!:x:')

@client.command()
@commands.has_permissions( kick_members = True )
async def clear( ctx, amount : int  = None):
	if amount is None:
		await ctx.send(embed = discord.Embed(description = f':negative_squared_cross_mark: Syntax error!\nВведите {PREFIX}clear [число]', color=0x0c0c0c))
	else:
		await ctx.channel.purge( limit = amount )
		await ctx.send(embed = discord.Embed(description = f':white_check_mark: Удалено {amount} сообщений', color=0x0c0c0c))

@client.command()
@commands.has_permissions( kick_members = True )
async def kick( ctx, member: discord.Member = None, *, reason = None ):
	if reason is None or member is None:
		await ctx.send(embed = discord.Embed(
			title = f'{ctx.author.name}, **укажите причину**',
			description = f'Пример: .kick @user **reason**'
		))
	else:
		await ctx.channel.purge( limit = 1 )
		await member.kick( reason = reason )
		
		emb = discord.Embed( title = 'Информация об изгнании', description = f'{ member.name.title() }, был выгнан в связи нарушений правил',
		color = 0xc25151 )

		emb.set_author( name = member, icon_url = member.avatar_url )
		emb.set_footer( text = f'Был изганан администратором { ctx.author.mention }', icon_url = ctx.author.avatar_url )

		await ctx.send( embed = emb )

@client.command() #BAN
@commands.has_permissions( administrator = True )
async def ban( ctx, member: discord.Member = None, *, reason = None ):
	if reason is None or member is None:
		await ctx.send(embed = discord.Embed(
			title = f'{ctx.author.name}, **укажите причину**',
			description = f'Пример: .ban @user **reason**'
		))
	else:
		await ctx.channel.purge( limit = 1 )
		await member.ban( reason = reason )
		emb = discord.Embed( title = 'Информация о блокировке участника', description = f'{ member.name }, был заблокирован в связи нарушений правил',
		color = 0xc25151 )

		emb.set_author( name = member.name, icon_url = member.avatar_url )
		emb.add_field( name = f'ID: { member.id }', value = f'Блокированный участник : { member }' )
		emb.set_footer( text = 'Был заблокирован администратором {}'.format( ctx.author.name ), icon_url = ctx.author.avatar_url )

		await ctx.send( embed = emb )


@client.command(aliases = ['card']) # КАРТА
async def card_user(ctx, member: discord.Member = None):
	if member is None:
		await ctx.channel.purge(limit = 1)
		img = Image.open(requests.get('http://i.yapx.ru/NRwBi.png', stream=True).raw) # загружаем картинку в память

		url = str(ctx.author.avatar_url)[:-10] 										  # получаем url аватарки
		response = requests.get(url, stream = True)									  # получаем аватарку
		response = Image.open(io.BytesIO(response.content))							  # ебем аватарку по размерам и формату
		response = response.convert('RGBA')											  
		response = response.resize((170, 170))									
		img.paste(response, (40, 15))												  # вставляем аватарку в фотку

		imagg =Image.open(urlopen('http://i.yapx.ru/NRwBE.png')).convert('RGBA')	  # получаем рамку
		imagg =imagg.resize((900,200))												  # ебем рамку по размерам

		idraw = ImageDraw.Draw(img)													  # чото делаем
		name = ctx.author.name														  # ники, теги и шрифты
		nick = ctx.message.author.display_name
		tag = ctx.author.discriminator 

		headline = ImageFont.truetype('bahnschrift.ttf', size = 45)
		exp_lvl = ImageFont.truetype('malgun.ttf', size = 33)
		


		with open('lvl.json','r') as f:											 	  # получаем лвл и экспу
			users = json.load(f)
		user = str(ctx.author.id)
		exp = users[user]['exp']
		lvl = users[user]['lvl']
		exp_need = lvl*2
		textr = f'{lvl} ({exp}/{exp_need} exp)'
		lentex = len(textr)
		#print(lentex)
		xya = (607, 75)
		if lentex >= 17:															  # делаем красоту
			xya = (560, 75)
		elif lentex <= 13:
			xya = (643, 75)
		idraw.text(xya, f'{lvl} lvl ({exp}/{exp_need} exp)', font = exp_lvl)
		idraw.text((260, 75), f'{nick}#{tag}', font = headline) 
		color=(98,211,245,175)
		exp = int(exp)
		exp_need = int(exp_need)
		per = (exp/exp_need)*100
		img = draw_progress(img, per)											     # рисуем полоску, склеиваем и отправляем
		img.paste(imagg, (0,0), mask=imagg)															
		buf = io.BytesIO()
		img.save(buf, 'PNG')
		buf.seek(0)
		await ctx.send(file = discord.File(fp = buf, filename = 'image.png'))
		#await ctx.send('check')
	else:
		await ctx.channel.purge(limit = 1)
		img = Image.open(requests.get('http://i.yapx.ru/NRwBi.png', stream=True).raw) # загружаем картинку в память
		#img = Image.new('RGBA', (300, 100), imgr)
		url = str(member.avatar_url)[:-10]

		response = requests.get(url, stream = True)
		response = Image.open(io.BytesIO(response.content))
		response = response.convert('RGBA')
		response = response.resize((170, 170))

		img.paste(response, (40, 15))

		idraw = ImageDraw.Draw(img)

		name = member.name # Fsoky
		nick = member.display_name
		tag = member.discriminator # 9610
		font = ImageFont.load_default().font
		headline = ImageFont.truetype('bahnschrift.ttf', size = 45)
		exp_lvl = ImageFont.truetype('malgun.ttf', size = 33)		
		with open('lvl.json','r') as f:
			users = json.load(f)
		user = str(member.id)
		exp = users[user]['exp']
		lvl = users[user]['lvl']
		exp_need = lvl*2
		xya = (607, 75)
		if lentex >= 18:
			xya = (560, 75)
		elif lentex <= 13:
			xya = (643, 75)
		idraw.text(xya, f'{lvl} lvl ({exp}/{exp_need} exp)', font = exp_lvl) # Fsoky#9610
		idraw.text((260, 75), f'{nick}#{tag}', font = headline) # Fsoky#9610
		draw = ImageDraw.Draw(img)
		color=(98,211,245,175)
		x, y, diam = 260, 136, 40
		#idraw.ellipse([x,y,x+diam,y+diam], fill=(98,211,245,175))
		#ImageDraw.floodfill(img, xy=(310,140), value=color, thresh=100)
		draw_progress(img, 50)
		cart = f"Карточку запросил - {ctx.message.author.mention}"
		img.save('user_card.png')
		embed = discord.Embed(title = f'kaif zone :gem:',description = cart, color = member.color)
		await ctx.send(file = discord.File(fp = 'user_card.png'), embed = embed)


@client.command() #me — карточка в тексте
async def me(ctx, member:discord.Member = None):
	kaifcoin = str(client.get_emoji(843036469282603028))
	if member == None:
		with open('coins.json','r') as f:
			coins = json.load(f)
			user = str(ctx.author.id)
		if not user in coins:
				coins[user]['coin'] = 0
		his_coins = coins[user]['coin']
		spotif = ''
		#game = game.Activity.name
		#print('1 ' + game)
		#for activity in user.activities:
		#	if isinstance(activity, discord.Spotify):
		#		spotif = (f"{user} слушает {activity.title} - {activity.artist}")
		emb = discord.Embed(title="Профиль", color=ctx.message.author.color)
		emb.add_field(name="Имя на сервере: ", value=ctx.message.author.display_name,inline=False)
		emb.add_field(name="Высшая роль на сервере: ", value=f"{ctx.author.top_role.mention}",inline=False)
		emb.add_field(name="Баланс: ", value = f"{his_coins} kaif coin'ов {kaifcoin}")

		emb.add_field(name="Брак:", value='Coming soon :hourglass:',inline=False)
		#emb.add_field(name="Статус:", value=f"Test:",inline=False)
		emb.add_field(name = "Вступил: ", value = ctx.author.joined_at)
		emb.set_thumbnail(url=ctx.message.author.avatar_url)
		emb.set_footer(text = f'ID: {ctx.author.id}')
		await ctx.send(embed = emb)
	else:
		with open('coins.json','r') as f:
			coins = json.load(f)
			user = str(ctx.author.id)
		if not user in coins:
				coins[user]['coin'] = 0
		his_coins = coins[user]['coin']
		#spotif = ''
		#print('G ' + Member)
		#user = member
		#game = game.Activity.name
		#print('1 ' + game)
		#for activity in user.activities:
		#	if isinstance(activity, discord.Spotify):
		#		spotif = (f"{user} слушает {activity.title} - {activity.artist}")
		#emb = discord.Embed(title="Профиль", description = f"**Высшая роль на сервере:** {ctx.message.author.display_name}\n**Имя на сервере:** {ctx.message.author.display_name}\n**Баланс:** {his_coins} kaif coin'ов :coin:\n**Брак:** Coming soon :hourglass:\n**Статус:** {game}\n**Вступил:** {ctx.author.joined_at}", color=ctx.message.author.color)
		emb = discord.Embed(title="Профиль", color=member.color)
		emb.add_field(name="Имя на сервере: ", value=f"{member.display_name}", inline = False)
		emb.add_field(name="Высшая роль на сервере: ", value=f"{member.top_role.mention}",inline=False)
		emb.add_field(name="Баланс: ", value = f"{his_coins} kaif coin'ов {kaifcoin}")
		emb.add_field(name="Брак:", value='Coming soon :hourglass:',inline=False)
		#emb.add_field(name="Статус:", value=f"Test:",inline=False)
		emb.add_field(name = "Вступил: ", value = member.joined_at)
		emb.set_thumbnail(url=member.avatar_url)
		emb.set_footer(text = f'ID: {member.id}')
		await ctx.send(embed = emb)

@client.command(aliases = ['help']) #HELP
async def helep(ctx):
	await ctx.send(embed = discord.Embed(
				description = f'''**Список команд и их возможности:**
				```bash
".card" - запрос свой карточки
".card @user" - запрос карточки отмеченного пользователя
".help" - список команд
".me" - просмотреть информацию о себе
```
**Команды администратора**:
```bash
".setlvl @user [уровень]" - установить уровень игроку (при этом сбрасывается кол-во exp)
".mute @user [время (пример: 3m)] [причина]" - установить пользователю мут на определенное время
".kick @user [причина]" - кикает пользователя с сервера
".ban @user [причина]" - банит пользователя
".clear [число]" - удаляет N-ое кол-во сообщений
".setcoins [кол-во]" - выдаёт пользователю N-ое кол-во kaif coin-ов 
".setexp @user [кол-во]" - выдаёт пользователю N-ок кол-во exp
				```
				''',
				color = ctx.author.color,
			))

@client.command(aliases = ['mute'])#MUTE
@commands.has_permissions( kick_members = True )
async def __mute(ctx, member: discord.Member = None, amount_time = None, *, reason = None):
	if member is None:
		await ctx.send(embed = discord.Embed(
			title = f'{ctx.author.name}, **укажите пользователя**',
			description = f'Пример: .mute **@user** time reason'
		))
	elif amount_time is None:
		await ctx.send(embed = discord.Embed(
			title = f'{ctx.author.name}, **укажите кол-во времени**',
			description = f'Пример: .mute @user **time** reason'
		))
	elif reason is None:
		await ctx.send(embed = discord.Embed(
			title = f'{ctx.author.name}, **укажите причину**',
			description = f'Пример: .mute @user time **reason**'
		))
	else:
		if 'm' in amount_time:
			await ctx.channel.purge( limit = 1 )
			await ctx.send(embed = discord.Embed(
				description = f'''**[{member.mention}]** Вы были замучены на **{amount_time}**.
				**Выдал мут:** {ctx.author}
				```css
Причина: [{reason}]
				```
				''',
				color = 0x36393E,
			))

			mute_role = discord.utils.get(ctx.guild.roles, id = 837760789712207962)
			await member.add_roles(mute_role)
			await asyncio.sleep(int(amount_time[:-1]) * 60)
			await member.remove_roles(mute_role)

			await ctx.send(embed = discord.Embed(
				description = f'''**[{member.mention}]** Время мута истекло, вы были размучены''',
				color = 0x2F3136
			))	
		elif 'h' in amount_time:
			await ctx.channel.purge( limit = 1 )
			await ctx.send(embed = discord.Embed(
				description = f'''**[{member.mention}]** Вы были замучены на **{amount_time}**.
				**Выдал мут:** {ctx.author}
				```css
Причина: [{reason}]
				```
				''',
				color = 0x36393E,
			))

			mute_role = discord.utils.get(ctx.guild.roles, id = 837760789712207962)
			await member.add_roles(mute_role)
			await asyncio.sleep(int(amount_time[:-1]) * 60 * 60)
			await member.remove_roles(mute_role)

			await ctx.send(embed = discord.Embed(
				description = f'''**[{member.mention}]** Время мута истекло, вы были размучены''',
				color = 0x2F3136
			))	
		elif 'd' in amount_time:
			await ctx.channel.purge( limit = 1 )
			await ctx.send(embed = discord.Embed(
				description = f'''**[{member.mention}]** Вы были замучены на **{amount_time}**.
				**Выдал мут:** {ctx.author}
				```css
Причина: [{reason}]
				```
				''',
				color = 0x36393E,
			))

			mute_role = discord.utils.get(ctx.guild, id = 837760789712207962)
			await member.add_roles(mute_role)
			await asyncio.sleep(int(amount_time[:-1]) * 60 * 60 * 24)
			await member.remove_roles(mute_role)

			await ctx.send(embed = discord.Embed(
				description = f'''**[{member.mention}]** Время мута истекло, вы были размучены''',
				color = 0x2F3136
			))	
		else:
			await ctx.channel.purge( limit = 1 )
			await ctx.send(embed = discord.Embed(
				description = f'''**[{member.mention}]** Вы были замучены на **{amount_time}s**.
				**Выдал мут:** {ctx.author}
				```css
Причина: [{reason}]
				```
				''',
				color = 0x36393E,
			))

			mute_role = discord.utils.get(ctx.guild.roles, id = 837760789712207962)
			await member.add_roles(mute_role)
			await asyncio.sleep(int(amount_time))
			await member.remove_roles(mute_role)

			await ctx.send(embed = discord.Embed(
				description = f'''**[{member.mention}]** Время мута истекло, вы были размучены''',
				color = 0x2F3136
			))	


# Get token
token = os.environ['TOKEN']
client.run(token)
