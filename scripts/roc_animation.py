import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from sklearn.metrics import roc_curve

# Daten vorbereiten
np.random.seed(0)
class0 = np.random.normal(0, 1, 1000)
class1 = np.random.normal(2, 1, 1000)
data = np.concatenate([class0, class1])
labels = np.concatenate([np.zeros(1000), np.ones(1000)])

# ROC vorbereiten
fpr, tpr, thresholds = roc_curve(labels, data)

# Farben
threshold_colors = plt.cm.viridis(np.linspace(0, 1, len(thresholds)))

# Plot vorbereiten
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

x = np.linspace(-4, 6, 500)
y0 = 1/np.sqrt(2 * np.pi) * np.exp(-0.5 * (x - 0)**2)
y1 = 1/np.sqrt(2 * np.pi) * np.exp(-0.5 * (x - 2)**2)

line0, = ax1.plot(x, y0, label='Class 0', alpha=0.7)
line1, = ax1.plot(x, y1, label='Class 1', alpha=0.7)
grenzlinie = ax1.axvline(x=0, color='red', linestyle='--')
ax1.set_title("Gaußverteilungen mit Grenzwert")
ax1.legend()

roc_line, = ax2.plot(fpr, tpr, label='ROC Curve')
punkt, = ax2.plot([], [], 'o', color='red')
ax2.set_title("ROC-Kurve")
ax2.set_xlabel("False Positive Rate")
ax2.set_ylabel("True Positive Rate")
ax2.legend()

# Animation

def update(i):
    threshold = thresholds[i]
    grenzlinie.set_xdata(threshold)

    fpr_i, tpr_i = fpr[i], tpr[i]
    punkt.set_data([fpr_i], [tpr_i])
    punkt.set_color(threshold_colors[i])
    grenzlinie.set_color(threshold_colors[i])
    return grenzlinie, punkt

ani = FuncAnimation(fig, update, frames=len(thresholds), interval=20, blit=True)
plt.tight_layout()
plt.show()

#from matplotlib.animation import PillowWriter
#ani.save("roc_animation.gif", writer=PillowWriter(fps=10))
from matplotlib.animation import FFMpegWriter
ani.save("animation.mp4", writer=FFMpegWriter(fps=10))