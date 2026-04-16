# if / elif / else
# se / senão se / senão

entrada = input("Você quer entrar ou sair? ").strip().casefold()

if entrada == "entrar":
    print("Você entrou!")
elif entrada == "sair":
    print("Você saiu!")
else:
    print("Entrada inválida!")
