from functools import wraps
from functools import reduce
from time import time
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def check_performance(repeats):
    def inner(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            attempts = []
            for repeat in range(repeats):
                start_time = time()
                print(f"Executing function: {fn.__name__}")
                result = fn(*args, **kwargs)
                end_time = time() - start_time
                print(f"Response: {result}")
                print(f"Time: {end_time}")
                attempts.append(end_time)
            average_time = reduce(lambda x, y: x + y, attempts) / len(attempts)
            print(f"Average URL time: {average_time}")
            return result
        return wrapper
    return inner

repeats = 15
headers = {"Cache-Control": "no-cache"}

@check_performance(repeats)
def get_url(url):
    try:
        response = requests.get(url, headers=headers, verify=False)        
    except requests.exceptions.RequestException as err:
        return err
    return response

#reply = get_url("https://postman-echo.com/get?foo1=bar1&foo2=bar2")
reply = get_url("https://google.com")
print(reply)
