from global_functions.api_reader import get_eve_module_quantity, ping
from global_functions.choose_mission import choose_mission_and_run
from global_functions.get_pid import get_pid


def main():
    working = True
    count = 0

    print("инициализирум и проверяем веб-сервер")
    if not ping():
        print(f"сервер лежит, код: {ping()}")
        return Exception("сервер лежит ")
    else:
        print("сервер работает")


    while working:
        choose_mission_and_run()
        count += 1
        print("\n")
        print("_"*50)
        print(f"миссий сделано: {count} \n")


main()