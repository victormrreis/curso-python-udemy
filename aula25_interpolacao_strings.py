# Interpolação básica de strings
# s - string
# d e i - int
# f - float
# x e X - Hexadecimal (base 16)

nome = 'Maria'
preco = 1000.95897643
variavel = '%s, o preço total foi de R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %08X' % (255, 255))
