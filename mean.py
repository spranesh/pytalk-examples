import scipy

data = []
for line in open("run.data").readlines():
  x = int(line.strip())
  data.append(x)

print scipy.mean(data)
print scipy.median(data)
print scipy.std(data)

