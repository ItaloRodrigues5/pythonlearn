def soma_primos(a, b):

  soma = 0
  num = 0

  if a > b:
    num = b + 1

    for i in range(num, a):
      for j in range(2, i):
        if i % j == 0:
          break
      else:
        soma += i

  if b > a:
    num = a + 1

    for i in range(num, b):
      for j in range(2, i):
        if i % j == 0:
          break
      else:
        soma += i

    return soma


def main():

  print(soma_primos(10, 20))

main()
