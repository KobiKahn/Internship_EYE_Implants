import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math
import statistics as stats
plt.style.use('Solarize_Light2')
# BioCeramic			Coralline			MedPor

# FUNCTONS
def graph_scatter(xdata, ydata, name):
    plt.figure(figsize=(10, 8))
    plt.plot(xdata, ydata)
    plt.title(name)
    plt.show()


def graph_all(set1, set2, set3):
    fig, ax = plt.subplots(nrows=1, ncols=3)
    ax[0].plot(set1[0], set1[1])
    ax[0].title.set_text(set1[2])

    ax[1].plot(set2[0], set2[1])
    ax[1].title.set_text(set2[2])

    ax[2].plot(set3[0], set3[1])
    ax[2].title.set_text(set3[2])
    plt.show()




#"BioCeramic",,,"Coralline",,,"MedPor",,
data_df = pd.read_csv('22mm Eye implant compression data 031523-1.csv', delim_whitespace=False)
data_df = data_df[0:69772]

# MAKE LISTS
Bio_time = data_df['Time_B']
Bio_force = data_df['Force_B']
Bio_stroke = data_df['Stroke_B']

Cor_time = data_df['Time_C']
Cor_force = data_df['Force_C']
Cor_stroke = data_df['Stroke_C']

Med_time = data_df['Time_M']
Med_force = data_df['Force_M']
Med_stroke = data_df['Stroke_M']

graph_scatter(Bio_stroke, Bio_force, 'BIOCERAMIC STROKE VS FORCE')
graph_scatter(Cor_stroke, Cor_force, 'CORRALINE STROKE VS FORCE')
graph_scatter(Med_stroke, Med_force, 'MEDPOR STROKE VS FORCE')

set1 = [Bio_stroke, Bio_force, 'BIOCERAMIC STROKE VS FORCE']
set2 = [Cor_stroke, Cor_force, 'CORRALINE STROKE VS FORCE']
set3 = [Med_stroke, Med_force, 'MEDPOR STROKE VS FORCE']

graph_all(set1, set2, set3)

# print(Bio_time)






