import pandas as pd
import math, pdb, statistics
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

ages = [19, 19, 19, 19, 19, 19, 20, 20, 20, 20, 20, 20, 20, 21, 22, 22, 22, 24, 27, 28, 29]
heights = [1.54, 1.67, 1.68, 1.70, 1.72, 1.73, 1.74, 1.75, 1.75, 1.76, 1.77, 1.78, 1.78, 1.78, 1.78, 1.80, 1.80, 1.80, 1.80, 1.85, 1.90]
commute = [5, 15, 19, 20, 25, 25, 30, 30, 30, 35, 40, 40, 40, 40, 40, 50, 60, 60, 60, 60, 70, 120, 180]

def plot_histogram(data, graph_name, xlabel, ylabel):
    rango = max(data) - min(data)
    classes = round(math.sqrt(len(data)))
    IdeC = rango/classes
    bins = []
    bins.append(min(data))
    for i in range(1,classes):
        separacion = bins[-1] + IdeC
        bins.append(separacion)

    #pdb.set_trace()

    plt.hist(data, bins=bins, edgecolor='white')

    plt.title(graph_name)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    plt.tight_layout()

    plt.show()

def plot_box_diagram(data, graph_name,label):
    df = pd.DataFrame(data)
    #df.plot(kind='box')
    plt.boxplot(x=df[0], vert=False)
    print(f"Numero de elementos(n) : {len(data)}")
    print(f"Q1: {data[int((1/4)*(len(data) + 1)) - 1]}")
    print(f"Q2: {statistics.median(data)}")
    print(f"Q3: {data[int((3/4)*(len(data) + 1)) - 1]}")
    print(f"IRQ: {data[int((3/4)*(len(data) + 1)) - int((1/4)*(len(data) + 1)) - 1]}")
    plt.title(graph_name)
    plt.xlabel(label)
    plt.show()

if __name__ == "__main__":
    #plot_histogram(ages, "Edades de estudiantes del salon", "Edades", "Numero de Estudiantes")
    #plot_histogram(heights, "Estaturas de estudiantes del salon", "Metros", "Numero de Estudiantes")
    #plot_histogram(commute, "Tiempos de traslado de estudiantes del salon", "Minutos", "Numero de Estudiantes")
    plot_box_diagram(ages, "Edades de estudiantes del salon", "Edades")
    plot_box_diagram(heights, "Estaturas de estudiantes del salon", "Metros" )
    plot_box_diagram(commute, "Tiempos de traslado de estudiantes del salon", "Minutos" )
