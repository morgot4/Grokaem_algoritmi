from pydantic_settings import BaseSettings, SettingsConfigDict
from divide_and_conquer import f

class Settings(BaseSettings):
    MODEL: str
    model_config = SettingsConfigDict(env_file=".env")

def binary_search(lst: list, item):
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = lst[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 23412, 223344343]
print(binary_search(my_list, 2))