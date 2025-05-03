'''
Клиент для взаимодействия с локальным веб-сервисом EveApiReader.
'''
import requests
import sys
from logging import basicConfig, info, INFO
from http.client import responses

# Убедитесь, что config.py существует и LOGS_PATH определен
# Если нет, замените строку ниже или создайте config.py
try:
    from config import LOGS_PATH
except ImportError:
    LOGS_PATH = "eve_client.log"  # Значение по умолчанию

basicConfig(level=INFO,
            filename=LOGS_PATH,
            filemode="w",
            format="%(asctime)s %(levelname)s %(message)s")

# --- НАСТРОЙКА ---
# Укажите базовый URL вашего запущенного C# веб-сервиса.
# Обычно это http://localhost:5000 или https://localhost:5001
# Проверьте настройки запуска вашего C# проекта (Properties/launchSettings.json)
BASE_URL = "http://localhost:5052"


# -------------

def ping():
    try:
        response = requests.get(BASE_URL, timeout=20)
        return True if response.status_code == 200 else response.status_code
    except requests.exceptions.RequestException as e:
        info(f"[ping] Ошибка подключения к {BASE_URL}: {e}")
        return False


def reset_eve_cache(pid: int):
    """Отправляет запрос на сброс кэша для указанного PID."""
    if not isinstance(pid, int) or pid <= 0:
        info(f"[reset_cache] Ошибка: Неверный PID процесса: {pid}")
        return False
    url = f"{BASE_URL}/api/eve/cache/{pid}"
    info(f"[reset_cache] Отправка запроса DELETE на: {url}")
    try:
        response = requests.delete(url, timeout=10)
        if response.status_code == 200:
            info(f"[reset_cache] Кэш для PID {pid} успешно сброшен сервером.")
            return True
        else:
            info(f"[reset_cache] Ошибка: Сервер вернул статус {response.status_code} при сбросе кэша для PID {pid}.")
            return False
    except requests.exceptions.RequestException as e:
        info(f"[reset_cache] Ошибка при запросе DELETE к {url}: {e}")
        return False


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
        info(f"[get_quantity] Ошибка: Неверный PID процесса: {pid}")
        return None

    url = f"{BASE_URL}/api/eve/quantity/{pid}"
    info(f"[PythonClient] Отправка запроса на: {url}")

    try:
        # Используем ваш таймаут
        response = requests.get(url, timeout=1000)
        info(f"[PythonClient] Статус ответа: {response.status_code}")

        if response.status_code == 200:
            try:
                data = response.json()
                quantity = data.get('quantity')

                if quantity is not None and isinstance(quantity, (int, float)):
                    result = int(quantity)
                    info(f"[PythonClient] Успешно получено quantity={result} для PID={pid}")
                    return result
                else:
                    info(
                        f"[PythonClient] Ошибка: Ответ 200 OK, но некорректное поле 'quantity'. Ответ: {data}. Сбрасываем кэш.")
                    reset_eve_cache(pid)  # <<< СБРОС КЭША
                    return None
            except requests.exceptions.JSONDecodeError:
                info(
                    f"[PythonClient] Ошибка: Не удалось декодировать JSON из ответа 200 OK. Статус: {response.status_code}. Ответ: {response.text}. Сбрасываем кэш.")
                reset_eve_cache(pid)  # <<< СБРОС КЭША
                return None
            except ValueError:
                info(
                    f"[PythonClient] Ошибка: Не удалось преобразовать значение '{quantity}' в целое число. Сбрасываем кэш.")
                reset_eve_cache(pid)  # <<< СБРОС КЭША
                return None

        elif response.status_code == 404:
            info(f"[PythonClient] Ошибка: Данные для PID {pid} не найдены (404). Сбрасываем кэш.")
            reset_eve_cache(pid)  # <<< СБРОС КЭША
            try:
                error_data = response.json()
                info(f"   Сообщение сервера: {error_data.get('error', response.text)}")
            except requests.exceptions.JSONDecodeError:
                info(f"   Тело ответа: {response.text}")
            return None
        else:
            info(f"[PythonClient] Ошибка: Сервер вернул статус {response.status_code} для PID {pid}. Сбрасываем кэш.")
            reset_eve_cache(pid)  # <<< СБРОС КЭША
            try:
                error_data = response.json()
                info(f"   Сообщение сервера: {error_data.get('detail', error_data.get('title', response.text))}")
            except requests.exceptions.JSONDecodeError:
                info(f"   Тело ответа: {response.text}")
            return None

    except requests.exceptions.ConnectionError:
        info(
            f"[PythonClient] Ошибка: Не удалось подключиться к веб-сервису по адресу {BASE_URL}. Убедитесь, что C# сервис запущен.")
        return None
    except requests.exceptions.Timeout:
        info(f"[PythonClient] Ошибка: Превышено время ожидания ответа от сервера {url}.")
        return None
    except requests.exceptions.RequestException as e:
        info(f"[PythonClient] Ошибка: Произошла ошибка при выполнении запроса к {url}: {e}")
        return None
