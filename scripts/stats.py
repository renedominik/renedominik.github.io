'''
import matplotlib.pyplot as plt
import matplotlib.patches as patches



def draw_simple_person_icon(ax, x, y, size=1, color=(0, 0, 0, 1)):
    """Draws a simple person icon with the upper third of a circle representing the upper body."""
    
    # Head (circle)
    head_radius = size * 0.17
    head_center = (x, y + size * 0.4)
    head = patches.Circle(head_center, head_radius, color=color)
    ax.add_patch(head)

    # Upper body (top third of a circle)
    body_radius = size * 0.25
    body_center = (x, y)
    body = patches.Wedge(center=body_center, r=body_radius, theta1=20, theta2=160, color=color)
    ax.add_patch(body)


def draw_person_icon(ax, x, y, size=1, color=(0, 0, 0, 1)):
    """Draws a simple person icon at the specified (x, y) position with a specified color."""
    
    # Head (circle)
    head_radius = size * 0.17
    head_center = (x, y + size * 0.38)
    head = patches.Circle(head_center, head_radius, color=color)
    ax.add_patch(head)
    
    # Body (rectangle with rounded corners)
    body_width = size * 0.4
    body_height = size * 0.4
    body = patches.FancyBboxPatch((x - body_width / 2, y - body_height / 2), body_width, body_height, 
                                  boxstyle="round,pad=0.02", color=color)
    ax.add_patch(body)
    
    # Legs (two small rectangles)
    leg_width = size * 0.15
    leg_height = size * 0.3
    left_leg = patches.Rectangle((x - body_width / 4, y - body_height / 2 - leg_height), leg_width, leg_height, color=color)
    right_leg = patches.Rectangle((x + body_width / 4 - leg_width, y - body_height / 2 - leg_height), leg_width, leg_height, color=color)
    ax.add_patch(left_leg)
    ax.add_patch(right_leg)
    

def draw_person_icon_matrix(ax, rows=5, cols=5, spacing=(1.5,1.5), size=1, colors=None):
    """Draws a matrix of person icons with specified rows and columns, with optional individual colors for each block."""
    
    if colors is None:
        colors = [[(1,1,1,1) for _ in range(cols)] for _ in range(rows)]
    
    for row in range(rows):
        for col in range(cols):
            x = col * spacing[0]
            y = (rows - row - 1) * spacing[1]
            color = colors[row][col] if row < len(colors) and col < len(colors[row]) else (1, 1, 1, 1)
            draw_person_icon(ax, x, y, size, color)
    
    



def draw_table(ax, rows, cols, spacing=(1.5,1.5)):
    """Draws a table grid around the matrix of icons."""
    for row in range(rows + 1):
        y = row * spacing[1]
        ax.plot([0, cols * spacing[1]], [y, y], color="black", linewidth=1.5)
    for col in range(cols + 1):
        x = col * spacing[0]
        ax.plot([x, x], [0, rows * spacing[0]], color="grey", linewidth=1.5)



    
if __name__ == "__main__":
    
    white = (1,1,1,1)
    red = (0.5, 0, 0, 0.8)
    light_red = (0.5, 0, 0, 0.4)
    green = (0, 0.39, 0, 0.8)
    light_green = (0, 0.39, 0, 0.4)
    
    colors = [
        [ red, red, red, light_green, light_green, light_green, light_green, light_green ],
        [ red, red, red, light_green, light_green, light_green, light_green, light_green ],
        [ red, red, white , light_green, light_green, light_green, light_green ],
        [ light_red, light_red, light_red, green, green, green, green, green ],
        [ light_red, light_red, light_red, green, green, green, green, green ],
        [ light_red, light_red, light_red, green, green, green, green, green ],
        [ light_red, light_red, light_red, green, green, green, green, green ],
        [ light_red, light_red, white, green, green, green ]
    ]

    rows = len(colors)
    cols = max(len(row) for row in colors)

    spacing=(0.6,1.3)
    
    fig, ax = plt.subplots(figsize=(cols * spacing[0], rows * spacing[1]))

    draw_person_icon_matrix(ax, rows=rows, cols=cols, spacing=spacing, size=0.8, colors=colors)
    #ax.plot( [0,0], [0, rows*spacing[0]] )
    #ax.plot( [0,cols*spacing[1]], [0,0] )
    #draw_table(ax, rows, cols, spacing)  # Draw the table grid


    ax.set_aspect('equal', 'box')
    ax.set_xlim(-spacing[0], cols * spacing[0])
    ax.set_ylim(-spacing[1], rows * spacing[1])
    ax.axis('off')  # Hide axis

    plt.show()
'''




import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_person_icon(ax, x, y, size=1, color=(0, 0, 0, 1)):
    """Draws a simple person icon with the upper third of a circle representing the upper body."""
    
    # Head (circle)
    head_radius = size * 0.17
    head_center = (x, y + size * 0.4)
    head = patches.Circle(head_center, head_radius, color=color)
    ax.add_patch(head)

    # Upper body (top third of a circle)
    body_radius = size * 0.25
    body_center = (x, y)
    body = patches.Wedge(center=body_center, r=body_radius, theta1=20, theta2=160, color=color)
    ax.add_patch(body)
    

def draw_person_icon_matrix(ax, rows=5, cols=5, spacing=(1.5, 1.5), size=1, colors=None):
    """Draws a matrix of person icons with specified rows and columns, with optional individual colors for each block."""
    
    if colors is None:
        colors = [[(1, 1, 1, 1) for _ in range(cols)] for _ in range(rows)]
    
    for row in range(rows):
        for col in range(cols):
            x = col * spacing[0]
            y = (rows - row - 1) * spacing[1]
            color = colors[row][col] if row < len(colors) and col < len(colors[row]) else (1, 1, 1, 1)
            draw_person_icon(ax, x, y, size, color)

