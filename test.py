def imprimir(mensaje):
	print(mensaje)

def imprimirLista(l):
	print(list(l*2))

def quicksort(arr):
	if len(arr) <= 1:
		return arr
	else:
		pivot = arr[0]
		left = [x for x in arr[1:] if x < pivot]
		right = [x for x in arr[1:] if x >= pivot]
		return quicksort(left) + [pivot] + quicksort(right)

if __name__ == "__main__":
	impimir("hola mundo")
	imprimirLista(range(5))

