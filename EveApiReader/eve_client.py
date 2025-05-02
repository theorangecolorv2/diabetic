'''
Клиент для взаимодействия с локальным веб-сервисом EveApiReader.
'''
import requests
import sys

# --- НАСТРОЙКА --- 
# Укажите базовый URL вашего запущенного C# веб-сервиса.
# Обычно это http://localhost:5000 или https://localhost:5001
# Проверьте настройки запуска вашего C# проекта (Properties/launchSettings.json)
BASE_URL = "http://localhost:5000" 
# ------------- 

def get_eve_module_quantity(pid: int) -> int | None:
    """
    Получает значение 'quantity' для указанного модуля EVE Online,
    обращаясь к локальному веб-сервису EveApiReader.

    Args:
        pid: ID процесса EVE Online.

    Returns:
        Значение quantity (целое число) или None, если произошла ошибка
        или значение не найдено.
    """
    if not isinstance(pid, int) or pid <= 0:
        print(f"Ошибка: Неверный PID процесса: {pid}", file=sys.stderr)
        return None

    # Формируем полный URL для запроса
    url = f"{BASE_URL}/api/eve/quantity/{pid}"
    print(f"[PythonClient] Отправка запроса на: {url}") # Для отладки

    try:
        # Отправляем GET-запрос с таймаутом
        response = requests.get(url, timeout=10) 

        # Проверяем статус код ответа
        if response.status_code == 200:
            # Если успешно (200 OK)
            try:
                data = response.json() # Пытаемся разобрать JSON
                quantity = data.get('quantity') # Получаем значение по ключу 'quantity'
                
                # Дополнительная проверка типа, т.к. C# может вернуть long
                if quantity is not None and isinstance(quantity, (int, float)): # float добавлен из-за возможного чтения как double в C#
                     result = int(quantity) # Преобразуем в int, если нужно
                     print(f"[PythonClient] Успешно получено quantity={result} для PID={pid}")
                     return result
                else:
                     print(f"[PythonClient] Ошибка: Ответ от сервера не содержит целочисленное или числовое поле 'quantity'. Ответ: {data}", file=sys.stderr)
                     return None
            except requests.exceptions.JSONDecodeError:
                # Если ответ не является валидным JSON
                print(f"[PythonClient] Ошибка: Не удалось декодировать JSON из ответа сервера. Статус: {response.status_code}. Ответ: {response.text}", file=sys.stderr)
                return None
            except ValueError:
                 # Ошибка при преобразовании float в int
                 print(f"[PythonClient] Ошибка: Не удалось преобразовать полученное значение '{quantity}' в целое число.", file=sys.stderr)
                 return None
                 
        elif response.status_code == 404:
            # Если ресурс не найден (404 Not Found)
            print(f"[PythonClient] Ошибка: Данные для PID {pid} не найдены (404). Убедитесь, что клиент EVE запущен и модуль/поле доступны.", file=sys.stderr)
            try:
                # Попытка извлечь сообщение об ошибке из JSON ответа
                error_data = response.json()
                print(f"   Сообщение сервера: {error_data.get('error', response.text)}", file=sys.stderr)
            except requests.exceptions.JSONDecodeError:
                 # Если тело ответа не JSON, выводим как текст
                 print(f"   Тело ответа: {response.text}", file=sys.stderr)
            return None
        else:
            # Другие ошибки HTTP (например, 500 Internal Server Error)
            print(f"[PythonClient] Ошибка: Сервер вернул статус {response.status_code} для PID {pid}.", file=sys.stderr)
            try:
                # Попытка извлечь детали ошибки из JSON ответа
                error_data = response.json()
                print(f"   Сообщение сервера: {error_data.get('detail', error_data.get('title', response.text))}", file=sys.stderr)
            except requests.exceptions.JSONDecodeError:
                # Если тело ответа не JSON, выводим как текст
                print(f"   Тело ответа: {response.text}", file=sys.stderr)
            return None

    except requests.exceptions.ConnectionError:
        # Ошибка соединения (сервис не запущен или недоступен)
        print(f"[PythonClient] Ошибка: Не удалось подключиться к веб-сервису по адресу {BASE_URL}. Убедитесь, что C# сервис запущен.", file=sys.stderr)
        return None
    except requests.exceptions.Timeout:
        # Превышено время ожидания ответа
        print(f"[PythonClient] Ошибка: Превышено время ожидания ответа от сервера {url}.", file=sys.stderr)
        return None
    except requests.exceptions.RequestException as e:
        # Любые другие ошибки библиотеки requests
        print(f"[PythonClient] Ошибка: Произошла ошибка при выполнении запроса к {url}: {e}", file=sys.stderr)
        return None

# --- Пример использования --- 
# Этот блок выполнится, только если скрипт запускается напрямую (python eve_client.py)
if __name__ == "__main__":
    # ЗАМЕНИТЕ НА РЕАЛЬНЫЙ PID ПРОЦЕССА EVE ONLINE!
    # Его можно найти, например, в Диспетчере задач Windows (вкладка "Подробности")
    target_pid = 12345 
    
    print(f"\n--- Тестовый запуск ---") 
    print(f"Пытаемся получить 'quantity' для PID: {target_pid}")
    
    quantity_result = get_eve_module_quantity(target_pid)

    if quantity_result is not None:
        print(f"\n[РЕЗУЛЬТАТ] Полученное значение quantity: {quantity_result}")
    else:
        print(f"\n[РЕЗУЛЬТАТ] Не удалось получить quantity для PID {target_pid}.")
        print("   Возможные причины:")
        print("   1. C# веб-сервис EveApiReader не запущен.")
        print(f"   2. Неверно указан BASE_URL ('{BASE_URL}'). Проверьте порт.")
        print(f"   3. Неверно указан PID процесса EVE Online ('{target_pid}').")
        print("   4. Клиент EVE Online не запущен или не отвечает.")
        print(f"   5. Ошибка внутри C# сервиса (проверьте его логи). Не найден слот '{EveModuleReader.TargetSlotName}' или поле '{EveModuleReader.TargetQuantityField}'.")

    # Пример вызова для несуществующего PID (для проверки обработки 404)
    # print("\n--- Тест с несуществующим PID ---")
    # get_eve_module_quantity(999999)

    # Пример вызова с некорректным PID
    # print("\n--- Тест с некорректным PID ---")
    # get_eve_module_quantity(-5) 