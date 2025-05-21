import pandas as pd
import matplotlib.pyplot as plt
import numpy as np  # Import numpy

# File paths
file_paths = [
    "C:\\Users\\MEDIA\\Dropbox\\Il mio PC (DESKTOP-5MOS4OL)\\Desktop\\TESI MAGISTRALE\\risultati-03-02-2025.xlsx",
    "C:\\Users\\MEDIA\\Dropbox\\Il mio PC (DESKTOP-5MOS4OL)\\Desktop\\TESI MAGISTRALE\\risultati-04-02-2025.xlsx",
    "C:\\Users\\MEDIA\\Dropbox\\Il mio PC (DESKTOP-5MOS4OL)\\Desktop\\TESI MAGISTRALE\\risultati-05-02-2025.xlsx",
    "C:\\Users\\MEDIA\\Dropbox\\Il mio PC (DESKTOP-5MOS4OL)\\Desktop\\TESI MAGISTRALE\\risultati-07-02-2025.xlsx",
    "C:\\Users\\MEDIA\\Dropbox\\Il mio PC (DESKTOP-5MOS4OL)\\Desktop\\TESI MAGISTRALE\\risultati-10-02-2025.xlsx",
    "C:\\Users\\MEDIA\\Dropbox\\Il mio PC (DESKTOP-5MOS4OL)\\Desktop\\TESI MAGISTRALE\\risultati-DT40.xlsx"
]

# Import Excel files into DataFrames
dfs = [pd.read_excel(file_path, skiprows=0) for file_path in file_paths]

#Selezione del file con cui lavorare 
df0 = dfs [0]
df1 = dfs [1]
df2 = dfs [2]
df3 = dfs[3]  
df4 = dfs[4]
df5 = dfs [5]

# Selezione dei valori di portata e potenza 
Q0 = df0.iloc[:, 9]
QH2O0 = df0.iloc[:, 0] 
Q1 = df1.iloc[:, 9]  
QH2O1 = df1.iloc[:, 0]  
Q2=df2.iloc[:,9]
QH2O2 = df2.iloc[:, 0]
Q3 = df3.iloc[:, 9]  
QH2O3 = df3.iloc[:, 0]  
Q4=df4.iloc[:,9]
QH2O4 = df4.iloc[:, 0]
Q5=df5.iloc[:,9]
QH2O5 = df5.iloc[:, 0]
# Plot dati Potenza in funzione della portata d'acqua

plt.figure(figsize=(18,10))
plt.scatter(QH2O0, Q0, label='DT40', color='blue')
plt.scatter(QH2O1, Q1, color='blue')
plt.scatter(QH2O2, Q2, label='DT30', color='green')
plt.scatter(QH2O4, Q4, label='DT20', color='purple')
plt.scatter(QH2O3, Q3, label='DT10', color='red')
plt.xlabel("$Q_{H2O}$ [l/min]",fontsize=30)
plt.ylabel(r'$\dot{Q}$ [W]',fontsize=30)
plt.ylim(0,3600)
plt.xlim(0,20)
plt.title("Potenza termica della batteria in funzione della portata d'acqua",fontsize=30)
plt.tick_params(axis='both', which='major', labelsize=26)
plt.legend(fontsize=26)
plt.show()


# Plot della potenza scambiata in funzione della velocità dell'aria
v0 = df0.iloc[:, 3]
v1 = df1.iloc[:, 3]
v2 = df2.iloc[:, 3]
v3 = df3.iloc[:, 3]
v4 = df4.iloc[:, 3]
v5 = df5.iloc[:, 3]

# Visualizzazione grafica
plt.figure(figsize=(18, 10))

# Fitting e interpolazione per DT40

for i in range(0, 20, 4):
    v_curr40 = v5[i:i+4]# Estrai 4 valori di velocità 
    power_curr40 = Q5[i:i+4]# Estrai 4 valori di potenza
    pol40 = np.polyfit(v_curr40, power_curr40, 1)  # Fitting lineare
    print('coefficienti' ,pol40)
    vel40 = np.linspace(min(v_curr40), max(v_curr40), num=100)  # Genera valori di velocità
    Q_interp40 = np.polyval(pol40, vel40)  # Calcola l'interpolazione

    # Plotta la curva di interpolazione
    if i==0:
        plt.plot(vel40, Q_interp40, label=r'$\Delta T_{w-air} = 40$', color='blue')
    else:
        plt.plot(vel40, Q_interp40, color='blue')


