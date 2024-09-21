import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Definindo as posições das tabelas no gráfico
positions = {
    'Área de Exibição': (0, 1),
    'Família de Animais': (2, 1),
    'Raças': (4, 1)
}

# Criando a figura
fig, ax = plt.subplots(figsize=(8, 4))

# Adicionando retângulos para representar as tabelas
ax.add_patch(mpatches.FancyBboxPatch((positions['Área de Exibição'][0], positions['Área de Exibição'][1]), 
                                     1.5, 1, boxstyle="round,pad=0.1", ec="black", fc="lightblue"))
ax.text(positions['Área de Exibição'][0] + 0.75, positions['Área de Exibição'][1] + 0.5, 
        'Área de Exibição\n- AreaID (PK)\n- Nome\n- Localizacao', 
        ha='center', va='center', fontsize=9)

ax.add_patch(mpatches.FancyBboxPatch((positions['Família de Animais'][0], positions['Família de Animais'][1]), 
                                     1.5, 1, boxstyle="round,pad=0.1", ec="black", fc="lightgreen"))
ax.text(positions['Família de Animais'][0] + 0.75, positions['Família de Animais'][1] + 0.5, 
        'Família de Animais\n- FamiliaID (PK)\n- Nome\n- Descricao\n- AreaID (FK)', 
        ha='center', va='center', fontsize=9)

ax.add_patch(mpatches.FancyBboxPatch((positions['Raças'][0], positions['Raças'][1]), 
                                     1.5, 1, boxstyle="round,pad=0.1", ec="black", fc="lightcoral"))
ax.text(positions['Raças'][0] + 0.75, positions['Raças'][1] + 0.5, 
        'Raças\n- RacaID (PK)\n- Nome\n- NomeCientifico\n- FamiliaID (FK)', 
        ha='center', va='center', fontsize=9)

# Desenhando as linhas de relacionamento
ax.arrow(1.5, 1.5, 0.5, 0, head_width=0.05, head_length=0.1, fc='black', ec='black')
ax.text(1.75, 1.55, '1:N', ha='center', va='center', fontsize=9)

ax.arrow(3.5, 1.5, 0.5, 0, head_width=0.05, head_length=0.1, fc='black', ec='black')
ax.text(3.75, 1.55, '1:N', ha='center', va='center', fontsize=9)

# Configurando o gráfico
ax.set_xlim(-0.5, 5)
ax.set_ylim(0.5, 2)
ax.axis('off')

# Exibindo o gráfico
plt.show()