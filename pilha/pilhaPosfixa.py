class Pilha:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def top(self):
        if not self.is_empty():
            return self.items[-1]


def calcular_expressao_posfixa(expressao_posfixa):
    pilha = Pilha()

    for caractere in expressao_posfixa:
        if caractere.isdigit():
            pilha.push(int(caractere))
        else:
            operando2 = pilha.pop()
            operando1 = pilha.pop()

            if caractere == '+':
                resultado = operando1 + operando2
            elif caractere == '-':
                resultado = operando1 - operando2
            elif caractere == '*':
                resultado = operando1 * operando2
            elif caractere == '/':
                resultado = operando1 / operando2

            pilha.push(resultado)

    resultado_final = pilha.top()
    pilha.pop()

    return resultado_final

expressao_posfixa = "23*5+"
resultado = calcular_expressao_posfixa(expressao_posfixa)
print("resultado da expressão posfixa:", resultado)
