import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.metrics import confusion_matrix

# ==== Farbdefinitionen ====
COLOR_TP = '#2E7D32'  # Kräftiges Grün
COLOR_FP = '#C62828'  # Kräftiges Rot
COLOR_FN = '#EF6C00'  # Kräftiges Orange
COLOR_TN = '#1565C0'  # Kräftiges Blau

# ==== Simulierte Daten ====
np.random.seed(0)
class0 = np.random.normal(0, 1, 1000)
class1 = np.random.normal(2, 1, 1000)
data = np.concatenate([class0, class1])
labels = np.concatenate([np.zeros_like(class0), np.ones_like(class1)])

# ==== Schwellenwert definieren ====
threshold = 1.0
preds = data >= threshold
cm = confusion_matrix(labels, preds)
TN, FP, FN, TP = cm.ravel()

# ==== Plot vorbereiten ====
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5), gridspec_kw={'width_ratios': [2, 1]})

# ==== Gaußverteilungen und Flächen ====
x = np.linspace(-4, 6, 1000)
y0 = (1 / np.sqrt(2 * np.pi)) * np.exp(-0.5 * (x - 0)**2)
y1 = (1 / np.sqrt(2 * np.pi)) * np.exp(-0.5 * (x - 2)**2)

ax1.plot(x, y0, label='Class 0', color='blue')
ax1.plot(x, y1, label='Class 1', color='orange')
ax1.axvline(x=threshold, color='black', linestyle='--', label='Grenzwert')

ax1.fill_between(x, 0, y0, where=(x < threshold), color=COLOR_TN, alpha=0.8, label='TN')
ax1.fill_between(x, 0, y0, where=(x >= threshold), color=COLOR_FP, alpha=0.8, label='FP')
ax1.fill_between(x, 0, y1, where=(x < threshold), color=COLOR_FN, alpha=0.8, label='FN')
ax1.fill_between(x, 0, y1, where=(x >= threshold), color=COLOR_TP, alpha=0.8, label='TP')

ax1.set_title("Gaußverteilungen mit Schwellenwert")
ax1.legend(loc='upper right')

# ==== Konfusionsmatrix ====
matrix = np.array([[TN, FP], [FN, TP]])
labels_text = np.array([["TN", "FP"], ["FN", "TP"]])
colors = np.array([[COLOR_TN, COLOR_FP], [COLOR_FN, COLOR_TP]])

for i in range(2):
    for j in range(2):
        ax2.add_patch(plt.Rectangle((j, i), 1, 1, color=colors[i, j]))
        ax2.text(j + 0.5, i + 0.5, labels_text[i][j],
                 ha='center', va='center', fontsize=14, color='white', weight='bold')

ax2.set_xlim(0, 2)
ax2.set_ylim(0, 2)
ax2.set_xticks([0.5, 1.5])
ax2.set_xticklabels(['Negativ', 'Positiv'])
ax2.set_yticks([0.5, 1.5])
ax2.set_yticklabels(['Tatsächlich Negativ', 'Tatsächlich Positiv'])
ax2.set_title("Konfusionsmatrix")
ax2.set_aspect('equal')
ax2.invert_yaxis()
ax2.tick_params(left=False, bottom=False, labelleft=True, labelbottom=True)

plt.tight_layout()
plt.savefig( "gaussian_confusion.png")
plt.show()
