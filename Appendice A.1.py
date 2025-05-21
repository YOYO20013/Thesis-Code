#Codice calcolo portate
#Dati diaframma 
D=96 #mm
d=70.1 #mm
beta=d/D #rapporto di contrazione diaframma
#Dati misurati temperatura e pressione ambiente
T_amb=21 #gradi Celsius
p_amb=1026.1 #mbar
#correzione t amb e p amb
P_amb=((p_amb-0.000163*p_amb*T_amb)/1000*100000)
T_AMB=T_amb+273.15 # temperatura ambiente in Kelvin
#Geometria della batteria e del canale di scarico 
#Batteria
L1=236
H1=138
Area1=L1*H1*10**(-6) #area batteria in m^2
#Canale di scarico 
L2=151
H2=277
Area2=L2*H2*10**(-6) #area canale in m2

import pandas as pd
import numpy as np

# Importazione misure corrette da Excel
file_path = "C:\\Users\\MEDIA\\Dropbox\\Il mio PC (DESKTOP-5MOS4OL)\\Desktop\\TESI MAGISTRALE\\misure-04-02-2025.xlsx"
leggi_misura = pd.read_excel(file_path, header=None)

# Converti il DataFrame in un array NumPy
Misure_vett = leggi_misura.to_numpy(dtype=float)
print(Misure_vett)

# Dati di input
mu = 0.000018
Dpdiaf_corr = Misure_vett[:, 6]
Pmdiaf_corr = Misure_vett[:, 5]
T_diaf = Misure_vett[:, 3]
beta = d / D  # Assicurati che beta sia definito correttamente
# Dati di input
Pamb = 1030.2*100
DpH2O_corr = Misure_vett[:, 7]
Dp_air_corr = Misure_vett[:, 4]
TH2Oin = Misure_vett[:, 0]
T_air = Misure_vett[:, 2]
TH2O_out_corr = Misure_vett[:, 1]
Q_H2O = Misure_vett[:, 8]  # Portata d'acqua nella batteria


# Lista per memorizzare le potenze
Powers = []
results=[]
# Costanti
gamma = 1.40  # esponente dell'iso-s
flow_rates = []  # Lista per memorizzare i flow rates

# Itera su ogni riga di Misure_vett
for i in range(Misure_vett.shape[0]):
    # Estrai i valori per la riga corrente
    Pmdiaf = Pmdiaf_corr[i]
    Dpdiaf = Dpdiaf_corr[i]
    T_diaf_current = T_diaf[i]
    DpH2O_curr=DpH2O_corr[i]
    # Calcolo delle variabili necessarie
    Pmd = P_amb - Pmdiaf * 100
    Dpdiaf = Dpdiaf * 100
    Rho_med = (P_amb - Pmdiaf * 100) / (287 * (T_diaf_current + 273.15))
    epsilon = 1 - (0.351 + 0.256 * beta ** 4 + 0.93 * beta ** 8) * (1 - (1 - (Dpdiaf / Pmd)) ** (1 / gamma))

    # Inizializzazione per il calcolo di c
    n = 1
    c = np.full((n,), 0.6)  # n è il numero di valori di c che desideri
    tolleranza = 1e-3  # tolleranza per la variazione di c
    c_old = c + 2 * tolleranza  # inizializza c_old a un valore diverso da c

    while np.any(np.abs(c - c_old) > tolleranza):
        c_old = c.copy()  # Copia i valori correnti di c in c_old
        # Calcolo portate
        alfa = c / (((1 - beta ** 4)) ** 0.5)
        flow_rate = alfa * epsilon * ((np.pi * (0.0701) ** 2) / 4) * (2 * Rho_med * Dpdiaf) ** 0.5
        v = flow_rate / (Rho_med * np.pi * 0.25 * 0.096 ** (2))
        Reynolds = Rho_med * v * 0.096 / mu
        A = ((19000 * beta) / Reynolds) ** 0.8
        L2 = 0.47
        M2 = 2 * L2 / (1 - beta)
        C = 0.5961 + 0.0261 * beta ** (2) - 0.216 * beta ** (8) + 0.000521 * (((10 ** 6) * beta) / Reynolds) ** 0.7 + (0.0188 + 0.0063 * A) * beta ** (3.5) * ((10 ** 6) / Reynolds) ** 0.3 + (0.043 + 0.08 * np.exp(-10) - 0.123 * np.exp(-7)) * (1 - 0.11 * A) * (beta ** (4) / (1 - beta ** (4))) - 0.031 * (M2 - 0.8 * M2 ** 1.1) * beta ** 1.3
        
        # Aggiorna c
        c = C

    # Salva il flow rate per la riga corrente
    flow_rates.append(flow_rate)

# Estrai i valori per la riga corrente - potenza della batteria 
    Dp_air_corr_curr = Dp_air_corr[i]
    TH2Oin_curr = TH2Oin[i]
    TH2O_out_corr_curr = TH2O_out_corr[i]
    T_air_curr = T_air[i]
    T_diaf_current = T_diaf[i]
    flow_rate_curr = flow_rates[i]
    Q_H2O_curr=Q_H2O[i]
    # Calcolo densità dell'aria in ingresso e in uscita
    Rho_air_in = Pamb / (287 * (T_air_curr + 273.15))
    Rho_air_out = (Pamb - Dp_air_corr_curr * 100) / (287 * (T_diaf_current + 273.15))

    # Calcolo velocità dell'aria in ingresso e in uscita
    V_air_in = flow_rate_curr / (Rho_air_in * Area1)
    V_air_out = flow_rate_curr / (Rho_air_out * Area2)

    # Salto di pressione dinamica dell'aria dopo il passaggio nella batteria
    Dp0_air = Dp_air_corr_curr * 100 + 0.5 * Rho_air_out * V_air_out ** 2

    # Differenza di temperatura aria-acqua
    DT_airH2O = TH2Oin_curr - T_air_curr
    # Calcolo della potenza termica scambiata (prestazione batteria)
    DT = abs(TH2O_out_corr_curr - TH2Oin_curr)
    if DT == 0:
        Power = 0  # o un valore predefinito, o un messaggio di errore
        print("ATTENZIONE: TH2O_out_corr_curr e TH2Oin_curr sono uguali!")
    else:
        Power = Q_H2O_curr / 60 * (4186 * DT)
    DTAW=TH2Oin_curr-T_air_curr
# Aggiungi i risultati alla lista
    results.append([Q_H2O_curr, flow_rate_curr, Rho_air_in, V_air_in, Rho_air_out, V_air_out, Dp0_air, DpH2O_curr, DT_airH2O, Power])

# Converti la lista in un DataFrame di pandas
results_df = pd.DataFrame(results, columns=["Q_H2O", "Flow Rate", "Rho Air In", "V Air In", "Rho Air Out", "V Air Out", "Dp0 Air", "Dp H2O Corr", "DT Air-Water", "Power"])

# Salva i risultati in un file Excel
output_file_path = "C:\\Users\\MEDIA\\Dropbox\\Il mio PC (DESKTOP-5MOS4OL)\\Desktop\\TESI MAGISTRALE\\risultati-04-02-2025.xlsx"
results_df.to_excel(output_file_path, index=False, header=True)