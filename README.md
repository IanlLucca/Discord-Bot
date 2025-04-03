<div style="display: flex;">
  <img src="https://github.com/user-attachments/assets/38a576b0-ecc2-4ae6-8e37-abc09030f574" width="50">
  <img src="https://github.com/user-attachments/assets/5a84afa6-550e-4b46-ac05-eee907386799" width="50">
</div>
<h1>Como configurar um Bot do Discord (PT/BR)</h1>
  <h2>Sobre o projeto </h2>
    <p>&nbsp;&nbsp;&nbsp;&nbsp;O intuito desse projeto é ajudar pessoas que não entendam muito da documentação do próprio Discord que está originalmente em inglês. Aqui vou ensinar o basico sobre configurações do bot e comandos uteis, deixando o bot pronto para uso, você vai aprender, linha por linha, como funciona o programa (o arquivo final vai estar anexado).
      Essa aplicação será totalmentte feita em <strong>Python</strong>, portanto tenha o <strong>Python</strong> e uma <span title="Ambiente de Desenvolvimento Integrado"><strong>*IDE</strong></span> (como o <strong>PyCharm</strong> ou <strong>VSCode</strong>) 
      instalados no seu computador.</p>
    
  <h2>#1 - Discord Developer e DiscordAPI</h2>
    <p>Para começarmos, primeiro devemos criar uma nova aplicação no <strong>Discord Developer</strong>, acesse o site:</p>
    
    https://discord.com/developers/applications
  <p> &nbsp;&nbsp;&nbsp;&nbsp;Agora que você está em <strong>Applications</strong>, clique no botão <strong>New Applications</strong>. Declare o nome do seu app (o nome do bot pode ser alterado depois) e aceite os termos. Depois vá na parte de <strong>Bot</strong>, 
    ache e habilite as opções <strong>Presence Intent</strong>, <strong>Server Members Intent</strong> e <strong>Message Content Intent</strong>.
    No final da página você vai encontrar <strong>Bot Permissions</strong>, clique para dar permissão de <strong>Administrator</strong> (para ficar mais facil de utilizá-lo).<br>
    &nbsp;&nbsp;&nbsp;&nbsp;Feito isso, vc deve ir em <strong>General Information</strong> e na parte de <strong>Application ID</strong> você deve copiar o ID e ir para esse site: </p>
    
    https://discordapi.com/permissions.html
  <p>&nbsp;&nbsp;&nbsp;&nbsp;Nele você vai colar o ID em <strong>Client ID</strong> e marcar a opção <strong>Administrator</strong> e copiar o link que está na parte inferior. Agora convide o seu bot para algum servidor (crie um servidor privado para testar as funcionalidades do seu bot e não ter problemas com servidores publicos)</p>

<div style="display: flex;">
  <img src="https://github.com/user-attachments/assets/61660b37-a38d-4896-bf5e-c41959989517">
</div>
    <p>&nbsp;&nbsp;&nbsp;&nbsp;Depois disso, precisamos de só mais uma coisa do <strong>Discord Developer</strong> para fazer nosso bot funcionar perfeitamente, o <strong>Token</strong> que está localizado na aba <strong>Bot</strong>. Esse Token é uma das partes mais importantes do projeto, pois com ele você vai consegui conectar com o seu próprio computador e enviar comandos para o bot.</p>
    <p><strong>(⚠️ATENÇÃO: Esse código token só você deve ter acesso, pois qualquer um que tiver esse código pode alterar seu bot⚠️)</strong></p>

<h2>#2 - Colocando o Bot Online</h2>
  <p>&nbsp;&nbsp;&nbsp;&nbsp;Nessa parte, vamos entrar na área que envolve programação, para isso você deve estar com o <strong>Python</strong> e uma <span title="Ambiente de Desenvolvimento Integrado"><strong>IDE</strong></span> instalados para darmos continuidade. Antes de começarmos a por a mão na massa, precisamos instalar a biblioteca <strong>discord.py</strong>, pois ela vai permitir que o bot se conecte com o Discord, podendo efetuar comandos e interagir nos servers. Para isso, você deve ir no Prompt de Comando do seu próprio computador e digitar o seguinte comando: </p>
  
    pip install discord.py
<p>&nbsp;&nbsp;&nbsp;&nbsp;Com a biblioteca <strong>discord.py</strong> instalada, podemos começar a programar de verdade. Abra sua <strong>IDE</strong> e crie um arquivo no formato <strong>.py</strong> (isso especifica que é na linguagem Python), depois escreva os seguintes comandos: </p>

```
import discord                                                    #Importa a biblioteca discord.py
from discord.ext import commands                                  #Importa a biblioteca discord.ext.commands

TOKEN = "coloque_seu_token_aqui"                                  #Coloque seu token aqui

intents = discord.Intents.default()                               #Cria intents
intents.message_content = True                                    #Ativa leitura de mensagens
intents.members = True                                            #Ativa leitura de membros
bot = commands.Bot(command_prefix="!", intents=intents)           #Cria o bot com o prefixo "!" e as intents
client = discord.Client(intents=intents)                          #Cria o client com as intents

@bot.event                                                        #Evento que acontece quando o bot está pronto
async def on_ready():                           
    print(f'Bot conectado como {bot.user}')                       #Vai aparecer no terminal quando o bot estiver online

bot.run(TOKEN)                                                    #Vai fazer o bot conectar no discord
```
<p>&nbsp;&nbsp;&nbsp;&nbsp;Se quiser, pode apagar as anotações de cada linha (as q estão em "#"), mas coloque o seu <strong>Token</strong> no lugar indicado para o programa conectar e indentificar que é o seu bot. Agora rode o programa e, se você seguiu o passo a passo perfeitamente, seu bot vai ficar online no discord: </p>

