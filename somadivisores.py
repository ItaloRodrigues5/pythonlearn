def soma_divisores(x):

  count = 1
  somadivisaopositivo = 0
  somadivisaonegativo = 0

  if x < 0:
    conversor = (-1) * x
    while count < conversor:
      if conversor % count == 0:
        somadivisaonegativo += count

      count += 1

      conversor

  elif x > 0:
    while count < x:

      if x % count == 0:
        somadivisaopositivo += count

      count += 1

  if x > 0:
    return somadivisaopositivo

  elif x < 0:
    return (somadivisaonegativo * (-1))

  else:
    return 0

def main():

  x = int(input())

  print(soma_divisores(x))

main()
