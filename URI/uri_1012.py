valor = input().split()
pi = 3.14159

area_triangulo = (float(valor[0]) * float(valor[2])) / 2
area_circulo = pi * (float(valor[2]) ** 2)
area_trapezio = ((float(valor[0]) + float(valor[1])) * float(valor[2])) / 2
area_quadrado = float(valor[1]) ** 2
area_retangulo = float(valor[0]) * float(valor[1])

print("TRIANGULO: {:.3f}".format(area_triangulo))
print("CIRCULO: {:.3f}".format(area_circulo))
print("TRAPEZIO: {:.3f}".format(area_trapezio))
print("QUADRADO: {:.3f}".format(area_quadrado))
print("RETANGULO: {:.3f}".format(area_retangulo))
