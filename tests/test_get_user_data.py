import requests
import allure
from jsonschema import validate
from core.contracts import USER_DATA_SCHEME

BASE_URL = "https://reqres.in/"
LIST_USERS = "api/users?page=2"
EMAIL_ENDS = "@reqres.in"

@allure.title("Проверяем получение списка пользователей")
def test_list_users():
    with allure.step("Делаем запрос по адресу api/users?page=2"):
        response = requests.get(BASE_URL+LIST_USERS)
    with allure.step("Делаем запрос по адресу api/users?page=2"):
        assert response.status_code == 200, f"Ожидаемый статус 200, получен {response.status_code}"

    data = response.json()['data']
    for item in data:
        with allure.step("Проверяем элемент из списка"):
            validate(item, USER_DATA_SCHEME)
            with allure.step("Проверяем окончание email адреса"):
                assert item['email'].endswith(EMAIL_ENDS)


