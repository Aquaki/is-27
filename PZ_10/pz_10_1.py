# Известны марки машин, выпускаемые в данной стране и экспортируемых в N заданных
# стран. Определить какие марки машин были доставлены во все указанные страны, какие в
# некоторые из стран и какие не доставлены ни в одну страну.

def analyze_car_exports(domestic_cars, exports):
    # Если нет данных об экспорте
    if not exports:
        return set(), set(), domestic_cars.copy()

    # Получаем список всех стран
    countries = list(exports.keys())

    # Марки, экспортированные во все страны (пересечение всех множеств экспорта)
    all_countries = set(exports[countries[0]])
    for country in countries[1:]:
        all_countries &= exports[country]  # Используем оператор & для пересечения

    # Марки, экспортированные в некоторые страны (объединение всех множеств экспорта)
    some_countries = set()
    for country in countries:
        some_countries |= exports[country]  # Используем оператор | для объединения

    # Марки, не экспортированные ни в одну страну
    none_countries = domestic_cars - some_countries  # Используем оператор - для разности множеств

    return all_countries, some_countries, none_countries

# Пример данных
domestic_cars = {'Toyota', 'Honda', 'Nissan', 'Mazda', 'Subaru', 'Mitsubishi', 'BMW'}

# Данные об экспорте по странам
exports = {
    'USA': {'Toyota', 'Honda', 'Nissan', 'Subaru'},
    'Germany': {'Toyota', 'Honda', 'BMW'},
    'Russia': {'Toyota', 'Nissan', 'Mitsubishi'},
    'China': {'Toyota', 'Honda', 'Nissan', 'BMW'}
}
# Получаем результаты анализа
all_countries, some_countries, none_countries = analyze_car_exports(domestic_cars, exports)

print("Марки, экспортированные во все страны:", all_countries)
print("Марки, экспортированные в некоторые страны:", some_countries)
print("Марки, не экспортированные ни в одну страну:", none_countries)