# Fitting e interpolazione per DT30
for i in range(0, 12, 4):
    v_curr30 = v2[i:i+4]  # Estrai 4 valori di velocità
    power_curr30 = Q2[i:i+4]  # Estrai 4 valori di potenza
    pol30 = np.polyfit(v_curr30, power_curr30, 1)  # Fitting lineare
    vel30 = np.linspace(min(v_curr30), max(v_curr30), num=100)  # Genera valori di velocità
    Q_interp30 = np.polyval(pol30, vel30)  # Calcola l'interpolazione

    # Plotta la curva di interpolazione
    if i==0:
        plt.plot(vel30, Q_interp30, label=r'$\Delta T_{w-air} = 30$', color='green')
    else:
        plt.plot(vel30, Q_interp30, color='green')


# Fitting e interpolazione per DT20

for i in range(0, 20, 4):
    v_curr20 = v4[i:i+4]# Estrai 4 valori di velocità 
    power_curr20 = Q4[i:i+4]# Estrai 4 valori di potenza
    pol20 = np.polyfit(v_curr20, power_curr20, 1)  # Fitting lineare
    vel20 = np.linspace(min(v_curr20), max(v_curr20), num=100)  # Genera valori di velocità
    Q_interp20 = np.polyval(pol20, vel20)  # Calcola l'interpolazione

    # Plotta la curva di interpolazione
    if i==0:
        plt.plot(vel20, Q_interp20, label=r'$\Delta T_{w-air} = 20$', color='purple')
    else:
        plt.plot(vel20, Q_interp20, color='purple')

# Fitting e interpolazione per DT10
for i in range(0, 12, 4):
    v_curr10 = v3[i:i+4]  # Estrai 4 valori di velocità
    power_curr10 = Q3[i:i+4]  # Estrai 4 valori di potenza
    pol10 = np.polyfit(v_curr10, power_curr10, 1)  # Fitting lineare
    vel10 = np.linspace(min(v_curr10), max(v_curr10), num=100)  # Genera valori di velocità
    Q_interp10 = np.polyval(pol10, vel10)  # Calcola l'interpolazione

    # Plotta la curva di interpolazione
    if i==0:
        plt.plot(vel10, Q_interp10, label=r'$\Delta T_{w-air} = 10$', color='red')
    else:
        plt.plot(vel10, Q_interp10, color='red')
plt.legend(fontsize=26)
plt.xlabel(r'$v_{air,in} [\frac{m}{s}]$',fontsize=30)
plt.ylabel(r'$\dot{Q}$ [W]',fontsize=30)
plt.title('Potenza termica in funzione della velocità dell\'aria in ingresso alla batteria',fontsize=30)
plt.tick_params(axis='both', which='major', labelsize=26)
plt.show()

#perdite di carico aria
Dp0 = df0.iloc[:, 6]
Dp1 = df1.iloc[:, 6]
Dp2 = df2.iloc[:, 6]
Dp3 = df3.iloc[:, 6]
Dp5 = df5.iloc[:,6]
plt.figure(figsize=(18,10))
# Curva perdite di carico lato aria

v_curr = v2  # Estrai 4 valori di velocità
Dp0_air = Dp2  # Estrai 4 valori di potenza
pol_dp0 = np.polyfit(v_curr, Dp0_air, 2)  # Fitting quadratico
velocity = np.linspace(min(v_curr), max(v_curr), num=100)  # Genera valori di velocità
Dp0_interp = np.polyval(pol_dp0, velocity)  # Calcola l'interpolazione
# Plotta la curva di interpolazione
print("Coefficienti del polinomio (a, b, c):", pol_dp0)
plt.plot(velocity, Dp0_interp, color='black',linewidth=2)
plt.scatter(v1 ,Dp1, label=r'$\Delta T_{w-air} = 40$', color='blue')
plt.scatter(v2 ,Dp2, label=r'$\Delta T_{w-air} = 30$', color='green')
plt.scatter(v3 ,Dp3, label=r'$\Delta T_{w-air} = 10$', color='red')
plt.xlim([2,6])
plt.ylim([0,150])
plt.xlabel(r'$v_{air,in} [\frac{m}{s}]$',fontsize=30)
plt.ylabel(r'$Dp_{0} \, [Pa]$', fontsize=30)
plt.title('Perdite di carico lato aria in funzione della velocità dell\'aria in ingresso alla batteria',fontsize=30)
plt.tick_params(axis='both', which='major', labelsize=26)
plt.legend(fontsize=26)
plt.show()




