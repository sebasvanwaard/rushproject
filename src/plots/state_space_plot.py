import matplotlib.pyplot as plt

boards = ['6x6_1', '6x6_2', '6x6_3', '9x9_4', '9x9_5', '9x9_6', '12x12_7']
state_space = [1000000, 976562500, 976562500, 1.94*(10**19), 2.12*(10**21), 1.04*(10**23), 1.44*(10**45)]

plt.figure(figsize=(10, 6))
plt.plot(boards, state_space, 'ro-', label='State Space')

plt.yscale('log')

plt.xlabel('Board')
plt.ylabel('State Space')
plt.title('State Space Size for Different Gameboards')

for i, value in enumerate(state_space):
    plt.annotate(f'{value:.2e}', (boards[i], value), color='red', fontsize=7, ha='right', va='bottom', rotation=-5, rotation_mode='anchor', xytext=(-5, 5), textcoords='offset points')

plt.grid(True, which='both', linestyle='--', linewidth=0.5)

plt.legend()
plt.tight_layout()
plt.show()