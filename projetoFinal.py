from colorama import Fore, Style, init
import os
import time
import json

init(autoreset=True)

nomes_cidades = []
populacoes = []
areas = []

ARQUIVO_JSON = 'dados.json'

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_mensagem_inicial(primeira_vez):
    mensagem = '\nPressione Enter para iniciar!' if primeira_vez else '\nPressione Enter para continuar!'
    input(Fore.YELLOW + mensagem)

def exibir_arte():
    print(Fore.WHITE + r"""                                         
~         ~~          __        
       _T      .,,.    -- ^^  
 ^^   // \                    ~ 
      ][O]    ^^      ,-~ ~     
   /''-I_I       II_      
/  /   \ / ''   /'\,  
  | II--'''' \,--:--..,_/,.-{ },
; '/__\,.--';|   |[] .-.| O{ _ }
:' |  | []  -|   ''--:.;[,.'\,/ 
'  |[]|,.--'' '',   ''-,.    |  
  ..    ..-''    ;       ''. '  
""" + Style.RESET_ALL, end='')

def carregar_dados():
    global nomes_cidades, populacoes, areas
    try:
        with open(ARQUIVO_JSON, 'r') as f:
            dados = json.load(f)
            nomes_cidades = dados['nomes_cidades']
            populacoes = [int(pop.replace(".", "").replace(",", "")) for pop in dados['populacoes']]
            areas = [float(area.replace(",", ".")) for area in dados['areas']]
    except (FileNotFoundError, json.JSONDecodeError):
        nomes_cidades, populacoes, areas = [], [], []

def salvar_dados():
    dados = {
        'nomes_cidades': nomes_cidades,
        'populacoes': [formatar_numero(pop) for pop in populacoes], 
        'areas': [formatar_area(area) for area in areas]  
    }

    with open(ARQUIVO_JSON, 'w') as f:
        json.dump(dados, f, indent=4)

def formatar_numero(numero):
    return f"{numero:,}".replace(",", ".")  

def formatar_area(area):
    return str(area).replace(".", ",")
    
def carregar_menu():
    print(Fore.YELLOW + '\nCarregando o menu, por favor, aguarde', end='')
    for _ in range(3):
        time.sleep(0.5)
        print(Fore.YELLOW + '.', end='')
    print('\n')

def exibir_menu():
    print(Fore.CYAN + '=' * 43)
    print(Fore.GREEN + '   𝒮𝒾𝓈𝓉𝑒𝓂𝒶 𝒹𝑒 𝒢𝑒𝓇𝑒𝓃𝒸𝒾𝒶𝓂𝑒𝓃𝓉𝑜 𝒟𝑒𝓂𝑜𝑔𝓇á𝒻𝒾𝒸𝒐 ')
    print(Fore.CYAN + '=' * 43 + Style.RESET_ALL)
    print('1. Adicionar cidade')
    print('2. Exibir cidade mais extensa')
    print('3. Exibir cidade mais populosa')
    print('4. Calcular média de população')
    print('5. Exibir todas as informações das cidades')
    print('6. Limpar todos os dados')
    print('7. Sair')
    print(Fore.CYAN + '=' * 43 + Style.RESET_ALL)

def adicionar_cidade():
    if len(nomes_cidades) <= 100:
        nome = input('Digite o nome da cidade: ')
        populacao = int(input('Digite a população: '))
        area = float(input('Digite a área (em km²): '))

        nomes_cidades.append(nome)
        populacoes.append(populacao)
        areas.append(area)

        salvar_dados()

        print(Fore.GREEN + '\nSalvando Dados', end='')
        for _ in range(3):
            time.sleep(0.3)
            print(Fore.GREEN + '.', end='')
    else:
        print(Fore.RED + 'Limite de 100 cidades alcançado. Não é possível adicionar mais cidades.')

def exibir_cidade_extensa():
    if areas:
        max_area = max(areas)
        indice_max_area = areas.index(max_area)
        print(Fore.MAGENTA + f'\nA cidade mais extensa é "{nomes_cidades[indice_max_area]}" com uma área de {formatar_area(max_area)} km².\n')
    else:
        print(Fore.RED + '\nNenhuma cidade cadastrada.\n')

def exibir_cidade_populosa():
    if populacoes:
        max_populacao = max(populacoes)
        indice_max_populacao = populacoes.index(max_populacao)
        print(Fore.MAGENTA + f'\nA cidade mais populosa é "{nomes_cidades[indice_max_populacao]}" com uma população de {formatar_numero(max_populacao)} habitantes.\n')
    else:
        print(Fore.RED + '\nNenhuma cidade cadastrada.\n')

def calcular_media_populacao():
    if populacoes:
        media_populacao = sum(populacoes) / len(populacoes)
        print(Fore.CYAN + f'\nA média de população entre as cidades cadastradas é de {formatar_numero(media_populacao)} habitantes.\n')
    else:
        print(Fore.RED + '\nNenhuma cidade cadastrada.\n')

def exibir_todas_cidades():
    if nomes_cidades:
        print(Fore.BLUE + '\nInformações de todas as cidades cadastradas:\n' + '=' * 43)
        for i in range(len(nomes_cidades)):
            print(f'{Fore.YELLOW}Cidade: {nomes_cidades[i]}')
            print(f'População: {formatar_numero(populacoes[i])}')
            print(f'Área: {formatar_area(areas[i])} km²')
            print(Fore.BLUE + '-' * 43)
    else:
        print(Fore.RED + '\nNenhuma cidade cadastrada.\n')

def limpar_dados():
    global nomes_cidades, populacoes, areas
    nomes_cidades, populacoes, areas = [], [], []
    salvar_dados()
    print(Fore.RED + 'Todos os dados foram apagados com sucesso.\n')

def sair_sistema():
    print(Fore.GREEN + '\nSaindo do sistema', end='')
    for _ in range(3):
        time.sleep(0.5)
        print(Fore.GREEN + '.', end='')
    print('\n')
    return False

continuar = True
primeira_vez = True

carregar_dados()

while continuar:
    exibir_mensagem_inicial(primeira_vez)
    primeira_vez = False

    exibir_arte()
    carregar_menu()
    exibir_menu()

    opcao = input(Fore.YELLOW + '\nEscolha uma opção (1-7): ' + Style.RESET_ALL)
    limpar_tela()

    match opcao:
        case '1':
            adicionar_cidade()
        case '2':
            exibir_cidade_extensa()
        case '3':
            exibir_cidade_populosa()
        case '4':
            calcular_media_populacao()
        case '5':
            exibir_todas_cidades()
        case '6':
            limpar_dados() 
        case '7':
            continuar = sair_sistema()
        case _:
            print(Fore.RED + '\nOpção inválida. Tente novamente!')
