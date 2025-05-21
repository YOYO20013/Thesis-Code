#Potenza in funzione della portata d'acqua
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Definisci il percorso del file Excel
file_path = "C:/Users/MEDIA/Dropbox/Il mio PC (DESKTOP-5MOS4OL)/Desktop/TESI MAGISTRALE/Code_portate_5.xlsx"

# Carica il file Excel (header=0 indica che la prima riga contiene i nomi delle variabili)
df = pd.read_excel(file_path, header=0)

# Colori distinti per ogni fitting lineare (usati codici esadecimali)
colors = ['#1f77b4', '#2ca02c', '#d62728',  '#9467bd']

# Funzione per eseguire il fitting e la visualizzazione con colore specifico
def fit_and_plot(x, y, label, color):
    coefficients = np.polyfit(x, y, 1)  # Fitting lineare
    y_fit = np.polyval(coefficients, x)  # Valori del fitting
    plt.plot(x, y_fit, label=label, color=color, linewidth=2)  # Disegna la retta di fitting con colore

plt.figure(figsize=(18, 12))  

# Prendi i primi 5 valori
x1 = df['Q_H2O [l/min]'].iloc[0:5].values
y1 = df['Power [W]'].iloc[0:5].values
fit_and_plot(x1, y1, r'$\Delta T_{w-air} = 40 \, \text{K}$', colors[0])

# Prendi i successivi 3 valori
x2 = df['Q_H2O [l/min]'].iloc[5:8].values
y2 = df['Power [W]'].iloc[5:8].values
fit_and_plot(x2, y2, r'$\Delta T_{w-air} = 30 \, \text{K}$', colors[1])

# Prendi i successivi 5 valori
x3 = df['Q_H2O [l/min]'].iloc[8:13].values
y3 = df['Power [W]'].iloc[8:13].values
fit_and_plot(x3, y3, r'$\Delta T_{w-air} = 20 \, \text{K}$', colors[3])

# Prendi gli ultimi 3 valori
x4 = df['Q_H2O [l/min]'].iloc[13:16].values
y4 = df['Power [W]'].iloc[13:16].values
fit_and_plot(x4, y4, r'$\Delta T_{w-air} = 10 \, \text{K}$', colors[2])

# Imposta le etichette e il titolo
plt.xlabel(r'$Q_{H2O} \, [\frac{l}{min}]$', fontsize=30)
plt.ylabel(r'$\dot{Q}$ [W]',fontsize=30)
plt.title(r'Potenza scambiata con $v_{air}$ data dai fan', fontsize=26)
plt.legend(fontsize=26)
plt.grid()
plt.tick_params(axis='both', which='major', labelsize=26)
plt.xlim(0, 20)
plt.ylim(0, 3500)

# Mostra il grafico
plt.show()
#Perdite di carico lato acqua 
import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import Polynomial

# Dati delle perdite di carico (Dp H2O in mbar)
dp_h2o = [164.0, 116.1, 75.2, 43.4, 19.9, 169.5, 77.6, 20.4, 173.4, 122.4, 79.7, 46.2, 20.9, 177.5, 82.0, 21.2]

# Dati della portata d'acqua (Q H2O in l/min)
q_h2o = [15.00, 12.50, 10.00, 7.50, 5.00, 15.00, 10.00, 5.00, 15.00, 12.50, 10.00, 7.50, 5.00, 15.00, 10.00, 5.00]

# Creazione del grafico scatter
plt.figure(figsize=(18, 10))
plt.scatter(q_h2o, dp_h2o, color='b', label='Dati sperimentali')

# Interpolazione polinomiale (grado 2 per un modello quadratico)
coeffs = np.polyfit(q_h2o, dp_h2o, 2)
polynomial = np.poly1d(coeffs)

# Generazione dei punti per la linea interpolante
q_h2o_fit = np.linspace(min(q_h2o), max(q_h2o), 100)
dp_h2o_fit = polynomial(q_h2o_fit)

# Plot della linea interpolante
plt.plot(q_h2o_fit, dp_h2o_fit, color='k', label='Linea interpolante')

# Etichette e titolo
plt.title('Perdite di carico lato acqua in funzione della portata d\'acqua', fontsize=26)
plt.xlabel(r'$Q_{H2O} [l/min]$', fontsize=30)
plt.ylabel(r'$ Dp_{H2O} [mbar] $', fontsize=30)

# Mostra la legenda e il grafico
plt.legend(fontsize=26)
plt.tick_params(axis='both', which='major', labelsize=26)
plt.grid(True)
plt.tight_layout()
plt.show()