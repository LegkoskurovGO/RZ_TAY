import numpy as np
import matplotlib.pyplot as plt

def ACHX(w):
    return 1.2*np.sqrt(1+np.square(8*w))/(w*np.sqrt(1+np.square(4*w))*np.sqrt(1+np.square(10*w))*np.sqrt(1+np.square(20*w)))

def LACHX(w):
    return 20*np.log10(ACHX(w))

def LFCHX(w):
    return (np.arctan(8*w) - np.arctan(4*w) - np.arctan(10*w) - np.arctan(20*w) - np.pi/2)*180/np.pi


w = np.linspace(0.01, 2, 1000)

print('omega средняя')
omega_cp = 0.196539
print(f'ЛАЧХ(w) = {LACHX(omega_cp):.8f}')
print(f'ЛФЧХ(w) = {LFCHX(omega_cp):.8f}')
print(f'gamma = {180 + LFCHX(omega_cp):.8f}')

print('\nomega pi')
omega_pi = 0.09643849406
print(f'ЛАЧХ(w) = {LACHX(omega_pi):.8f}')
print(f'ЛФЧХ(w) = {LFCHX(omega_pi):.8f}')
print(f'АЧХ(w) = {(abc := np.power(10, LACHX(omega_pi)/20)):.8f}')
print(f'beta = {(beta := 1/abc):.8f}')
print(f'Kпред = {1.2*beta:.8f}')

# Delta_дин
print('\nDelta_дин')
print(f'ЛАЧХ(w) = {LACHX(0.1*omega_cp):.8f}')
print(f'АЧХ(w) = {ACHX(0.1*omega_cp):.8f}')
print(f'Delta_дин = {1/ACHX(0.1*omega_cp):.8f}')


# ЛАЧХ и ЛФЧХ
fig = plt.figure(figsize=(14, 8))

ax1 = fig.add_subplot(2,1,1)
ax1.plot(w, LACHX(w), 'r')
ax1.set_xscale('log')
ax1.grid()

ax2 = fig.add_subplot(2,1,2)
ax2.plot(w, LFCHX(w), 'b')
ax2.set_xscale('log')
ax2.grid()

plt.margins(x=0.01, y=0.01)
# plt.savefig('image.png', bbox_inches='tight', pad_inches=0)
plt.show()
