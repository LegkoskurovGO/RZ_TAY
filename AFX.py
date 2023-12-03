import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

def plot_bode(user_input):
    s = sp.symbols('p')
    G = sp.sympify(user_input)
    numerator, denominator = sp.fraction(G)
    num_coeffs = np.array(sp.Poly(numerator, s).all_coeffs(), dtype=float)
    den_coeffs = np.array(sp.Poly(denominator, s).all_coeffs(), dtype=float)
    w = np.logspace( -1.1, 4, 1000)
    # w = np.logspace( -100, 4, 1000)
    s = 1j * w
    G = np.polyval(num_coeffs, s) / np.polyval(den_coeffs, s)
    return G

def graph(G):
    plt.figure(figsize=(8, 6))
    plt.plot(G.real, G.imag)
    plt.xlabel('Re')
    plt.ylabel('Im')
    plt.title('Годограф')
    plt.grid()
    plt.margins(x=0.01, y=0.01)
    plt.savefig('АФХ.png', bbox_inches='tight', pad_inches=0)
    # plt.savefig('АФХ2.png', bbox_inches='tight', pad_inches=0)
    plt.show()

# equation = input("Введи W(p), например: (p + 1) / (p**2 + 3*p + 2): ")
equation = '(1.2*(1+8*p)) / (p*(1+4*p)*(1+10*p)*(1+20*p))'

G = plot_bode(equation)
graph(G)