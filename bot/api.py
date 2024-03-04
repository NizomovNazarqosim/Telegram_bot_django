import requests
from datetime import date


BASE_URL = 'http://localhost:8000/api/v1'

def get_staffs():
    url = f"{BASE_URL}/staffs"
    response = requests.get(url=url)
    return response

def get_birthday_staff():
    today = date.today()
    staff_birth = []
    url = f"{BASE_URL}/staffs"
    data = requests.get(url=url)
    print('data-----', data)

    employees_today = data.objects.filter(birthdate__day=today.day, birthdate__month=today.month)
    return employees_today

# def get_admins():
#     admins = []
#     url = f"{BASE_URL}/staffs"
#     response = requests.get(url=url)
#     for i in range(len(response)):
#         if i[]



