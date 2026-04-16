# Operadores Lógicos
# and, or, not
# and - todas as condições precisam ser verdadeiras
# or - uma ou outra condição precisa ser verdadeira
# not - inverte o resultado, ou seja, torna verdadeiro em falso e vice-versa
# Se qualquer valor for considerado falso, a expressão inteira será avaliada como falsa.
# São considerados falsy os seguintes valores: None, False, 0, 0.0, 0j, Decimal(0), Fraction(0, 1), [], (), {}, set(), range(0)
# Também existe o tipo None que é utilizado para representar a ausência de valor, ou seja, quando uma variável não tem um valor atribuído. O None é considerado falsy, ou seja, é avaliado como falso em contextos booleanos.

entrada = input('[E]ntrar [S]air: ').strip().casefold()

if entrada == 's':
    print('Você saiu!')
elif entrada == 'e':
    senha_permitida = '123456'
    senha_digitada = input('Digite a senha de acesso: ')
    if senha_digitada == senha_permitida:
        print('Você entrou com sucesso! ')
    else:
        print('Senha incorreta, tente novamente!')
else:
    print('Entrada inválida, tente novamente.')
