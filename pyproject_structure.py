import os

def show_structure():
    print("Структура проекта:")
    for root, dirs, files in os.walk("."):
        # Пропускаем служебные папки
        if '__pycache__' in dirs:
            dirs.remove('__pycache__')
        if '.git' in dirs:
            dirs.remove('.git')
        
        level = root.count(os.sep) - 1
        indent = ' ' * 2 * level
        print(f"{indent}{os.path.basename(root)}/")
        
        for file in files:
            if file.endswith(('.py', '.toml')):
                print(f"{indent}  {file}")

if __name__ == "__main__":
    show_structure()