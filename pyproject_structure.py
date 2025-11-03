import os
from pathlib import Path

def print_project_structure(start_path='.'):
    """Выводит структуру проекта в виде дерева"""
    print("Структура проекта:")
    print(".")
    
    for root, dirs, files in os.walk(start_path):
        # Пропускаем служебные папки
        if '__pycache__' in dirs:
            dirs.remove('__pycache__')
        if '.git' in dirs:
            dirs.remove('.git')
        
        level = root.replace(start_path, '').count(os.sep)
        indent = ' ' * 2 * level
        print(f"{indent}{os.path.basename(root)}/")
        
        subindent = ' ' * 2 * (level + 1)
        for file in files:
            if file.endswith(('.py', '.toml', '.txt')):
                print(f"{subindent}{file}")

if __name__ == "__main__":
    print_project_structure()