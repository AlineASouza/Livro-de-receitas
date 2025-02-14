import os

recipes_dir = 'receitas'
index_file = 'indice.md'

def generate_index():
    with open(index_file, 'w', encoding='utf-8') as index:
        index.write('# Índice de Receitas\n\n')
        index.write('## Receitas\n\n')
        for recipe in sorted(os.listdir(recipes_dir)):
            if recipe.endswith('.md'):
                recipe_name = recipe.replace('-', ' ').replace('.md', '').title()
                index.write(f'- [{recipe_name}]({recipes_dir}/{recipe})\n')

if __name__ == '__main__':
    generate_index()
