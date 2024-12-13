import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Create a figure and axis
fig, ax = plt.subplots(figsize=(6, 6))  # Square figure

# Add dividing lines (horizontal and vertical)
ax.axhline(0.5, color='black', linewidth=2)  # Horizontal line in the middle
ax.axvline(0.5, color='black', linewidth=2)  # Vertical line in the middle
red = (0.5, 0, 0, 0.8)         # True Positives
light_red = (0.5, 0, 0, 0.3)   # False Negatives
green = (0, 0.39, 0, 0.8)      # True Negatives
light_green = (0, 0.39, 0, 0.3) # False Positives

# Add the labels for each quadrant
ax.text(0.25, 0.75, 'TP', ha='center', va='center', fontsize=96, fontweight='bold', color=red)
ax.text(0.75, 0.75, 'FN', ha='center', va='center', fontsize=96, fontweight='bold', color=light_red)
ax.text(0.25, 0.25, 'FP', ha='center', va='center', fontsize=96, fontweight='bold', color=light_green)
ax.text(0.75, 0.25, 'TN', ha='center', va='center', fontsize=96, fontweight='bold', color=green)

# Remove axis labels, ticks, and frame
ax.set_xticks([])
ax.set_yticks([])
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal', 'box')  # Ensure equal aspect ratio
ax.axis('off')  # Turn off axis

# Save the figure as an image
plt.savefig('confusion_matrix.png', bbox_inches='tight', dpi=300)

# Show the plot
plt.savefig('logo.png')
plt.show()
