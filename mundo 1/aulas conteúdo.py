#AULA 6 tipos primitivos de variáveis

int(inteiro = (7 -4 0 9875) #números inteiros sem vírgula sendo negativos, positivos ou nulos
float(float = (1.24 3.65 -13.5 3,14)) #números com vírgula sendo negativos, positivos ou nulos
bool(bool = () #operadores lógicos sendo verdadeiro e falso
str(str = 'texto') #apenas texto

print(type(inteiro)) #para verificar a tipo de variável utilizar o comando type como no exemplo

n1 = int(input('numero 1'))
n2 = int(input('numero 2'))
s = n1 + n2
print('a soma entre', n1, 'e', n2, 'vale', s) #forma pouco usual de se fazer um print com várias variáveis, segue abaixo exemplo com o .format
print('a soma entre {0} e {1} vale {2}'.format(n1, n2, s)) #números nos colchetes para especificar a ordem, poré nesta situação não é necessário

print(s,isnumeric()) #is é como se um fosse um "É" usado neste exemplo para verificar se o valor digitado pelo usuário é numérico

#AULA 7 operadores aritméticos

+ #é soma
- #é subtração
* #é multiplicação
/ #é divisão
** #é potência(um numero elevado a outro)
// #é divisão inteira (divisão sem vírgula)
% #é o resto da divisão

#ORDEM DE PRECEDÊNCIA

#primeiro colchetes ()
#segundo potências **
#terceiro multiplicação *, divisão /, divisão interia //, resto da divisão %,
#quarto soma + e subtração
#quando se tem mais de uma operação na ordem o código fará a que aparecer primeiro como no 3 caso

#exemplos de print
nome = input('digite seu nome')
n1 = input('digite algo')
n2 = input('digite algo')
print('prazer em te conhecer {:>20}'.format(nome))
print('prazer em te conhecer {:><20}'.format(nome))
print('prazer em te conhecer {:^20}'.format(nome))
print('prazer em te conhecer {:=^20}'.format(nome), end='') #este end vai fazer com que a linha não se quebre!!!
print('o valor 1 é {} \n o valor 2 é \n {} a soma é {}')

# Solicita ao usuário a quantidade de reais na carteira
reais = float(input("Digite a quantidade de reais que você tem na carteira: "))

# Define a taxa de câmbio fictícia (substitua pela taxa atual)
taxa_cambio = 5.3  # Exemplo: 1 real = 5.3 dólares

# Calcula a quantidade de dólares que podem ser comprados
dolares = reais / taxa_cambio

# Exibe o resultado
print(f"Com {reais} reais, você pode comprar aproximadamente {dolares:.2f} dólares.")

#AULA 8
