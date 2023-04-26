print('╔══════════════════════════════════╗')
print('║           CALCULADORA            ║')
print('╚══════════════════════════════════╝')

print('\n╔══════════════════════════════════╗')
print('        OPERAÇÕES DISPONÍVEIS:     ')
print('         +  -  *  /  r  p  m       ')
print('╚══════════════════════════════════╝')
operacao = input('\n╔══════════════════════════════════╗\n   Digite a operação desejada: ')

if operacao != 'm':
  x = float(input('\n     Digite o primeiro valor: '))

# Verifica se é uma operação que requer um segundo valor
if (operacao != 'r' and operacao != 'm'):
    y = float(input('     Digite o segundo valor: '))
    print('╚══════════════════════════════════╝')

# Realiza a operação selecionada
if operacao == '+':
    resultado = x + y
elif operacao == '-':
    resultado = x - y
elif operacao == '*':
    resultado = x * y
elif operacao == '/':
    resultado = x / y
elif operacao == 'r':
    resultado = x ** 0.5
elif operacao == 'p':
    resultado = x ** y
elif operacao == 'm':
  n = int(input("  Quantidade de valores da média: "))

  soma = 0
  for i in range(n):
      valor = float(input("        Digite o valor {}: ".format(i+1)))
      soma += valor

  resultado = soma / n
  print('╚══════════════════════════════════╝')
else:
    print('\n╔══════════════════════════════════╗')
    print('║        OPERAÇÃO INVÁLIDA         ║')
    print('╚══════════════════════════════════╝')
    resultado = None

# Imprime o resultado formatado com 2 casas decimais, se existir
if resultado is not None:
    print('\n╔══════════════════════════════════╗')
    print('        O RESULTADO É: {:.2f}        '.format(resultado))
    print('╚══════════════════════════════════╝')
