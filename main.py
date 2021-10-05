valorVaga = 10

corredor1=[1,1,1,0,1,0]
corredor2=[0,0,1,0,1,0]
corredor3=[1,1,0,1,0,1]
corredor4=[0,0,0,1,0,0]
corredor5=[0,0,0,0,0,0]
corredor6=[0,1,0,1,0,1]
corredor7=[1,0,1,0,0,0]
corredor8=[0,1,0,1,1,0]
corredor9=[1,0,1,0,1,0]

andar1=[corredor1, corredor2, corredor3]
andar2=[corredor4, corredor5, corredor6]
andar3=[corredor7, corredor8, corredor9]

edGaragem=[andar1, andar2, andar3]

num_andar=int(input('informe o numero do andar: '))
num_corredor=int(input('informe um numero do corredor: '))

totalCorredor=edGaragem[num_andar][num_corredor]
print('Total de vagas do corredor ', num_corredor, ' = ', totalCorredor.count(1))

get_andar=edGaragem[num_andar]
total_vagas=0

for corredor in get_andar:
    total_vagas += corredor.count(0)
print('Total de vagas do andar    ', num_andar, ' = ', total_vagas)

vagas = 0
contador = 0
indice_andar = 0

for andar in edGaragem:
    total = 0
    for corredor in andar:
        total += corredor.count(0)
    if vagas <= total:
        vagas = total
        indice_andar = contador
    contador += 1

print('Andar mais livre = ', indice_andar)
for ed in edGaragem[indice_andar]:
    print(ed)

print('\nAndares ordenandos por vagas.')
edGaragemOrden = sorted(edGaragem)
for edO in edGaragemOrden:
    print(edO)

faturamento = 0;
for ed in edGaragem:
    for e in ed:
        faturamento += e.count(1)

print('\nVagas ocupadas do edificio:', faturamento)
faturamento = (faturamento * valorVaga)
print('Faturamento = ', faturamento)