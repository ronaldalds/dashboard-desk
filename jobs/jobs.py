from tecnicos.models import Tecnicos, TempoSLA, SLA_OS, TecnicosMensagem, Log, TiposOS
from dotenv import dotenv_values
import requests
import datetime
import telebot

config = dotenv_values(".env")


def MKat_API(url, data):
    """ Obtem Agenda do tecnico """

    resultado = requests.post(url, data=data)
    if resultado.status_code == 200:
        return resultado.json()
    else:
        print("Oops!, erro eo consultar MKat (っ °Д °;)っ")


def Obter_Agenda_Tecnico(nome_tecnico):
    """ Obtem Agenda do tecnico """

    Agenda = MKat_API(url='https://mkat.online.psi.br/agenda/tecnico', data={
        "token": config['TOKEN'],
        "tecnico": nome_tecnico,
        "de": datetime.datetime.now().strftime('%Y-%m-%d'),
        "ate": (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%Y-%m-%d'),
        "mk": 1
    })

    return Agenda


def Obter_Tipo_SLA(Tipo_OS):
    tipo = TiposOS.objects.get(tipo=Tipo_OS)
    status = SLA_OS.objects.filter(id_tipo_os=tipo, status=True).first()
    if status:
        return status.sla
    else:
        return -1


def Obter_Diferenca_hora(Data_Abertura):
    formato_data_hora = '%Y/%m/%d %H:%M:%S'
    data_e_hora_em_texto = datetime.datetime.now().strftime(formato_data_hora)

    return round(((datetime.datetime.strptime(data_e_hora_em_texto, formato_data_hora) -
                   datetime.datetime.strptime(Data_Abertura, formato_data_hora)).total_seconds())/3600, 2)


def Obter_Tempo_de_Aviso():
    tempo_aviso = TempoSLA.objects.all().values()
    return sorted([x['sla'] for x in tempo_aviso])


def Enviar_Notificacao(Cod_OS, ID_Tecnico, Tempo_Aviso, Nome_Tecnico, Tipo_OS, Data_Abertura, Chat_ID):
    Mensagens = TecnicosMensagem.objects.filter(
        cod_os=Cod_OS).filter(chat_id=ID_Tecnico).filter(sla=Tempo_Aviso).filter(status=True).values()

    if len(Mensagens) == 0:
        print('Nome_Tecnico : ', Nome_Tecnico)
        Nome_Tecnico_Formatado = (Nome_Tecnico.replace('.', ' ')).title()
        msg = f"🔴 🟡 🟢\n\nOlá {Nome_Tecnico_Formatado}.\n\n\rFalta menos de {Tempo_Aviso} horas para a seguinte O.S. expirar.\n\n\rCód O.S. : {Cod_OS}\nTipo O.S : {Tipo_OS}\nData Abertura : {Data_Abertura}"
        try:
            bot_telegram = telebot.TeleBot(config['TELEGRAM'], parse_mode=None)

            bot_telegram.send_message(chat_id=Chat_ID, text=msg)

            TecnicosMensagem.objects.create(chat_id=Tecnicos.objects.get(
                nome=Nome_Tecnico), mensagem=msg, sla=Tempo_Aviso, cod_os=Cod_OS, status=True)

        except:
            TecnicosMensagem.objects.create(
                chat_id=Tecnicos.objects.get(nome=Nome_Tecnico), mensagem=msg, sla=Tempo_Aviso, cod_os=Cod_OS, status=False)
            bot_telegram.send_message(chat_id=int(config["CHAT_ID_ADM"]), text=msg)


def shedule_api():
    Lista_Tecnicos = Tecnicos.objects.filter(status=True)

    for tecnico in Lista_Tecnicos:
        print('id : ', tecnico['id'], ' Nome : ', tecnico['nome'], ' Chat_ID : ', tecnico['chat_id'])
        Chat_ID = int(tecnico['chat_id'])
        Agenda_Tecnico = Obter_Agenda_Tecnico(tecnico['nome'])
        Tempo_Aviso = Obter_Tempo_de_Aviso()

        for agenda in Agenda_Tecnico:
            Data_Abertura = (agenda['os']['data_abertura'][:10]).replace(
                '-', '/')+' '+agenda['os']['hora_abertura'][:8]
            Encerrado = agenda['os']['encerrado']
            Cod_OS = agenda['codos']
            Tipo_OS = agenda['os']['tipo_os']['descricao']

            if not Encerrado:
                print('Tipo_OS : ', Tipo_OS)
                Hora_Passada = Obter_Diferenca_hora(Data_Abertura)
                Sla_Max = Obter_Tipo_SLA(Tipo_OS)

                if Sla_Max > 0:
                    for tempo_aviso in Tempo_Aviso:
                        if ((Sla_Max - Hora_Passada) >= 0) and ((Sla_Max - Hora_Passada) <= tempo_aviso):
                            print('*'*20)
                            print(
                                f'Falta menos de: {(Sla_Max - Hora_Passada)} | Aviso de {tempo_aviso}')
                            print('Cod OS: ', Cod_OS)
                            print('Data Abertura: ', Data_Abertura)
                            print('Tipo OS: ', Tipo_OS)
                            print('Vida O.S.: ', round(Hora_Passada, 2))
                            print('*'*20)
                            # Cod_OS, ID_Tecnico, Tempo_Aviso, Nome_Tecnico, Tipo_OS, Data_Abertura
                            Enviar_Notificacao(
                                Cod_OS, int(tecnico['id']), tempo_aviso, tecnico['nome'], Tipo_OS, Data_Abertura, Chat_ID)
                            break

    print('Rodando : ', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    Log.objects.create()

