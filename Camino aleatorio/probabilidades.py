import random


def tirar_dado(numero_de_tiros):
    secuencia_de_tiros = []


    for _ in range(numero_de_tiros):
        tiro_1 = random.choice([1, 2, 3, 4, 5, 6])
        tiro_2 = random.choice([1, 2, 3, 4, 5, 6])
        suma_de_tiros = tiro_1 + tiro_2
        secuencia_de_tiros.append(suma_de_tiros)

    return secuencia_de_tiros


def main(numero_de_tiros, numero_de_intentos):
    tiros = []
    for _ in range(numero_de_intentos):
        secuencia_de_tiros = tirar_dado(numero_de_tiros)
        tiros.append(secuencia_de_tiros)

    
    tiros_con_12 = 0

    for tiro in tiros:
        if 12 in tiro:
           tiros_con_12 += 1

    probabilidad_tiros_con_12 = tiros_con_12 / numero_de_intentos
    print(f'Probabilidad de obtener por lo menos un 12 en {numero_de_tiros} tiros = {probabilidad_tiros_con_12}')


if __name__ == "__main__":
    numero_de_tiros = int(input('Cuantos tiros de dado:  '))
    numero_de_intentos = int(input('Cuantas veces correra la simulacion: '))
    
    main(numero_de_tiros, numero_de_intentos)


    

    



