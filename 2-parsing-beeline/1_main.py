import json
import urllib3
import time
import random

region = 'moskva'

def fetch_and_save_phones(region):
    while True:
        try:
            url = f'https://{region}.beeline.ru/fancynumber/all/'
            http = urllib3.PoolManager(cert_reqs='CERT_NONE', assert_hostname=False)
            response = http.request('GET', url, timeout=3)
            if response.status == 200:
                print('yes')
                data = json.loads(response.data.decode('utf-8-sig'))
                a = data['numbers'][3]['numbers']
                with open('new.txt', 'a', encoding='utf8') as f:
                    for i in a:
                        f.write(f"7{i['value']}")
                        f.write('\n')
            random_delay = random.uniform(1, 10)
            time.sleep(random_delay)
        except Exception as e:
            print(f"An error occurred: {e}")

fetch_and_save_phones(region)