def imprimir(mensaje):
	print(mensaje)

def imprimirLista(l):
	print(list(l*2))

def sumar(a,b):
	c = a+b
	return c


if __name__ == "__main__":
	impimir("hola mundo")
	imprimirLista(range(5))
	print(sumar(5,4))
