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
    def diag(n,m,i,k):
        k1=k
        i1=i
        while k1!=8 and i1!=8:
            i1=i1+1
            k1=k1+1
            if k1==m and i1==n:
                return 1
                
        k1=k
        i1=i
        while k1!=1 and i1!=1:
            i1=i1-1
            k1=k1-1
            if k1==m and i1==n:
                return 1
                
        k1=k
        i1=i
        while k1!=8 and i1!=1:
            i1=i1-1
            k1=k1+1
            if k1==m and i1==n:
                return 1
                
        k1=k
        i1=i
        while k1!=1 and i1!=8:
            i1=i1+1
            k1=k1-1
            if k1==m and i1==n:
                return 1
        return 0
k = Vvod(1, 1)
i = Vvod(2, 1)
m = Vvod(1, 2)
n = Vvod(2, 2)
print(f'Клетка 1: ({k},{i}); Клетка 2: ({m},{n})')
if ((i+k+m+n) % 2 == 0):
    print ('(А) Клетки одного цвета\n')
    same=1
else:
    print('(А) Клетки разных цветов\n')
    same=0           
e=0

while e == 0:
    fig=int(input(""""Какая фигура расположена в клетке 1? Для выбора введите соответствующую цифру
              1 - ферзь
              2 - ладья
              3 - слон
              4 - конь\n"""))
    fig = errorCheck(fig)
    if (fig > 4) or (fig < 1):
        print('Ошибка ввода. Введите цифру от 1 до 4\n')
        e=0
    else:
        e=1
res=0
attack=0
end=0
