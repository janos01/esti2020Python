import time

pil = time.time()

print(pil)

print(time.localtime(pil))
localtime = time.localtime(pil)
print(time.asctime(localtime))

print(localtime.tm_year)
