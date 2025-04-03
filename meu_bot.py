import discord                                              #Importa a biblioteca discord.py
from discord.ext import commands                            #Importa a biblioteca discord.ext.commands
import random

TOKEN = "coloque_aqui_o_token"                              #Coloque seu token aqui

intents = discord.Intents.default()                         #Cria intents
intents.message_content = True                              #Ativa leitura de mensagens
intents.members = True                                      #Ativa leitura de membros
bot = commands.Bot(command_prefix="!", intents=intents)     #Cria o bot com o prefixo "!" e as intents
client = discord.Client(intents=intents)                    #Cria o client com as intents

@bot.event                                                  #Evento que acontece quando o bot está pronto
async def on_ready():                           
    print(f'Bot conectado como {bot.user}')                 #Vai aparecer no terminal quando o bot estiver online

frasesdeoi = [                                              #Lista de frases de oi, para aleatorizar
    "Como você está?",
    "Tudo bem?",
    "Como posso ajudar?",
    "O que você precisa?",
    "Como vai?"
]

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    print(f'📩 Mensagem recebida de {message.author}: {message.content}')
    
    mensagem = message.content.lower()
    comandos = {
        "!oi": f"👋 Olá {message.author.mention}!!!",
        "!adeus": f"👋 Adeus {message.author.mention}!!!",
        "!regras": "📜 Aqui estão as regras do servidor: \n1. Seja respeitoso. \n2. Não faça spam. \n3. Siga as diretrizes da comunidade."
    }
    
    if mensagem in comandos:                                    # Verifica se a mensagem está nos "comandos"
        await message.channel.send(comandos[mensagem])
    if mensagem == "!oi":
        await message.channel.send(random.choice(frasesdeoi)) 
    if mensagem == "!adeus":
        await message.channel.send('Desligando...')
        await bot.close()                                       #Desliga o bot                                         

@bot.event
async def on_member_join(member):               
    print(f'👋 {member.name} entrou no servidor!')  #Vai aparecer no seu terminal toda vez q alguem entrar no servidor
    guild = member.guild
    if guild.system_channel is not None:
        mensagembemvindo = f'Bem-vindo(a) {member.mention} ao {guild.name}!'
        await guild.system_channel.send(mensagembemvindo)

bot.run(TOKEN)                                                  #Vai fazer o bot conectar no discord
