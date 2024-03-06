import sqlite3
from faker import Faker
import random
import threading
from datetime import datetime

fake = Faker()
lock=threading.Lock()


def insert_data(thread_id):
    conn = sqlite3.connect('D:\\subham-da-task\\backend\\db.sqlite3', timeout=60)
    c = conn.cursor()

    try:
        for _ in range(100000):
            insert_query = """INSERT INTO api_people(name, age, registered_at)
                              VALUES('%s', %d, '%s')""" % (fake.name(), random.randint(19, 66), datetime.now())
            c.execute(insert_query)
        conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()
    finally:
        c.close()
        conn.close()


def insert_in_threads(thread_count):
    threads = []

    for i in range(thread_count):
        thread = threading.Thread(target=insert_data, args=(i,), daemon=True)
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    thread_count = 5
    insert_in_threads(thread_count)
    print("Data insertion complete.")