from matplotlib import pyplot as plt



# constants in MeV
c_1 = 15.9
c_2 = 18.4
c_3 = 0.71
c_4 = 23.2
c_5 = 11.5

# masses in MeV/c^2
m_h = 938.783
m_n = 939.565

# other constants
c = 3e8
d = 1 # delta is 1 for even-even

# binding energy function
def B(A,Z):
    return c_1*A - c_2*A**(2/3) - c_3*(Z**2)*A**(-1/3) - c_4*((A-2*Z)**2)/A + c_5*d*A**(-1/2)

# mass function
def M(A,Z):
    return Z*m_h + (A-Z)*m_n - B(A,Z)/(c**2)

Z = 26

# seperation energy function
S_n = lambda A, Z: B(A,Z) - B(A-1,Z)
S_p = lambda A, Z: B(A,Z) - B(A-1,Z-1)


A = range(Z, 120, 2) # step size 2 because even-even
S_p = [S_p(a,Z) for a in A]
S_n = [S_n(a,Z) for a in A]

y = [min(S_p, key=lambda l: abs(0-l)), min(S_n, key=lambda l: abs(0-l))]

print(f"Proton drip line: {A[S_p.index(y[0])] - 26}")
print(f"Neutron drip line: {A[S_n.index(y[1])] - 26}")

plt.plot(A, S_p, label="S_p")
plt.plot(A, S_n, label="S_n")
plt.grid(color='gray')

plt.legend()
plt.show()
