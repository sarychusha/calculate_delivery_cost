def calculate_delivery_cost(distance, size, fragility, load):
    """Функция расчета стоимости доставки в зависимости от расстояния, габаритов груза, хрупкости груза и загруженности службы доставки"""
    #Минимальная стоимость доставки, сделала ее отдельной переменной, чтобы при изменении было легко поправить значение
    MIN_COST = 400

    # Валидация входных данных
    if not isinstance(distance, (int, float)) or distance <= 0:
        raise ValueError("Distance must be a positive number.")

    if size not in ['small', 'big']:
        raise ValueError("Size must be 'small' or 'big'.")

    if fragility not in [True, False]:
        raise ValueError("Fragility must be True or False.")

    if load not in ['very_high', 'high', 'increased', 'normal']:
        raise ValueError("Load must be one of: 'very_high', 'high', 'increased', 'normal'.")

    ###ПОЯСНЕНИЕ###
    #Так как в требованиях не было очевидно к какой конретно стоимости граничное значение, например, 2 км,
    # считала что где говорится до - это = до включительно, где от - там невключительно
    if distance > 30.0:
        cost = 300
    elif distance > 10.0:
        cost = 200
    elif distance > 2.0:
        cost = 100
    else:
        cost = 50

    # Add cost based on size
    cost += 200 if size == 'big' else 100

    # Добавляем стоимость за хрупкость, но с условием, что при этом расстояние не должно быть больше 30 км
    if fragility:
        if distance > 30.0:
            raise ValueError("Fragile goods cannot be transported over 30 km.")
        cost += 300

    load_coefficients = {
        'very_high': 1.6,
        'high': 1.4,
        'increased': 1.2,
        'normal': 1.0
    }

    # Учитываем коэффициент загружености
    final_cost = round(cost * load_coefficients[load], 2)
    # Учитываем условие, что доставка не может быть ниже минимальной стоимости доставки
    return max(final_cost, MIN_COST)

# Пример использования
# print(calculate_delivery_cost(15, 'small', True, 'normal'))