def nr_rows( nr_cols, nr_elements):
  nr = nr_elements/nr_cols
  inr = int(nr)
  if nr - inr > 0:
    inr += 1
  print( nr_cols, nr_elements, inr)
  return inr
  

def generate_colors(tp, tn, fp, fn, left_cols, right_cols):
    """Generates the color matrix based on the counts of TP, TN, FP, and FN, ordered as blocks for each confusion matrix part."""
    
    red = (0.5, 0, 0, 0.8)         # True Positives
    light_red = (0.5, 0, 0, 0.3)   # False Negatives
    green = (0, 0.39, 0, 0.8)      # True Negatives
    light_green = (0, 0.39, 0, 0.3) # False Positives
    white = (1, 1, 1, 1)           # White for unused spaces
    
    upper_rows = max( nr_rows( left_cols, tp), nr_rows( right_cols, fn))
    lower_rows = max( nr_rows( left_cols, fp), nr_rows( right_cols, tn))
  
    total_cols = left_cols + right_cols
    total_rows = upper_rows + lower_rows

    print( "rows", upper_rows, lower_rows)
    print( "total", total_rows, total_cols)  
  
    # Initialize color grid
    colors = [[white for _ in range(total_cols)] for _ in range(total_rows)]
    
    # Fill top-left block (TP)
    count = 0
    for i in range(upper_rows):
        for j in range(left_cols):
            count += 1
            if count <= tp:
              colors[i][j] = red
    
    # Fill top-right block (FP)
    count = 0
    for i in range(upper_rows):
        for j in range(left_cols, total_cols):
            count += 1
            if count <= fp:
              colors[i][j] = light_red
    
    # Fill bottom-left block (FN)
    count = 0
    for i in range(upper_rows, total_rows):
        for j in range(left_cols):
            count += 1
            if count <= fn:
              colors[i][j] = light_green
    
    # Fill bottom-right block (TN)
    count = 0
    for i in range(upper_rows, total_rows):
        for j in range(left_cols, total_cols):
            count += 1
            if count <= tn:
                colors[i][j] = green
    
    return colors

def draw_table(ax, rows, cols, spacing=(1.5, 1.5)):
    """Draws a table grid around the matrix of icons."""
    for row in range(rows + 1):
        y = row * spacing[1]
        ax.plot([0, cols * spacing[0]], [y, y], color="black", linewidth=1.5)
    for col in range(cols + 1):
        x = col * spacing[0]
        ax.plot([x, x], [0, rows * spacing[1]], color="grey", linewidth=1.5)

if __name__ == "__main__":
    
    # Define the number of True Positives, True Negatives, False Positives, and False Negatives
    tp = 10
    tn = 15
    fp = 5
    fn = 8
    
    # Define the dimensions of the matrix
    left_cols = 4
    right_cols = 4
    
    # Generate the color matrix based on the counts of TP, TN, FP, and FN
    colors = generate_colors(tp, tn, fp, fn, left_cols, right_cols)
    
    spacing = (0.6, 1.0)

    total_rows = len(colors)
    total_cols = max(len(row) for row in colors)

  
    fig, ax = plt.subplots(figsize=(total_cols * spacing[0], total_rows * spacing[1]))
    
    draw_person_icon_matrix(ax, rows=total_rows, cols=total_cols, spacing=spacing, size=0.8, colors=colors)

    # Draw dividing lines for the 4 blocks
    ax.plot([(left_cols-0.5) * spacing[0], (left_cols-0.5) * spacing[0]], [0, (total_rows+0.5) * spacing[1]], color="black", linewidth=3)  # Vertical line
    ax.plot([-2*spacing[0], (total_cols-0.5) * spacing[0]], [(total_rows+0.5) * spacing[1] / 2, (total_rows+0.5) * spacing[1] / 2], color="black", linewidth=3)  # Horizontal line

    # Draw outer lines for the 4 blocks
    ax.plot([(-0.5) * spacing[0], (-0.5) * spacing[0]], [-0*spacing[1], (total_rows+0.5) * spacing[1]], color="black", linewidth=3)  # Vertical line
    ax.plot([-2*spacing[0], (total_cols-0.5) * spacing[0]], [(total_rows - 0.25) * spacing[1], (total_rows - 0.25) * spacing[1]], color="black", linewidth=3)  # Horizontal line

    ax.text(total_cols * spacing[0] / 2, total_rows * spacing[1] + 0.6, 'Vorhergesagt', ha='center', va='center', fontsize=16, fontweight='bold')
    ax.text(-1.5, total_rows * spacing[1] / 2, 'Tatsächlich', ha='center', va='center', fontsize=16, fontweight='bold', rotation=90)

    ax.text( 0.2 * total_cols * spacing[0] , total_rows * spacing[1] , 'Krank', ha='center', va='center', fontsize=14, fontweight='bold')
    ax.text(0.7 * total_cols * spacing[0]  , total_rows * spacing[1] , 'Nicht krank', ha='center', va='center', fontsize=14, fontweight='bold')

    ax.text( -1.1 * spacing[0]  , 0.75 * total_rows * spacing[1] , 'Krank', ha='center', va='center', fontsize=14, fontweight='bold', rotation=90)
    ax.text( -1.1 * spacing[0]  , 0.25 * total_rows * spacing[1] , 'Nicht krank', ha='center', va='center', fontsize=14, fontweight='bold', rotation=90)

    
    ax.set_aspect('equal', 'box')
    ax.set_xlim(-3*spacing[0], total_cols * spacing[0])
    ax.set_ylim(-2*spacing[1], (total_rows+1) * spacing[1])
    ax.axis('off')  # Hide axis

    plt.savefig( 'icon_matrix_small.png')
    plt.show()
