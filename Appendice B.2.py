v0 = df0.iloc[:, 3]
v1 = df1.iloc[:, 3]
v2 = df2.iloc[:, 3]
v3 = df3.iloc[:, 3]
v4 = df4.iloc[:, 3]

# Dati di portata
QH2O0 = df0.iloc[:, 0]
QH2O1 = df1.iloc[:, 0]
QH2O2 = df2.iloc[:, 0]
QH2O3 = df3.iloc[:, 0] 
QH2O4 = df4.iloc[:, 0]

# Dati Delta_t aria-acqua

DT0 = df0.iloc[:,8]
DT1 = df1.iloc[:,8]
DT2 = df2.iloc[:,8]
DT3 = df3.iloc[:,8]
DT4 = df4.iloc[:,8]

# Dati potenza termica scambiata 

Q0 = df0.iloc[:, 9]
Q1 = df1.iloc[:, 9]
Q2 = df2.iloc[:, 9]
Q3 = df3.iloc[:, 9]
Q4 = df4.iloc[:, 9]

import pandas as pd
import numpy as np
from scipy.interpolate import LinearNDInterpolator

# Dati in un singolo DataFrame combinati
data = {
    'velocity': np.concatenate([v0, v1, v2, v3, v4]),
    'flow_rate': np.concatenate([QH2O0, QH2O1, QH2O2, QH2O3, QH2O4]),
    'delta_t': np.concatenate([DT0, DT1, DT2, DT3, DT4]),
    'power': np.concatenate([Q0, Q1, Q2, Q3, Q4])
}

df = pd.DataFrame(data)


# Funzione per interpolazione dei dati sperimentali

interpolator = LinearNDInterpolator(
    points=df[['velocity', 'flow_rate', 'delta_t']].values,
    values=df['power'].values
)

# Funzione per stimare la potenza sulla base dei dati sperimentali

def estimate_power(velocity, flow_rate, delta_t):
    return interpolator(velocity, flow_rate, delta_t)


# Valori in input 
velocity_input = float(input('Velocita aria in [m/s]:'))  
flow_rate_input = float(input('Portata acqua in [l/min]:'))   
delta_t_input =   float(input('Delta T aria-acqua in [K]:')) 

# Interpolazione dei dati per stimare la potenza termica scambiata

power_output = estimate_power(velocity_input, flow_rate_input, delta_t_input)

print(f"Estimated Power : {power_output:.2f}  W")