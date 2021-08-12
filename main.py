import time

'Нахождение делителей числа'
def dev_collection(a):
    m = []
    i = 1
    while i < a:
        if a % i == 0:
            m.append(i)
        i += 1
    return m

'Получение суммы всех делителей'
def num_sum(m):
    s = 0
    for i in m:
        s += i
    return s

'Фиксированный вывод'
def to_fixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"


fstNum = 2
provMas = []

'fstNum  - первое дружественное число'
'scndNum - второе дружественное число'
'z       - коллекция чисел'
'a       - проверка суммы делителей второго числа'

'Таймер для отслеживания времени поиска пары'
startTime = time.time()

while fstNum < 100000000000:
    z = dev_collection(fstNum)
    scndNum = num_sum(z)

    z = dev_collection(scndNum)
    secondSum = num_sum(z)

    if secondSum == fstNum and scndNum != fstNum and scndNum not in provMas:
        print("\033[32m{0} and {1} (in {2} sec)".format(fstNum, scndNum, to_fixed(time.time() - startTime, 4)))
        startTime = time.time()
        provMas.append(fstNum)

    fstNum += 1
