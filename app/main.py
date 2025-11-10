import random
import tomllib
import os

# Загрузка конфигурации
try:
    with open('pyproject.toml', 'rb') as f:
        config = tomllib.load(f)
    tests_enabled = config['settings']['tests_enabled']
    print(f"Тесты включены: {tests_enabled}")
except:
    print("Ошибка загрузки config.toml, используем настройки по умолчанию")
    tests_enabled = False

# Бар
alcohol_bar = ["Teqilla", "Rum", "Vodka", "Gin"]
non_alco_bar = ["Cola", "Lemon juice", "Tripple sec", "Tonic", "Orange juice", "Sugar syrup", "Lemon-lime soda", "Blue curacao", "Grenadine"]
bar = alcohol_bar + non_alco_bar

# Коктейли
coctails = {
    "Long island": ["Teqilla", "Rum", "Vodka", "Gin", "Tripple sec", "Cola"],
    "Cuba libre": ["Rum", "Cola"],
    "Gin tonic": ["Gin", "Tonic"],
    "Margarita": ["Teqilla", "Tripple sec"],
    "Screwdriver": ["Vodka", "Orange juice"],
    "Gin sour": ["Gin", "Lemon juice", "Sugar syrup"],
    "Daiqiri": ["Rum", "Lime juice", "Sugar syrup"],
    "Electric lemonade": ["Vodka", "Lemon juice", "Sugar syrup", "Lemon-lime soda", "Blue curacao"],
    "Teqila sunrise": ["Teqilla", "Grenadine", "Orange juice"]
}

def get_coctail(val):
    for key, value in coctails.items():
        if val == value:
            return key
    return "No coctail"

def run(inp_bar):
    print("Input values:", list(set(inp_bar)))
    for recepie in coctails.values():
        remain = list(set(recepie) - set(inp_bar))
        if remain != recepie:
            if not remain:
                print(f"You got everything for {get_coctail(recepie)}.")
            else:
                remain = ", ".join(remain)
                print(f"For {get_coctail(recepie)} not enough {remain}.")
    print("")

# Основная логика
if tests_enabled:
    print("=== РЕЖИМ ТЕСТИРОВАНИЯ ===")
    for i in range(5):
        test_vals = [bar[random.randrange(len(bar))] for i in range(random.randrange(1, len(bar)))]
        run(test_vals)
else:
    print("=== ИНТЕРАКТИВНЫЙ РЕЖИМ ===")
    print("Доступные ингредиенты:", ", ".join(bar))
    print("Для выхода введите 'exit'")
    
    while True:
        user_input = input("\nВведите ингредиенты через запятую: ").strip()
        if user_input.lower() == 'exit':
            break
        
        if user_input:
            ingredients = [ingredient.strip() for ingredient in user_input.split(",")]
            run(ingredients)