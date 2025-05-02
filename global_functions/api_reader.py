from http.client import responses

import requests
import sys
from logging import basicConfig, info, INFO

from requests import request

from config import LOGS_PATH

basicConfig(level=INFO,
            filename=LOGS_PATH,
            filemode="w",
            format="%(asctime)s %(levelname)s %(message)s")

# --- НАСТРОЙКА ---
# Укажите базовый URL вашего запущенного C# веб-сервиса.
# Обычно это http://localhost:5000 или https://localhost:5001
# Проверьте настройки запуска вашего C# проекта (Properties/launchSettings.json)
BASE_URL = "http://localhost:5052"

def ping():
    response = requests.get(BASE_URL, timeout=20)
    return True if response.status_code == 200 else response.status_code


def get_eve_module_quantity(pid: int) -> int | None:

    if not isinstance(pid, int) or pid <= 0:
        info(f"Ошибка: Неверный PID процесса: {pid}")
        return None

    url = f"{BASE_URL}/api/eve/quantity/{pid}"
    info(f"[PythonClient] Отправка запроса на: {url}")  # Для отладки

    try:
        response = requests.get(url, timeout=1000)
        info(response.status_code)
        if response.status_code == 200:
            try:
                data = response.json()
                quantity = data.get('quantity')

                if quantity is not None and isinstance(quantity, (
                int, float)):  # float добавлен из-за возможного чтения как double в C#
                    result = int(quantity)  # Преобразуем в int, если нужно
                    info(f"[PythonClient] Успешно получено quantity={result} для PID={pid}")
                    return result
                else:
                    info(
                        f"[PythonClient] Ошибка: Ответ от сервера не содержит целочисленное или числовое поле 'quantity'. Ответ: {data}")
                    return None
            except requests.exceptions.JSONDecodeError:
                info(
                    f"[PythonClient] Ошибка: Не удалось декодировать JSON из ответа сервера. Статус: {response.status_code}. Ответ: {response.text}"
                    )
                return None
            except ValueError:
                info(
                    f"[PythonClient] Ошибка: Не удалось преобразовать полученное значение '{quantity}' в целое число."
                    )
                return None

        elif response.status_code == 404:
            info(
                f"[PythonClient] Ошибка: Данные для PID {pid} не найдены (404). Убедитесь, что клиент EVE запущен и модуль/поле доступны."
                )
            try:
                error_data = response.json()
                info(f"   Сообщение сервера: {error_data.get('error', response.text)}")
            except requests.exceptions.JSONDecodeError:
                info(f"   Тело ответа: {response.text}")
            return None
        else:
            info(f"[PythonClient] Ошибка: Сервер вернул статус {response.status_code} для PID {pid}.")
            try:
                error_data = response.json()
                info(f"   Сообщение сервера: {error_data.get('detail', error_data.get('title', response.text))}"
                      )
            except requests.exceptions.JSONDecodeError:
                info(f"   Тело ответа: {response.text}")
            return None

    except requests.exceptions.ConnectionError:
        info(
            f"[PythonClient] Ошибка: Не удалось подключиться к веб-сервису по адресу {BASE_URL}. Убедитесь, что C# сервис запущен."
            )
        return None
    except requests.exceptions.Timeout:
        info(f"[PythonClient] Ошибка: Превышено время ожидания ответа от сервера {url}.")
        return None
    except requests.exceptions.RequestException as e:
        info(f"[PythonClient] Ошибка: Произошла ошибка при выполнении запроса к {url}: {e}")
        return None



if __name__ == "__main__":
    target_pid = 15076

    print(f"\n--- Тестовый запуск ---")
    print(f"Пытаемся получить 'quantity' для PID: {target_pid}")

    quantity_result = get_eve_module_quantity(target_pid)

    print(quantity_result)