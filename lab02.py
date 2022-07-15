canal = input("")
N = int(input(""))


views_18 = []
views_19 = []
views_20 = []

i = 0

while i < N:
    data_1 = input()
    views = int(input())

    data = data_1.split('-')

    if int(data[0]) == 2018:
        views_18.append(views)

    if int(data[0]) == 2019:
        views_19.append(views)

    if int(data[0]) == 2020:
        views_20.append(views)

    i += 1

x = 0
y = 0
z = 0

for a in views_18:
    x += a

med_18 = x/(len(views_18))

media_18 = format(med_18, '.2f')


for a in views_19:
     y += a

med_19 = y/(len(views_19))


media_19 = format(med_19, '.2f')

for a in views_20:
    z += a

med_20 = z/(len(views_20))

media_20 = format(med_20, '.2f')

total = x + y + z

if total != 0:
    percent_18 = 100*x/total
    percent_19 = 100*y/total
    percent_20 = 100*z/total

elif total == 0:
    percent_18 = percent_19 = percent_20 = "indeterminada"

media_total = (x + y + z)/(len(views_18) + len(views_19) + len(views_20))



print("Canal:", canal)
print("Total de views do trienio:", total)
print("Media de views do trienio:", format(media_total, ".2f"))

print("")

print("2018")
print("Total:", x)
if percent_18 == "indeterminada":
    print("Porcentagem das views do trienio: indeterminada")
else:
    print("Porcentagem das views do trienio:", format(percent_18, ".2f"))
print("Media:", media_18)

print("")

print("2019")
print("Total:", y)
if percent_19 == "indeterminada":
    print("Porcentagem das views do trienio: indeterminada")
else:
    print("Porcentagem das views do trienio:", format(percent_19, ".2f"))
print("Media:", media_19)

print("")

print("2020")
print("Total:", z)
if percent_20 == "indeterminada":
    print("Porcentagem das views do trienio: indeterminada")
else:
    print("Porcentagem das views do trienio:", format(percent_20, ".2f"))
print("Media:", media_20)









