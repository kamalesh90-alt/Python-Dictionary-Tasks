def produce_car(manufacturer, model, **car_attributes):
    print(f"Manufacturer: {manufacturer}")
    print(f"Model: {model}")
    print("Additional attributes:")
    for attribute, value in car_attributes.items():
        print(f"  {attribute.capitalize()}: {value}")

def main():
    car_info = {
        'color': 'Black',
        'tow_package': True,
        'top_speed': 220
    }
    produce_car('BMW', 'Outback', **car_info)

if __name__ == "__main__":
    main()