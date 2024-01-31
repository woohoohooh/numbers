import json
import urllib3
import pyautogui
import time

countries = [
    'australia', 'austria', 'belgium', 'brazil', 'bulgaria', 'canada',
    'chile', 'colombia', 'czech', 'finland', 'france', 'germany', 'greece', 'hong',
    'hungary', 'iceland', 'india', 'israel', 'italy', 'japan', 'kazakhstan', 'mexico',
    'netherlands', 'zealand', 'norway', 'poland', 'romania', 'russia', 'serbia', 'singapore',
    'korea', 'spain', 'sweden', 'switzerland', 'turkey', 'ukraine', 'kingdom', 'states'
]

region = 'Sankt-Peterburg'
region2 = 'spb'

qqq = 19

def clicks(country):
    try:
        pyautogui.moveTo(75, 1050)
        pyautogui.click()
        time.sleep(2)
        pyautogui.moveTo(75, 950)
        pyautogui.click()
        time.sleep(2)
        pyautogui.typewrite(country)
        time.sleep(2)
        pyautogui.moveTo(75, 600)
        pyautogui.click()
        time.sleep(5)
        pyautogui.moveTo(1520, 15)
        pyautogui.click()
        time.sleep(2)

    except KeyboardInterrupt:
        print("Stop.")

def fetch_and_save_phones():
    url = f'https://{region2}.mts.ru/json/numberselection/getfreephones?inputMask=&msisdnCount=10&lowPrice=0&topPrice=0'
    http = urllib3.PoolManager(cert_reqs='CERT_NONE', assert_hostname=False)
    response = http.request('GET', url)
    if response.status == 200:
        data = json.loads(response.data.decode('utf-8'))
        if isinstance(data, list):
            with open(f'{region}_new.txt', 'a') as file:
                for item in data:
                    msisdn = item.get('msisdn')
                    if msisdn:
                        file.write(f"+{msisdn}\n")
            print("Номера телефонов успешно записаны в файл phones.txt")
        else:
            print("Ошибка: Ответ не содержит ожидаемую структуру JSON.")
    else:
        print(f"Ошибка при получении данных. Код ответа: {response.status}")

count = len(countries)

clicks('argentina')

fetch_and_save_phones()
