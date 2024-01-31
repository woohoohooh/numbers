import json
import urllib3
import pyautogui
import time
import random

countries = [
    'argentina', 'australia', 'austria', 'belgium', 'brazil', 'bulgaria', 'canada',
    'chile', 'colombia', 'czech', 'finland', 'france', 'germany', 'greece', 'hong',
    'hungary', 'iceland', 'india', 'israel', 'italy', 'japan', 'kazakhstan', 'mexico',
    'netherlands', 'zealand', 'norway', 'poland', 'romania', 'russia', 'serbia', 'singapore',
    'korea', 'spain', 'sweden', 'switzerland', 'turkey', 'ukraine', 'kingdom', 'states'
]

# kuban, rnd
# moskva, nsk, spb, e-burg, chel, yaroslavl, barnaul, amur, arkhangelsk, astrakhan, belgorod, tomsk, omsk, khv, vologda, 'tatarstan', 'kemerovo', 'perm', 'khakasia', 'kras', 'nov', 'bryansk', 'vladimir', 'volgograd', 'voronezh', 'primorye', 'eao', 'chita', 'ivanovo',
# 'irkutsk', 'kbr', 'kaliningrad', 'kaluga', 'kamchatka', 'kchr', 'kirov', 'kostroma', 'kurgan', 'kursk', 'lipetsk', 'magadan', 'murmansk', 'nao', 'nnov', 'orenburg', 'orel',
# 'penza', 'buryatia', 'dagestan', 'magas', 'elista', 'karelia', 'komi', 'mari-el', 'mordovia', 'sakha', 'alania', 'tyva', 'saratov', 'ryazan', 'samara', 'sakh', 'smolensk', 'stavropol', 'tambov', 'tver', 'tula',
# 'tyumen', 'udm', 'uln', 'yugra', 'chechnya', 'chuvashia', 'chukotka', 'yamal'

cities = []

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
        time.sleep(8)
    except KeyboardInterrupt:
        print("Stop.")

def fetch_and_save_phones(region):
    while True:
        try:
            url = f'https://{region}.mts.ru/json/numberselection/getfreephones?inputMask=&msisdnCount=10&lowPrice=0&topPrice=0'
            http = urllib3.PoolManager(cert_reqs='CERT_NONE', assert_hostname=False)
            response = http.request('GET', url, timeout=3)
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
            random_delay = random.uniform(1, 5)
            time.sleep(random_delay)
        except:
            break

def start():
    for region in cities:
        for i in countries:
            clicks(i)
            fetch_and_save_phones(region)
            time.sleep(5)
        time.sleep(100)
start()