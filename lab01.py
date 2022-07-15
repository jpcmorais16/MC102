material = input()
Tf_1 = float(input())
Teb_1 = float(input())
T_1 = float(input())

a = (5/9)*(T_1 - 32)

T = round(a, 2)

Tf = round(Tf_1, 2)

Teb = round(Teb_1, 2)

if T >= Teb:
    estado = "Gasoso"

elif T < Tf:
    estado = "Solido"

else:
    estado = "Liquido"

print("Material:", material)

print("Ponto de fusao (Celsius):", format(Tf, '.2f'))

print("Ponto de ebulicao (Celsius):", format(Teb, '.2f'))

print("Temperatura atual (Celsius):", format(T, '.2f'))

print("Estado fisico do material:", estado)



