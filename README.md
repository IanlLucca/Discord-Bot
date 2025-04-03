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
  <img src="https://github.com/user-attachments/assets/bcc06e20-26c2-4537-b099-3eaa4f002c94" width="500">
</div>
<p>&nbsp;&nbsp;&nbsp;&nbsp;Vale ressaltar que o bot só vai ficar online quando você estiver com o programa rodando, quando você fechar o bot também desligara e ficara inativo. Se você quer que seu bot fique online por tempo integral, vai ter que colocalo em alguma hospedagem, que garanta a segurança dos arquivos.</p>

<h2>#3 - Comandos do Bot</h2>
<p>&nbsp;&nbsp;&nbsp;&nbsp;O arquivo que temos até agora é bem basico, o bot não consegue fazer, praticamente, nada, só analisar conversar e ver os membros. Portanto, vamos programar e adicionar alguns comando para ele: </p>

```
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    print(f'📩 Mensagem recebida de {message.author}: {message.content}')       #Toda vez q o bot ver alguma menssagem, ele vai mostrar no terminal
    if message.content == '?regras':
        await message.channel.send("📜 Aqui estão as regras do servidor: \n1. Seja respeitoso. \n2. Não faça spam. \n3. Siga as diretrizes da comunidade.")
```

  <h2>🚧AINDA TERMINANDO A DOCUMENTAÇÃO🚧</h2>
