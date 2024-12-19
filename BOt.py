import schedule
import time
from telegram import Bot
import asyncio

# Seu token do bot
TOKEN = '7479524024:AAE0WAun0HEQo9QeHYnI5lALtdtWddQyFFU'
GROUP_CHAT_IDS = \
    ['-1002248961927',
     '-1002233378018',
     '-1002244712891',
     '-1002486468642',
     '-1002172438260']  # IDs dos grupos

# Inicialize o bot
bot = Bot(token=TOKEN)

# Função para enviar mensagem
async def send_message(message):
    for chat_id in GROUP_CHAT_IDS:
        try:
            await bot.send_message(chat_id=chat_id, text=message)
            print(f"Mensagem enviada para o chat {chat_id}")
        except Exception as e:
            print(f"Erro ao enviar para {chat_id}: {e}")

# Funções para as mensagens programadas
def send_first_message():
    message = """
⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️
🚴🚴‍♀️     🏍🏍

Próximo turno se inicia em 1 hora.

Entregadores que se agendaram ficarão disponíveis automaticamente no APP.

QUEM NÃO SE AGENDOU, POR FAVOR, FAÇA SUA SOLICITAÇÃO DE VAGA NO GRUPO.

Pedimos que caso não possam rodar no turno agendado, nos informem com antecedência, por favor.
Antes de cada turno ser iniciado.

Contamos com a compreensão de todos e que nos ajudem nessas questões ✌🏻

Equipe ABJP RJ Taquara 💙
    """
    asyncio.run(send_message(message))

def send_second_message():
    message = """
⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️
🚴🚴‍♀️     🏍🏍

Próximo turno se inicia em 1 hora.

Entregadores que se agendaram ficarão disponíveis automaticamente no APP.

QUEM NÃO SE AGENDOU, POR FAVOR, FAÇA SUA SOLICITAÇÃO DE VAGA NO GRUPO.

Pedimos que caso não possam rodar no turno agendado, nos informem com antecedência, por favor.
Antes de cada turno ser iniciado.

Contamos com a compreensão de todos e que nos ajudem nessas questões ✌🏻

Equipe ABJP RJ Taquara 💙
    """
    asyncio.run(send_message(message))

def send_third_message():
    message = """
⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️
🚴🚴‍♀️     🏍🏍

Próximo turno se inicia em 1 hora.

Entregadores que se agendaram ficarão disponíveis automaticamente no APP.

QUEM NÃO SE AGENDOU, POR FAVOR, FAÇA SUA SOLICITAÇÃO DE VAGA NO GRUPO.

Pedimos que caso não possam rodar no turno agendado, nos informem com antecedência, por favor.
Antes de cada turno ser iniciado.

Contamos com a compreensão de todos e que nos ajudem nessas questões ✌🏻

Equipe ABJP RJ Taquara 💙
    """
    asyncio.run(send_message(message))

def send_fourth_message():
    message = """
⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️
🚴🚴‍♀️     🏍🏍

Próximo turno se inicia em 1 hora.

Entregadores que se agendaram ficarão disponíveis automaticamente no APP.

QUEM NÃO SE AGENDOU, POR FAVOR, FAÇA SUA SOLICITAÇÃO DE VAGA NO GRUPO.

Pedimos que caso não possam rodar no turno agendado, nos informem com antecedência, por favor.
Antes de cada turno ser iniciado.

Contamos com a compreensão de todos e que nos ajudem nessas questões ✌🏻

Equipe ABJP RJ Taquara 💙
    """
    asyncio.run(send_message(message))

def send_fifth_message():
    message = """
⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️
🚴🚴‍♀️     🏍🏍

Próximo turno se inicia em 1 hora.

Entregadores que se agendaram ficarão disponíveis automaticamente no APP.

QUEM NÃO SE AGENDOU, POR FAVOR, FAÇA SUA SOLICITAÇÃO DE VAGA NO GRUPO.

Pedimos que caso não possam rodar no turno agendado, nos informem com antecedência, por favor.
Antes de cada turno ser iniciado.

Contamos com a compreensão de todos e que nos ajudem nessas questões ✌🏻

Equipe ABJP RJ Taquara 💙
    """
    asyncio.run(send_message(message))
# Agendar as mensagens
##schedule.every().day.at("16:00").do(send_fifth_message)   # Enviar quinta mensagem às 16:00## adicioanr a quinta se eu quiser
schedule.every().day.at("10:00").do(send_first_message)   # Enviar primeira mensagem às 10:00
schedule.every().day.at("14:00").do(send_second_message)  # Enviar segunda mensagem às 14:00
schedule.every().day.at("17:00").do(send_third_message)   # Enviar terceira mensagem às 17:00
schedule.every().day.at("21:00").do(send_fourth_message)  # Enviar quarta mensagem às 21:00


# Rodar o agendador
while True:
    schedule.run_pending()  # Executa as tarefas agendadas
    time.sleep(1)  # Aguarda 1 segundo antes de verificar novamente
