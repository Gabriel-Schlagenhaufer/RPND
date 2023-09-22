from sympy import sympify, symbols, compose

# entradaf = input("Digite a funcao f(X): ")
# entradag = input("Digite a funcao g(X): ")

# exemplo 1
# entradaf = "x^2"
# entradag = "x - 1"

# exemplo 2
# entradaf = "(x^2) + 1"
# entradag = "2*x - 3"

# exemplo 3
entradaf = "5*x + 2"
entradag = "x + 3"

equacaof = sympify(entradaf)
equacaog = sympify(entradag)

x = symbols('x')

funcaof = lambda x_value: equacaof.subs(x, x_value)
funcaog = lambda x_value: equacaog.subs(x, x_value)

valor = input("Valor: ")

print(f"g o f: {funcaog(funcaof(valor))}\t{str(compose(equacaog, equacaof)).replace('**', '^')}")
print(f"f o f: {funcaof(funcaof(valor))}\t{str(compose(equacaof, equacaof)).replace('**', '^')}")
print(f"g o g: {funcaog(funcaog(valor))}\t{str(compose(equacaog, equacaog)).replace('**', '^')}")
print(f"f o g: {funcaof(funcaog(valor))}\t{str(compose(equacaof, equacaog)).replace('**', '^')}")