# Estrai le perdite di carico
DpW0 = df0.iloc[:, 7]
DpW1 = df1.iloc[:, 7]
DpW2 = df2.iloc[:, 7]
DpW3 = df3.iloc[:, 7]
DpW4 = df4.iloc[:, 7]

# Plot dei dati
plt.figure(figsize=(18, 10))

Flow = QH2O4  # Estrai 4 valori di portata
DpWater = DpW4  # Estrai 4 valori di perdite di carico
polW = np.polyfit(Flow, DpWater, 2)  # Fitting quadratico

F = np.linspace(min(Flow), max(Flow), num=100)  # Genera valori di portata
DpW_interp = np.polyval(polW, F)  # Calcola l'interpolazione
# Plotta la curva di interpolazione
plt.plot(F, DpW_interp, color='black', linewidth=2)

# Plotta i dataset
plt.scatter(QH2O0, DpW0, color='blue')
plt.scatter(QH2O1, DpW1, label=r'$\Delta T_{w-air} = 40$', color='blue')
plt.scatter(QH2O2, DpW2, label=r'$\Delta T_{w-air} = 30$', color='green')
plt.scatter(QH2O4, DpW4, label=r'$\Delta T_{w-air} = 20$', color='purple')
plt.scatter(QH2O3, DpW3, label=r'$\Delta T_{w-air} = 10$', color='red')

plt.legend(fontsize=26)
plt.xlabel(r'$Q_{H2O} [\frac{l}{min}]$',fontsize=30)
plt.ylabel(r'$D_{p_{H2O}} [Pa]$',fontsize=30)
plt.title('Perdite di carico lato acqua in funzione della portata d\'acqua',fontsize=26)
plt.tick_params(axis='both', which='major', labelsize=30)
plt.show()

#Visualizzazione grafico Q-Delta T
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Definisci il percorso del file Excel
file_path = "C:/Users/MEDIA/Dropbox/Il mio PC (DESKTOP-5MOS4OL)/Desktop/TESI MAGISTRALE/Code_portate.xlsx"

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
plt.title(r'Potenza scambiata con $v_{air,in} = 5 \, \frac{m}{s}$', fontsize=26)
plt.legend(fontsize=26)
plt.grid()
plt.tick_params(axis='both', which='major', labelsize=26)
plt.xlim(0, 20)
plt.ylim(0, 3500)
# Mostra il grafico
plt.show()

#Portata in funzione del Delta T
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Crea il DataFrame con i tuoi dati
data = {
    'DT': [40, 30, 20, 10],
    'Q': [2970.3, 2277.7, 1541.4, 814.5]
}

df = pd.DataFrame(data)

# Colori distinti per il fitting lineare (usati codici esadecimali)
colors = ['#1f77b4']

# Funzione per eseguire il fitting e la visualizzazione con colore specifico
def fit_and_plot(x, y, label, color):
    coefficients = np.polyfit(x, y, 1)  # Fitting lineare
    y_fit = np.polyval(coefficients, x)  # Valori del fitting
    plt.plot(x, y_fit, label=label, color=color, linewidth=2)  # Disegna la retta di fitting con colore

plt.figure(figsize=(18, 12))  

# Estrai i valori da DataFrame
x = df['DT'].values  # Prendi i valori di DT
y = df['Q'].values   # Prendi i valori di potenza (Q)
fit_and_plot(x, y, r'$Q$ vs $ \Delta T$', colors[0])  # Aggiungi la retta di fitting

# Imposta le etichette e il titolo
plt.xlabel(r'$ \Delta T_{w-air} \, [K]$', fontsize=30)
plt.ylabel(r'$\dot{Q}$ [W]', fontsize=30)
plt.title(r'Potenza in funzione di $\Delta T_{w-air}, con v_{air} = 5 \frac {m}{s}; Q_\text{H2O} = 15 \frac{l}{min} $', fontsize=26)
plt.grid()
plt.tick_params(axis='both', which='major', labelsize=26)
plt.xlim(0, 50)  # Aggiungi un limite per l'asse x
plt.ylim(0, 3500)  # Aggiungi un limite per l'asse y

# Mostra il grafico
plt.show()
