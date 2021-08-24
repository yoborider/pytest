import time

tic = time.perf_counter()
mafonc = lambda x:x+1
for i in range(0,5000):
    print(mafonc(i))
toc = time.perf_counter()
print(f"processed in {toc-tic:0.4f} seconds")