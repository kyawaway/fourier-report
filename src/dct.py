import numpy as np
import matplotlib.pyplot as plt


def base(N):
    phi_1 = np.array([phi(i,N) for i in range(N)])
    phi_2 = np.zeros((N, N, N, N))
    for i in range(N):
        for j in range(N):
            phi_i, phi_j = np.meshgrid(phi_1[i], phi_1[j])
            phi_2[i, j] = phi_i*phi_j
    return phi_2

def dct(original_data, N):
    return np.sum(base(N).reshape(N*N, N*N)*original_data.reshape(N*N), axis=1).reshape(N, N)

def idct(tranced_data, N):
    return np.sum((tranced_data.reshape(N, N, 1)*base(N).reshape(N,N, N*N)).reshape(N*N, N*N), axis=0).reshape(N, N)


def phi(k, N):
    if k == 0:
        return np.ones(N)/np.sqrt(N)
    else:
        return np.sqrt(2.0/N)*np.cos((k*np.pi/(2*N))*(np.arange(N)*2+1))

