from datetime import datetime

def converter_dataAutor(data_nascimento_str):
    partes = data_nascimento_str.split('/')
    if len(partes) == 3:
        data_nascimento = datetime.strptime(f'{partes[0]} {partes[1]} {partes[2]}', '%d %m %Y').strftime('%Y-%m-%d')
        return data_nascimento
    else:
        return None
