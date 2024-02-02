def primo (n):
    for num in range(2, n):
        if n % num == 0:
            print("No es primo")
            return False
        else:
            print("Es primo")
            return True