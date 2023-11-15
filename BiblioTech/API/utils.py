from datetime import datetime

def converter_dataNascimento(data_nascimento_str):
    partes = data_nascimento_str.split('/')
    if len(partes) == 3:
        data_nascimento = datetime.strptime(f'{partes[0]} {partes[1]} {partes[2]}', '%d %m %Y').strftime('%Y-%m-%d')
        return data_nascimento
    else:
        return None
    

def converter_dataEmprestimo(data_emprestimo_str):
    partes = data_emprestimo_str.split('/')
    if len(partes) == 3:
        data_emprestimo = datetime.strptime(f'{partes[0]} {partes[1]} {partes[2]}', '%d %m %Y').strftime('%Y-%m-%d')
        return data_emprestimo
    else:
        return None
    

def converter_dataDevolucao(data_devolucao_str):
    partes = data_devolucao_str.split('/')
    if len(partes) == 3:
        data_devolucao = datetime.strptime(f'{partes[0]} {partes[1]} {partes[2]}', '%d %m %Y').strftime('%Y-%m-%d')
        return data_devolucao
    else:
        return None