<div style="display: flex;">
  <img src="https://github.com/user-attachments/assets/bcc06e20-26c2-4537-b099-3eaa4f002c94" width="250">
</div>
<p>&nbsp;&nbsp;&nbsp;&nbsp;Vale ressaltar que o bot só vai ficar online quando você estiver com o programa rodando, quando você fechar o bot também desligara e ficara inativo. Se você quer que seu bot fique online por tempo integral, vai ter que colocalo em alguma hospedagem, que garanta a segurança dos arquivos.</p>

<h2>#3 - Comandos do Bot</h2>
<p>&nbsp;&nbsp;&nbsp;&nbsp;O arquivo que temos até agora é bem basico, o bot não consegue fazer, praticamente, nada, só analisar conversar e ver os membros. Portanto, vamos adicionar alguns comandos como: </p>
<h3>● Mensagens de Texto ●</h3>

```
@bot.event
async def on_message(message):
    if message.author == client.user:
        return
    print(f'📩 Mensagem recebida de {message.author}: {message.content}')
    if message.content == '!oi':
        await message.channel.send(f'👋Olá {message.author.mention}!!!')
    elif message.content == '!adeus':
        await message.channel.send(f"👋Adeus {message.author.mention}!!!") 
```
<P>&nbsp;&nbsp;&nbsp;&nbsp;Primeiramente o bot vai ler todos chats que ele tem permissão e toda vez que alguém digitar algo vai aparecer no terminal. Depois quando uma pessoa digitar os comandos "!oi" e "!adeus", o bot vai responder exatamente a mensagem definida, mas só vai responder se o comando estiver exatamente escrito do jeito definido. Para corrigir isso, podemos fazer com que o bot leia todas as mensagens mas em letras minusculas, sem ter essa confusão entre letras minusculas e maiusculas: </P>

```
@bot.event
async def on_message(message):
    if message.author == client.user:
        return
    print(f'📩 Mensagem recebida de {message.author}: {message.content}')
    mensagem = message.content.lower()
    if mensagem == '!oi':
        await message.channel.send(f"👋Olá {message.author.mention}!!!") 
    elif mensagem == '!adeus':
        await message.channel.send(f"👋Adeus {message.author.mention}!!!")
```
<p>&nbsp;&nbsp;&nbsp;&nbsp;Podemos adicionar diversas outras mensagens já determinadas com comandos especificos, mas se formos ficar adicionando "elif" toda vez, nosso código fiicará muito confuso. Portanto eu recomendo utilizar dessa forma:
</p>

```
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
```
<p>&nbsp;&nbsp;&nbsp;&nbsp;Dessa forma seu código ficará mais visivel para você modificalo quando quiser e adicionar outras interações, como eu fiz adicionando "!regras".</p>

<h3>● Mensagem de boas vindas ●</h3>
<p>&nbsp;&nbsp;&nbsp;&nbsp;Para adicionar uma mensagem de boas vindas personalizada é bem simples, basta você adicionar o seguinte comando e personalisar o texto como quiser: </p>

```
@bot.event
async def on_member_join(member):               
    print(f'👋 {member.name} entrou no servidor!')  #Vai aparecer no seu terminal toda vez q alguem entrar no servidor
    guild = member.guild
    if guild.system_channel is not None:
        mensagembemvindo = f'Bem-vindo(a) {member.mention} ao {guild.name}!'
        await guild.system_channel.send(mensagembemvindo)
```
![image](https://github.com/user-attachments/assets/f681474c-4c3f-45d4-b0d0-758d0aa2cfe3)

<h3>● Randomizar Mensagens ●</h3>
<p>&nbsp;&nbsp;&nbsp;&nbsp;Randomização é um método bem conhecido, permite que deixe as coisas aleatórias até certo nível. Para fazer isso, vamos utilizar uma biblioteca nativa do <strong>Python</strong>, a biblioteca <strong>Random</strong>: </p>

```
import random
```
<p>&nbsp;&nbsp;&nbsp;&nbsp;Para ser mais facil de randomizar, vamos criar uma <strong>array</strong> como essa: </p>

```
frasesdeoi = [                                              #Lista de frases de oi, para aleatorizar
    "Como você está?",
    "Tudo bem?",
    "Como posso ajudar?",
    "O que você precisa?",
    "Como vai?"
]
```
<p>&nbsp;&nbsp;&nbsp;&nbsp;Agora é só mandar o próprio programa randomizar essas palavras, assim, toda vez que alguém solicitar o comando, o bot vai escolher aleatóriamente uma dessas frases: </p>

```
if mensagem in comandos:                                    # Verifica se a mensagem está nos "comandos"
        await message.channel.send(comandos[mensagem])
        if mensagem == "!oi":
           await message.channel.send(random.choice(frasesdeoi))  
```
![image](https://github.com/user-attachments/assets/acc6dee6-393f-469d-b4ea-fcb031d66209)

<h3>● Desligar o Bot por Comando ●</h3>
<p>&nbsp;&nbsp;&nbsp;&nbsp;Outro tipo de comando simples, mas que deve ser usado corretamente. Esse tipo de comando você não deve deixar aberto ao publico, se não, qualquer um pode desligar o seu bot, portanto utilize com sabedoria e não deixe esse comando à mostra: </p>

```
if mensagem == "!adeus":
        await message.channel.send('Desligando...')
        await bot.close()                                       #Desliga o bot  
```

  <h2>🚧AINDA TERMINANDO A DOCUMENTAÇÃO🚧</h2>
