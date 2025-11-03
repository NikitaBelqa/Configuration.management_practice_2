import tomli
import os
import sys

# Добавляем пути для импорта
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from Vehicles.Car import Car
from Vehicles.ElectricCar import ElectricCar

def load_config():
    """Загружает конфигурацию из pyproject.toml"""
    try:
        with open('pyproject.toml', 'rb') as f:
            config = tomli.load(f)
        return config
    except FileNotFoundError:
        print("Ошибка: Файл pyproject.toml не найден!")
        return {}

def main():
    # Загружаем и выводим настройки
    config = load_config()
    
    print("=== НАСТРОЙКИ ИЗ TOML ФАЙЛА ===")
    if 'tool' in config and 'vehicle' in config['tool']:
        vehicle_config = config['tool']['vehicle']
        for key, value in vehicle_config.items():
            print(f"{key}: {value}")
    else:
        print("Конфигурация vehicle не найдена")
    
    print("\n=== РАБОТА ПРИЛОЖЕНИЯ ===")
    
    # Демонстрация работы с классами
    car = Car("Toyota", "Camry", 2020)
    electric_car = ElectricCar("Tesla", "Model S", 2023, 75)
    
    print(car.get_info())
    print(electric_car.get_info())
    electric_car.charge_battery(50)
    print(f"Уровень заряда: {electric_car.battery_level}%")

if __name__ == "__main__":
    main()