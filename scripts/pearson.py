import numpy as np
import matplotlib.pyplot as plt

#from scripts.gaussian_confusion import colors

# Zufallsdaten mit definierter Korrelation
np.random.seed(42)
x = np.linspace(0, 10, 100)
noise = np.random.normal(0, 1, size=100)
y1 = 2 * x + 5 + noise
y2 = -1.5 * x - 0.6 * noise + 35  # vertikal verschoben zur besseren Sichtbarkeit

# Mittelwerte und Standardabweichungen
mean_y1 = np.mean(y1)
std_y1 = np.std(y1)
mean_y2 = np.mean(y2)
std_y2 = np.std(y2)

# Plot
plt.figure(figsize=(12, 6))

# Standardabweichungsbereiche (hellgraue Balken)
plt.fill_between(x, mean_y1 - std_y1, mean_y1 + std_y1, color='lightgray', alpha=0.5, label='Std. Kurve 1')
plt.fill_between(x, mean_y2 - std_y2, mean_y2 + std_y2, color='lightgray', alpha=0.5, label='Std. Kurve 2')

# Mittelwertlinien
plt.axhline(mean_y1, color='blue', linestyle='--', linewidth=1.5, label='Mittelwert Kurve 1')
plt.axhline(mean_y2, color='red', linestyle='--', linewidth=1.5, label='Mittelwert Kurve 2')

# Kurven
plt.plot(x, y1, color='blue', label='Kurve 1')
plt.plot(x, y2, color='red', label='Kurve 2')

# Achsenformatierung: Nur x- und y-Achse sichtbar
ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')

plt.tick_params(left=False, bottom=False)
plt.xticks([])
plt.yticks([])

ix = 20
px = x[ix]
py1 = 2 * px + 5 + noise[ix]
py2 = -1.5 * px - 0.6 * noise[ix] + 35
line, = plt.plot( [px,px],[mean_y1,py1], label=r'$y_i - \bar{y}$' , color="blue")
plt.text(px + 0.1, 0.5 *(py1 + mean_y1), line.get_label(), color=line.get_color(),
         fontsize=12, va='center', ha='left')

line, = plt.plot( [px,px],[mean_y2,py2], label=r'$x_i - \bar{x}$' , color="red")
plt.text(px + 0.1, 0.5 *(py2 + mean_y2), line.get_label(), color=line.get_color(),
         fontsize=12, va='center', ha='left')


ix = 10
px = x[ix]
py1 = 2 * px + 5 + noise[ix]
py2 = -1.5 * px - 0.6 * noise[ix] + 35
line, = plt.plot( [px,px],[mean_y1,mean_y1+std_y1], label=r'$\sigma_y$' , color="blue")
plt.text(px + 0.1, mean_y1+std_y1-2.5, line.get_label(), color=line.get_color(),
         fontsize=12, va='center', ha='left')

line, = plt.plot( [px,px],[mean_y2,mean_y2 + std_y2], label=r'$\sigma_x$' , color="red")
plt.text(px + 0.1, 0.5 *(py2 + mean_y2), line.get_label(), color=line.get_color(),
         fontsize=12, va='center', ha='left')




# Legende
#plt.legend(loc='upper left')
corr_coef = np.corrcoef(y1, y2)[0, 1]
plt.title(f"Illustration Pearson-Korrelation (r = {corr_coef:.2f})")
#plt.title("Pearson-Korrelation: r = -0.96")
plt.tight_layout()
plt.savefig("pearson2.png")
plt.show()
