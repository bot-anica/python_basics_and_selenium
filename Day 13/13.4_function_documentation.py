import requests

# ---------- ДОКУМЕНТАЦИЯ ФУНКЦИЙ
print("----- ДОКУМЕНТАЦИЯ ФУНКЦИЙ -----")


def find_factorial(number):
    """
    Функция вычисления факториала числа

    Факториал числа - произведение всех натуральных чисел от 1 до n
    Например: 5! = 1*2*3*4*5 = 120

    :param number: Число для вычисления факториала
    :type number: int
    :return: Факториал числа number
    :rtype: int
    1:raises ValueError: Если number < 0
    """

    if number < 0:
        raise ValueError("Факториал отрицательного числа не определен")
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    return factorial


def get_weather(city):
    """
    Функция получения текущей погоды в указанном городе.

    Использует https://api.openweathermap.org/ для получения данных.

    :param city: Название города
    :type city: str
    :return: Словарь содержащий информацию о погоде (температуру, влажность и т.д.)
    :rtype: dict
    """

    api_key = "48615d934c9be0f6622a8631147759da"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}"
    response = requests.get(url)

    print(url)

    if response.status_code == 200:
        data = response.json()
        return {
            "city": city,
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "pressure": data["main"]["pressure"],
        }

    print("Не удалось получить данные о погоде в указанном городе")

    return {}


print(get_weather("Ivano-Frankivsk"))
