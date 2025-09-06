# Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro (2017). Depois mostre
# Apenas os cinco primeiros colocados
# Os últimos 4 colocados
# Uma lista com os times em ordem alfabética
# Em que posição tabela está o tima da chapecoense (ou qualquer time)

seria_A_2017 = ('Corinthians',
                'Palmeiras',
                'Santos',
                'Grêmio',
                'Cruzeiro',
                'Flamengo',
                'Vasco da Gama',
                'Chapecoense',
                'Atlético-MG',
                'Botafogo',
                'Athletico-PR',
                'Bahia',
                'São Paulo',
                'Fluminense',
                'Sport Recife',
                'EC Vitória',
                'Coritiba',
                'Avaí',
                'Ponte Preta',
                'Atlético-GO')

print('\nAnálise Básica do Brasileirão Séria A de 2017!\n')

print('========== Todos os times do Campeonato (Ordem Alfabética) ==========')
times_ordenados = tuple(sorted(seria_A_2017))
for cont in range(0, len(times_ordenados)):
    print(f'{times_ordenados[cont]}')

print('\n========== Classificação Final ==========')
for cont in range(0, len(seria_A_2017)):
    print(f'{cont}) {seria_A_2017[cont]}')

print('\n========== Classificados para Libertadores da América ==========')
for cont in range(0, 5):
    print(f'{cont + 1}) {seria_A_2017[cont]}')

print('\n========== Rebaixados para série B ==========')
for cont in range(len(seria_A_2017) - 1, len(seria_A_2017) - 5, -1):
    print(f'{cont + 1}) {seria_A_2017[cont]}')

escolha = ''
while escolha not in (seria_A_2017):
    escolha = str(input('\nDigite o nome de um time: ')).strip().title()
    if escolha not in (seria_A_2017):
        print('Opção inválida! Digite novamente..')

for cont in range(0, len(seria_A_2017)):
    if escolha == seria_A_2017[cont]:
        print(f"O time {escolha} acabou o campeonato na {cont+1}º posição!")
