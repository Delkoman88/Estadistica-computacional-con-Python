import random
import collections
from estadisticas import  media, desviacion_estandar
from bokeh.plotting import figure, show, output_file


def tirar_dado(numero_de_veces):

    tiros = []

    for _ in range(numero_de_veces):
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        tiro = dado1 + dado2
        tiros.append(tiro)

    return tiros

def statistics(numero_de_tiros):

    tiros = tirar_dado(numero_de_tiros)
    

    media_tiros = media(tiros)

    sigma = desviacion_estandar(tiros)


    return (media_tiros , sigma)
    #counter = dict(collections.Counter(tiros))
    #print(counter)
    
def graficar(x, y):

    fig = figure(title='Dist. normal dados')
    fig.vbar(x, top = y, width = 0.001)
    output_file('dist_dados.htm')
    show(fig)

    
    #print(x)
    #print(y)
    
    

def main(numero_de_tiros, numero_de_intentos):

    media_de_tiros = []

    for _ in range(numero_de_intentos):

        media_tiros, sigma_tiros = statistics(numero_de_tiros)
        media_de_tiros.append(media_tiros)
    
    counter = dict(collections.Counter(media_de_tiros))
    x = list(counter.keys())
    y = list(counter.values())
    graficar(x, y)
    





   
   # print(f'la media de los tiros es de {media_tiros}, y la desviacion estandar es de {sigma_tiros}')


if __name__ == "__main__":

    numero_de_tiros = int(input('cuantas veces quieres tirar los dados?: '))
    numero_de_intentos = int(input('cuantas veces quieres correr la simulacion?: '))
    main(numero_de_tiros, numero_de_intentos)

  



