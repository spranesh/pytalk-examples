import matplotlib.pyplot
import scipy

t_start = 0.0
t_end = 0.6
sample_rate = 1000.00

t = scipy.r_[t_start:t_end:1/sample_rate]
N = len(t)

s = scipy.sin(179*scipy.pi*t)+scipy.sin(240*scipy.pi*t)
S = scipy.fft(s)

f = sample_rate*scipy.r_[0:(N/2)]/N
n = len(f)

matplotlib.pyplot.grid(True)
matplotlib.pyplot.plot(f,abs(S[0:n])/N)
matplotlib.pyplot.show()
