import numpy as np
import matplotlib.pyplot as plt

# Parameter
x = 10.0
s = 2.0
n = 100
m1 = 20
m2 = 400

# Mittelwerte erzeugen
means_50 = [np.mean(np.random.normal(loc=x, scale=s, size=m1)) for _ in range(n)]
means_100 = [np.mean(np.random.normal(loc=x, scale=s, size=m2)) for _ in range(n)]

# Gemeinsame Bins bestimmen
all_means = means_50 + means_100
bins = np.linspace(min(all_means), max(all_means), 20)

# Histogrammdaten berechnen
counts_50, _ = np.histogram(means_50, bins=bins)
counts_100, _ = np.histogram(means_100, bins=bins)

# Plot vorbereiten
plt.figure(figsize=(10, 5))

# Treppenfunktionen
plt.step(bins[:-1], counts_100, where='post', color='orange', label='Stichprobengröße = ' + str(m2), linewidth=2, zorder=1)
plt.step(bins[:-1], counts_50, where='post', color='blue', label='Stichprobengröße = ' +str(m1), linewidth=2, zorder=2)

# Achsen und Layout
plt.title("Vergleich der Mittelwertverteilungen bei unterschiedlichen Stichprobengrößen")
plt.xlabel("Mittelwert")
plt.ylabel("Häufigkeit")
plt.legend()
plt.grid(axis='y', linestyle=':')
plt.tight_layout()
plt.savefig("means.png")
plt.show()



exit(1)

import numpy as np
import matplotlib.pyplot as plt

# Parameter
x = 10.0
s = 2.0
n = 100
m1 = 10
m2 = 100

# Mittelwerte erzeugen
means_50 = [np.mean(np.random.normal(loc=x, scale=s, size=m1)) for _ in range(n)]
means_100 = [np.mean(np.random.normal(loc=x, scale=s, size=m2)) for _ in range(n)]

# Gemeinsame Bins bestimmen
all_means = means_50 + means_100
bins = np.linspace(min(all_means), max(all_means), 20)

# Histogrammdaten berechnen
counts_50, _ = np.histogram(means_50, bins=bins)
counts_100, _ = np.histogram(means_100, bins=bins)

# Mittelpunkte der Bins berechnen
bin_centers = 0.5 * (bins[:-1] + bins[1:])

# Plot
plt.figure(figsize=(10, 5))

# Histogramm m = 100 (gefüllt hinten)
plt.bar(bin_centers, counts_100, width=np.diff(bins), align='center',
        color='orange', edgecolor='orange', label='Stichprobengröße = ' + str(m2), zorder=1)

# Histogramm m = 50 (gefüllt vorn)
plt.bar(bin_centers, counts_50, width=np.diff(bins), align='center',
        color='blue', edgecolor='blue', label='Stichprobengröße = ' + str(m1), zorder=2)

# Wenn m=100 an einer Stelle kleiner ist, zeichne Linie entlang
for i, (c50, c100, xval) in enumerate(zip(counts_50, counts_100, bin_centers)):
    if c100 < c50:
        plt.plot([xval - 0.5 * (bins[1]-bins[0]), xval + 0.5 * (bins[1]-bins[0])],
                 [c100, c100], color='orange', linewidth=2.5, zorder=3)

# Achsen und Layout
plt.title("Vergleich der Mittelwertverteilungen bei unterschiedlichen Stichprobengrößen")
plt.xlabel("Mittelwert")
plt.ylabel("Häufigkeit")
plt.legend()
plt.grid(axis='y', linestyle=':')
plt.tight_layout()
plt.show()

exit(1)

import numpy as np
import matplotlib.pyplot as plt

# Parameter
x = 10.0
s = 2.0
n = 100
m1 = 20
m2 = 100

# Mittelwerte erzeugen
means_50 = [np.mean(np.random.normal(loc=x, scale=s, size=m1)) for _ in range(n)]
means_100 = [np.mean(np.random.normal(loc=x, scale=s, size=m2)) for _ in range(n)]

# Gemeinsame Bins bestimmen
all_means = means_50 + means_100
bins = np.linspace(min(all_means), max(all_means), 20)

# Histogramme plotten
plt.figure(figsize=(10, 5))
plt.hist(means_50, bins=bins, alpha=0.6, color='blue', label='m = ' + str(m1))
plt.hist(means_100, bins=bins, alpha=0.6, color='orange', label='m = ' + str(m2))

plt.title("Vergleich der Mittelwertverteilungen bei unterschiedlichen Stichprobengrößen")
plt.xlabel("Mittelwert")
plt.ylabel("Häufigkeit")
plt.legend()
plt.grid(axis='y', linestyle=':')
plt.tight_layout()
plt.savefig("means.png")
plt.show()
