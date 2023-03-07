import pandas as pd
import math, pdb
from matplotlib import pyplot as plt

data = [[29, 1.80], [22, 1.75], [22, 1.80], [22, 1.80], [20, 1.77], 
        [28, 1.85], [20, 1.70], [19, 1.68], [20, 1.80], [20, 1.78], 
        [19, 1.80], [20, 1.70], [23, 1.75], [27, 1.90], [19, 1.80]]

ejemplo = [[4,134],[6,145],[8,142],[10,149],[12,144],
           [14,160],[16,156],[18,157],[20,168],[22,166],
           [24,167],[26,171],[28,174],[30,183]]

def dispersion_diagram(data, x_usuario):
    n = len(data)
    xi = 0.0
    yi = 0.0
    xi_2 = 0.0
    yi_2 = 0.0
    xiyi = 0.0
    i = 0
    print(f"i\t\tX\t\tY\t\tX*Y\t\tX^2\t\tY^2")
    for persona in data:
        xi += persona[0]
        yi += persona[1]
        xiyi += persona[0] * persona[1]
        xi_2 += persona[0] ** 2
        yi_2 += persona[1] ** 2
        i += 1
        print(f"{i}\t\t{persona[0]:.2f}\t\t{persona[1]:.2f}\t\t{(persona[0]*persona[1]):.2f}\t\t{(persona[0] ** 2):.2f}\t\t{(persona[1] ** 2):.2f}")
    print(f"\t\t{xi:.2f}\t\t{yi:.2f}\t\t{xiyi:.2f}\t\t{xi_2:.2f}\t\t{yi_2:.2f}")
    rxy = (xiyi - (((xi * yi)/n))) / math.sqrt((xi_2-(xi**2)/n)*(yi_2-(yi**2/n)))
    print(f"\nrxy = {rxy:.4f}")
    Dxy = rxy**2 * 100
    print(f"Dxy = {Dxy:.4f}%")

    beta_1 = (xiyi - (((xi * yi)/n))) / (xi_2-(xi**2)/n)
    y_media = yi/n
    x_media = xi/n
    beta_0 = y_media - beta_1*x_media
    y_regresion = beta_0 + beta_1*x_usuario
    print(f"Beta 1 = {beta_1}")
    print(f"Beta 0 = {beta_0}")
    print(f"y para un x = {x_usuario} : {y_regresion}")

    plt.style.use('fivethirtyeight')
    
if __name__ == "__main__":
    dispersion_diagram(data, 25)