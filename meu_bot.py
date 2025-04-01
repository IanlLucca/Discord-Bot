import discord                  #Importando a biblioteca discord.py
import os
from dotenv import load_dotenv
import random                   #Importando a biblioteca q pode randomizar coisas
from flask import Flask
from threading import Thread

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot está online!"

def run():
    app.run(host='0.0.0.0', port=5000)

def keep_alive():
    server = Thread(target=run)
    server.start()

#Vai carregar variáveis do arquivo .env
load_dotenv()
token = os.getenv("discord_token")
if token is None:
    raise ValueError("Token do Discord não encontrado. Verifique o arquivo .env.") #Se não tiver o token, vai dar erro e parar o bot
#Se tiver o token, vai continuar tranquilo
#Se você não tiver o arquivo .env, crie um com o seguinte conteúdo:
#discord_token=seu_token_aqui

#Vai criar intents e ativar leitura de mensagens
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'✅ Bot conectado como {client.user}') #Vai aparecer no terminal quando o bot estiver online

frasesdeoi = [                      #Lista de frases de oi, para aleatorizar
    "Olá! Como você está?",
    "Oi! Tudo bem?",
    "Oi! Como posso ajudar?",
    "Oi! O que você precisa?",
    "Oi! Como vai?",
    ""
]

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    print(f'📩 Mensagem recebida de {message.author}: {message.content}')       #Toda vez q o bot ver alguma menssagem, ele vai mostrar no terminal
    if message.content == '?regras':
        await message.channel.send("📜 Aqui estão as regras do servidor: \n1. Seja respeitoso. \n2. Não faça spam. \n3. Siga as diretrizes da comunidade.")
    elif message.content.lower() == '?ping':
        await message.channel.send("🏓 Pong!")
    elif message.content == '?d6':
        await message.channel.send("🎲 Rolando um dado de 6 lados...")
        await message.channel.send(random.randint(1, 6))
    elif message.content == '?moeda':
        await message.channel.send("🪙 Jogando uma moeda...")
        resultado = random.choice(['Cara', 'Coroa'])
        await message.channel.send(resultado)
    elif message.content == '?oi':
        respostaoi = random.choice(frasesdeoi)
        await message.channel.send(respostaoi)
        #Ou
        #await message.channel.send(random.choice(frasesdeoi))
    
@client.event
async def on_member_join(member):               #Vai fazer com q os membros q entrarem no servidor recebam uma mensagem de boas vindas
    print(f'👋 {member.name} entrou no servidor!')  #Vai aparecer no seu terminal toda vez q alguem entrar no servidor
    guild = member.guild
    if guild.system_channel is not None:
        mensagembemvindo = f'Bem-vindo(a) {member.mention} ao {guild.name}!'
        await guild.system_channel.send(mensagembemvindo)

keep_alive()
client.run(token)   #Inicia o bot com o token do discord   
                    #Ele só vai funcionar se o token estiver certo e o bot estiver online no discord
                    #Mas cuidado, com esse token, qualquer um pode entrar no seu bot e fazer o que quiser com ele, então não compartilhe com ninguém
