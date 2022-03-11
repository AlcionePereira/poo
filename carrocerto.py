class Carro:
    '''Classe que vai fazer comandos no carro'''
    #método construtor da classe
    def __init__(self,nome , ano, cor, veloc_max, veloc_atual, estado):
        self.nome = nome
        self.ano = ano
        self.cor = cor
        self.veloc_max = 80
        self.veloc_atual = 20
        self.estado = 'estado'

    def carro_antigo(self):
        self.estado = 'LIGADO'
        print(f'O carro é um {self.nome} ano {self.ano} de cor {self.cor} sua velocidade máxima é {self.veloc_max}km/h e velocidade atual {self.veloc_atual}km/h estado {self.estado}')


    def carro_chique(self):
        self.estado = 'DESLIGADA'
        print(f'O carro é uma {self.nome} ano {self.ano} cor {self.cor} velocidade máxima de {self.veloc_max}km/h velocidade mínima {self.veloc_atual}km/h está {self.estado} ')



teste = Carro('fusca', 1965, 'preto', 80, 20, 'LIGADO')
carão = Carro('Ferrari', 2014, 'vermelho', 300, 0, 'DESLIGADA')


carro = input('Escolha o carro que vai dirigir: ').lower()

#comandos do fusca
#O fusca começa em estado LIGADO
if carro == 'fusca':
    print('*** Ótimo, Você escolheu o FUSCA. \n')
    c = teste.carro_antigo()
    ação = input('Qual comando vai excecutar? ')

    if ação == 'desligar':
        print('Seu fusca foi desligado. \n')
        ação = input('Qual comando vai excecutar? ')

    if ação == 'ligar':
        print('Seu Fusca já está ligado.\n')
        ação = input('Qual comando vai excecutar? ')


    if ação == 'acelerar':
        print('Seu Fusca vai começar acelerar \n')
        velocidade = int(input('Qual velocidade você deseja? '))
        while velocidade > 80:
            print('Você ultrapassou a velocidade MÁXIMA permitida de 80km/h \n')
            velocidade = int(input('Digite novamente qual velocidade deseja: '))
        print(f'Seu fusca está na velocidade {velocidade}km/h')

    ação = input('Se deseja desligar o carro digite desligar: ').lower()

    if ação == 'desligar':
        print('Seu fusca foi desligado. \n FIM DO PROGRAMA.')
    else:
        print('Obrigada por faz o fusquinha funcionar. \n PROGRAMA CHEGOU AO FIM.')


#Comandos da ferrari
#A Ferrari começa em estado desligado

if carro ==  'ferrari':
    print('*** Muito bem, você vai dirigir uma FERRARI.\n')
    carro_massa = carão.carro_chique()
    ação = input('\n Qual comando vai excecutar? ')

    #se úsuario pedir para acelerar antes de ligar a Ferrari
    if ação == 'acelerar':
        print('Sua Ferrari está desligada, você precisa liga-ló para acelerar.')
        ação = input('Qual comando vai excecutar? ')

    #se úsuario pedir para desligar antes de ligar a Ferrari
    if ação == 'desligar':
        print('Sua Ferrari já está desligada.')
        ação = input('Qual comando vai excecutar? ')
    
    if ação == 'ligar':
        print('Vamos lá, sua Ferrari foi ligada.')
        ação = input('***Qual comando vai excecutar?\n ')
        if ação == 'acelerar':
            print('    Sua Ferrari vai acelerar. \n')
            velocidade = int(input('***Qual velocidade você deseja?\n '))
            while velocidade > 300:
                print('Velocidade MÁXIMA permitida é 300km/h')
                velocidade = int(input('***Digite novamente qual velocidade deseja: '))
            print(f'Sua Ferrari está na velocidade {velocidade}km/h')

        ação = input('Se deseja desliga sua Ferrari digite desligar:  ')
        if ação == 'desligar':
           print('Sua Ferrari já está desligada.')
        else:
            print('Obrigada por faz a Ferrari funcionar. \n PROGRAMA CHEGOU AO FIM.')

        





