nome = input('Digite seu nome: ')
idade_input = input('Digite sua idade: ') 
alergia_medicamento = input('Você tem alergia a algum medicamento? [S/N] ').strip().casefold()

if not idade_input.isdigit():
    print('Idade inválida. Por favor, digite apenas números.')
elif not alergia_medicamento in ['s', 'n']:
    print('Resposta inválida para a pergunta sobre alergia a medicamentos.')
else:
    idade = int(idade_input) 
    if alergia_medicamento == 's' or idade < 18:
        print(f'{nome}, infelizmente você não pode participar do estudo.')
    else:
        print(f'{nome}, você pode participar do estudo.')