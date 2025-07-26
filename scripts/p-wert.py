import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# === Parameter ===
mu = 0
sigma = 1
x = np.linspace(-4, 4, 1000)
y = norm.pdf(x, mu, sigma)

# === Signifikanzniveau und z-Werte ===
alpha = 0.05
z_critical = norm.ppf(1 - alpha)  # einseitig

# === Plot vorbereiten ===
fig, ax = plt.subplots(figsize=(10, 5))

# Normalverteilung zeichnen
ax.plot(x, y, label='Standardnormalverteilung', color='black')

# Horizontale Linie bei Dichte=0
ax.axhline(0, color='black', linewidth=1)

# Mittelwert markieren
ax.axvline(mu, color='blue', linestyle='--', label='Mittelwert (z=0)')

# Standardabweichungen einzeichnen
for i in range(1, 4):
    ax.axvline(mu + i * sigma, color='gray', linestyle=':', linewidth=1)
    ax.axvline(mu - i * sigma, color='gray', linestyle=':', linewidth=1)
    ax.text(mu + i * sigma, 0.01, f"+{i}σ", ha='center', color='gray')
    ax.text(mu - i * sigma, 0.01, f"-{i}σ", ha='center', color='gray')

# Kritischer Bereich einfärben (einseitig, rechts)
x_crit = np.linspace(z_critical, 4, 500)
y_crit = norm.pdf(x_crit, mu, sigma)
ax.fill_between(x_crit, y_crit, color='red', alpha=0.5, label=f'Signifikanzniveau α = {alpha:.2f}')

# z-Wert und p-Wert markieren (Beispiel)
z_value = 2.1
p_value = 1 - norm.cdf(z_value)
ax.axvline(z_value, color='darkgreen', linestyle='-', linewidth=2)
ax.text(z_value, 0.05, f'z = {z_value:.2f}\np = {p_value:.3f}',
        color='darkgreen', fontsize=12, fontweight='bold', ha='left', va='center')

# Layout
ax.set_title('Standardnormalverteilung (einseitiger Test)')
ax.set_xlabel('z-Wert')
ax.set_ylabel('Dichte')
ax.legend(title="Legende: \u03c3 = Standardabweichung")

plt.tight_layout()
plt.savefig( "p-wert.png")
plt.show()
