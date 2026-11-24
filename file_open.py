import time
f=open("/tmp/arrise-held.log","wb")
f.write(b"x" * 20 * 1024 * 1024)
f.flush()
print("File created and kept open")
time.sleep(300)
f.close()