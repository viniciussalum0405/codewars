 
def past(h, m, s):
    minutos = h * 60
    minutos = minutos + m
    resultado = minutos * 60000
    resultado = resultado + s * 1000
    return resultado
​