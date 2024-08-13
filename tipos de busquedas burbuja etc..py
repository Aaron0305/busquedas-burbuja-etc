import random

class SortingAlgorithms:
    @staticmethod
    def bubble_sort(arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]

    @staticmethod
    def quick_sort(arr):
        if len(arr) <= 1:
            return arr
        else:
            pivot = arr[0]
            menores = [x for x in arr[1:] if x <= pivot]
            mayores = [x for x in arr[1:] if x > pivot]
            return SortingAlgorithms.quick_sort(menores) + [pivot] + SortingAlgorithms.quick_sort(mayores)

    @staticmethod
    def shell_sort(arr):
        n = len(arr)
        brecha = n // 2

        while brecha > 0:
            for i in range(brecha, n):
                temp = arr[i]
                j = i
                while j >= brecha and arr[j - brecha] > temp:
                    arr[j] = arr[j - brecha]
                    j -= brecha
                arr[j] = temp
            brecha //= 2

    @staticmethod
    def counting_sort(arr, exp):
        n = len(arr)
        salida = [0] * n
        conteo = [0] * 10

        for i in range(n):
            index = arr[i] // exp
            conteo[index % 10] += 1

        for i in range(1, 10):
            conteo[i] += conteo[i - 1]

        i = n - 1
        while i >= 0:
            index = arr[i] // exp
            salida[conteo[index % 10] - 1] = arr[i]
            conteo[index % 10] -= 1
            i -= 1

        for i in range(n):
            arr[i] = salida[i]

    @staticmethod
    def radix_sort(arr):
        maximo = max(arr)
        exp = 1

        while maximo // exp > 0:
            SortingAlgorithms.counting_sort(arr, exp)
            exp *= 10

    @staticmethod
    def print_menu():
        print("\nSeleccione un método de ordenamiento:")
        print("1. Burbuja")
        print("2. Quicksort")
        print("3. ShellSort")
        print("4. Radix")
        print("5. Salir")

    @staticmethod
    def main():
        while True:
            try:
                # Tamaño del arreglo ingresado por el usuario
                n = int(input("Ingrese el tamaño del arreglo (por ejemplo, 100000): "))
                if n <= 0:
                    raise ValueError("El tamaño del arreglo debe ser un número positivo.")
            except ValueError as e:
                print(f"Error: {e}")
                continue

            # Genera un arreglo de n elementos no repetidos
            arr = random.sample(range(1, n+1), n)

            while True:
                SortingAlgorithms.print_menu()
                opcion = input("Ingrese el número de la opción deseada: ")

                if opcion == "1":
                    arr_bubble = arr.copy()
                    SortingAlgorithms.bubble_sort(arr_bubble)
                    print("Burbuja:", arr_bubble[:10])

                elif opcion == "2":
                    arr_quick = arr.copy()
                    arr_quick = SortingAlgorithms.quick_sort(arr_quick)
                    print("Quicksort:", arr_quick[:10])

                elif opcion == "3":
                    arr_shell = arr.copy()
                    SortingAlgorithms.shell_sort(arr_shell)
                    print("ShellSort:", arr_shell[:10])

                elif opcion == "4":
                    arr_radix = arr.copy()
                    SortingAlgorithms.radix_sort(arr_radix)
                    print("Radix:", arr_radix[:10])

                elif opcion == "5":
                    print("Saliendo del programa.")
                    return

                else:
                    print("Opción no válida. Por favor, elija una opción válida.")

if __name__ == "__main__":
    SortingAlgorithms.main()
