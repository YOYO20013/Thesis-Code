from scipy.optimize import curve_fit

filepath1="C:\\Users\\MEDIA\\Dropbox\\Il mio PC (DESKTOP-5MOS4OL)\\Desktop\\TESI MAGISTRALE\\Perdite di carico aria.txt"
filepath2="C:\\Users\\MEDIA\\Dropbox\\Il mio PC (DESKTOP-5MOS4OL)\\Desktop\\TESI MAGISTRALE\\Velocita aria.txt"

data1=np.loadtxt(filepath1)
data2=np.loadtxt(filepath2)
L = 26 * 10**(-3)
v_air = data2
Pressure_loss = data1/L  # Perdite di carico
#definizione della funzione per il fitting

def dp(v_air,alpha,beta):
    return alpha*v_air+beta*v_air**2

params, covariance = curve_fit(dp, v_air, Pressure_loss)

# Estrazione dei parametri
alpha = params[0]
beta = params[1]

plt.figure(figsize=(18,12))
plt.plot(v_air, Pressure_loss, 'bo', label='Dati sperimentali') 
plt.plot(v_air, dp(v_air,alpha,beta)  , 'r-', label=f'Curva interpolante, con alpha = {alpha:.2f};  beta = {beta:.2f}') 
plt.xlabel('$v_{air}$ [m/s]', fontsize=30)
plt.ylabel(r'$\frac{\Delta p_0}{L}$ [Pa/m]', fontsize=30)
plt.tick_params(axis='both', which='major', labelsize=30)


plt.title('Curva interpolante per la determinazione dei coefficienti di porosita',fontsize=30)
plt.legend(fontsize=24)
plt.grid()
plt.show()