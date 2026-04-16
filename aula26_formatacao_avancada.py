# Formatação básico de strings
# s - string
# d e i - int
# f - float
# x e X - Hexadecimal (base 16)
# .<número de dígitos>f - quantidade de casas decimais para float
# (Caractere) (> ou < ou ^) (Quantidade de caracteres) (Tipo - s, d, f, x, X)
# > - Alinhado à direita (padrão)
# < - Alinhado à esquerda
# ^ - Centralizado
# Sinal - + ou - ou espaço
# Ex.: 0>-100, .1f
# Conversation Flags - !r !s !a

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')  # Alinhado à direita
print(f'{variavel: <10}')  # Alinhado à esquerda
print(f'{variavel: ^10}')  # Centralizado
print(f'{variavel:0>10}')  # Preenchido com zeros e alinhado à direita
print(f'{variavel:!^20}')  # Centralizado e preenchido com !
print(f'{variavel:.>10}')  # Preenchido com . e alinhado à direita
print(f'{variavel:.<10}')  # Preenchido com . e alinhado
# à esquerda
print(f'{variavel:.^10}')  # Preenchido com . e centralizado
print(f'{variavel:0<10}')  # Preenchido com zeros e alinhado à esquerda
print(f'{variavel:0^10}')  # Preenchido com zeros e centralizado
print(f'{variavel:0>10.2}')  # Preenchido com zeros
# Alinhado à direita e com apenas 2 caracteres
print(f'{variavel:0<10.2}')  # Preenchido com zeros
# Alinhado à esquerda e com apenas 2 caracteres
print(f'{variavel:0^10.2}')  # Preenchido com zeros
# Centralizado e com apenas 2 caracteres

