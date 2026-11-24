import os
import time

pid = os.fork()

if pid == 0:
    os._exit(0)

print("Parent:", os.getpid())
print("Child :", pid)

time.sleep(300)