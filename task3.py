# На вход программе подается строка с названиями городов,
# записанных в одну строчку через пробел.
# Необходимо ее прочитать и применить функцию map так,
# чтобы она возвращала названия городов только длиной
# более 5 символов. Вместо остальных названий - строку
# с дефисом ("-").

# Пример:
# Москва Уфа Вологда Тула Владивосток Хабаровск
# Результат:
# Москва - Вологда - Владивосток Хабаровск

# P.S. Очевидно, функцию для передачи в map нужно сделать самому.

s = "Москва Уфа Вологда Тула Владивосток Хабаровск"

res = ''


def func(x: str):
    global res
    if res != '':
        res += " "
    if len(x)<= 5:
        x = '-'
    res += x
    return res


res_lst = list(map(func, s.split()))

print(res_lst[-1:][0])
