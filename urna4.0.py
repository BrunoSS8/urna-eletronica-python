class UrnaEletronica:
    def __init__(self):
        self.candidatos = []

    def adicionar_candidato(self, nome, partido):
        candidato = {'nome': nome, 'partido': partido, 'votos': 0}
        self.candidatos.append(candidato)

    def votar(self, indice):
        if indice == -1:
            print('Voto em branco registrado.')
        elif indice < 0 or indice >= len(self.candidatos):
            print('Voto nulo registrado.')
        else:
            self.candidatos[indice]['votos'] += 1
            print('Voto registrado com sucesso!')

    def exibir_candidatos(self):
        for indice, candidato in enumerate(self.candidatos):
            print(f"{indice+1}: {candidato['nome']} ({candidato['partido']})")

    def exibir_votacao(self):
        total_votos = sum(candidato['votos'] for candidato in self.candidatos)
        print(f"Total de votos: {total_votos}")
        for candidato in self.candidatos:
            print(f"{candidato['nome']} ({candidato['partido']}): {candidato['votos']} votos ({candidato['votos']/total_votos*100:.2f}%)")

# Teste da classe UrnaEletronica com interação do usuário
urna = UrnaEletronica()

# Adicionando candidatos
urna.adicionar_candidato('João', 'Partido A')
urna.adicionar_candidato('Maria', 'Partido B')
urna.adicionar_candidato('Pedro', 'Partido A')

while True:
    # Exibindo menu
    print('\nEscolha uma opção:')
    print('1: Exibir candidatos')
    print('2: Votar')
    print('3: Exibir resultado da votação')
    print('a: Adicionar candidato')
    print('0: Sair')

    opcao = input('Digite sua opção: ')
    if opcao == '1':
        urna.exibir_candidatos()
    elif opcao == '2':
        while True:
            voto = input('Digite o número do candidato em quem deseja votar (ou 0 para voto em branco, ou -1 para encerrar a votação): ')
            try:
                voto = int(voto)
            except ValueError:
                print('Digite um número válido!')
                continue

            if voto == -1:
                break

            urna.votar(voto-1)
    elif opcao == '3':
        urna.exibir_votacao()
    elif opcao == 'a':
        nome = input('Digite o nome do candidato: ')
        partido = input('Digite o partido do candidato: ')
        urna.adicionar_candidato(nome, partido)
    elif opcao == '0':
        break
    else:
        print('Opção inválida! Digite novamente.')
