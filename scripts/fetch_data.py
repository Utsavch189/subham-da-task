import requests
import time

URL='http://127.0.0.1:8000/api/v1/get-data'

start=time.perf_counter()

resp=requests.get(URL)

end=time.perf_counter()
print(f"time : {end-start}")
print(resp)