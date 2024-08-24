def remove_caracteres(lista):
  count = 0

  while count < len(lista):
    #print(type(lista[count]))
    if type(lista[count]) == str:
      lista.remove(lista[count])
    else:
      count += 1
  return lista

lista = [70, 2, 1, '1', '2', '3', 45, 2, 4, '4', 'b', 'd', 30, 65]

x = remove_caracteres(lista)

print(x)
