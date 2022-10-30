 def errorCheck(n):
    try:
        n = int(n)
    except Exception:
        return -1
    return n
   def Vvod(h, p):
    n = 0
    if h == 1:
        while n == 0:
            n = input(f'Введите координату от 1 до 8 по горизонтали для клетки {p}\n')
            n = errorCheck(n)
            if (n > 8) or (n < 1):
                print('Ошибка ввода. Введите цифру от 1 до 8\n')
                n=0
        return n
    else:
        while n == 0:
            n = input(f'Введите координату от 1 до 8 по вертикали для клетки {p} \n')
            n = errorCheck(n)
            if (n > 8) or (n < 1):
                print('Ошибка ввода. Введите цифру от 1 до 8\n')
                n=0
        return n

            
