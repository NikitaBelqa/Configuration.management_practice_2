import os

def simple_structure():
    lines = ["@startmindmap", "* cocktail_project/"]
    
    # Добавляем все что видим в проекте
    for item in os.listdir("."):
        if item.startswith('.'):
            continue
            
        if os.path.isdir(item):
            lines.append(f"** {item}")
            # Добавляем файлы внутри папки
            for file in os.listdir(item):
                if not file.startswith('.'):
                    lines.append(f"*** {file}")
        else:
            lines.append(f"** {item}")
    
    lines.append("@endmindmap")
    
    with open("project_structure.puml", "w") as f:
        f.write("\n".join(lines))
    
    print("Готово! Диаграмма создана.")

simple_structure()