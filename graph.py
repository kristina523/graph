import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.unicode_minus'] = False

fig, ax = plt.subplots(figsize=(12, 8))

intersection_x = 354
intersection_y = 227

nou_start = 92.8  


k1 = (intersection_y - nou_start) / intersection_x
x_nou = np.linspace(0, 800, 100)
y_nou = nou_start + k1 * x_nou
k2 = intersection_y / intersection_x
x_val = np.linspace(0, 800, 100)
y_val = k2 * x_val

ax.plot(x_nou, y_nou, 'b-', linewidth=2, label='nou')
ax.plot(x_val, y_val, 'r-', linewidth=2, label='ВАЛ')

ax.plot(intersection_x, intersection_y, 'ko', markersize=8)
ax.axvline(x=intersection_x, color='gray', linestyle='--', linewidth=1, alpha=0.7)
ax.axhline(y=intersection_y, color='gray', linestyle='--', linewidth=1, alpha=0.7)

y_800 = k2 * 800
ax.plot(800, y_800, 'ro', markersize=6)
ax.axvline(x=800, color='gray', linestyle='--', linewidth=1, alpha=0.5)

ax.set_xlabel('штук', fontsize=12)
ax.set_ylabel('тыс', fontsize=12, rotation=0, labelpad=20)
ax.set_xlim(0, 900)
ax.set_ylim(0, 350)

ax.set_xticks([100, 200, 300, 354, 800])
ax.set_xticklabels(['100', '200', '300', '354', '800'])
ax.set_yticks([100, 200, 300])
ax.set_yticklabels(['100', '200', '300'])

ax.plot(0, nou_start, 'bo', markersize=6)
ax.text(-40, nou_start, '92800', fontsize=9, verticalalignment='center')
ax.text(intersection_x + 10, intersection_y, '227', fontsize=9, verticalalignment='center')
ax.text(-40, 344, '344000', fontsize=9, verticalalignment='center')
ax.plot(0, 344, 'bo', markersize=4, alpha=0.5)
ax.text(850, 340, 'Выр.', fontsize=10, style='italic')
ax.grid(True, alpha=0.3, linestyle='-', linewidth=0.5)
ax.legend(loc='upper left', fontsize=10)
ax.set_title('График анализа безубыточности', fontsize=14, pad=20)
plt.tight_layout()
plt.savefig('graph.png', dpi=300, bbox_inches='tight')
print("График сохранен в файл 'graph.png'")

plt.show()

