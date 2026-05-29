import numpy as np
from numpy.ma.core import inner


# Controlla il file readme.md per i dettagli su ciascun sub-task

def prodotto_scalare(v1: list, v2: list) -> float:
    v1=np.array(list(map(float, v1)))
    v2=np.array(list(map(float, v2)))
    prodotto_scalare = inner(v1,v2)
    return prodotto_scalare
    pass

def rango_matrice(m: list) -> int:
    m=np.array(m)
    rango_matrice = np.linalg.matrix_rank(m)
    return rango_matrice
    pass

def risolvi_sistema_lineare(A: list, b: list) -> np.ndarray:
    A = np.array(list (A))
    b= np.array(list(b))
    risoluzione_sistema_lineare = np.linalg.solve(A, b)
    return risoluzione_sistema_lineare

    pass

def correlazione_matrici(m1: list, m2: list) -> np.ndarray:
    m1=np.array(m1)
    m2=np.array(m2)
    v1=np.ravel(m1)
    v2=np.ravel(m2)
    correlazione_matrici = np.corrcoef(v1,v2)
    return correlazione_matrici
    pass

def operazioni_elemento_per_elemento(v1: list) -> tuple:
    """Sub-task 5: Restituisce (seno, coseno, arcoseno, arcocoseno) elemento per elemento calcolati sul primo array."""
    pass


def main():
    print("Sub-task 1:", prodotto_scalare([-1, -2], [2,3]))
    print("Sub-task 1:", rango_matrice([[2, 4, 1], [0, 0, 0],[1, 2, 0]]))
    print("Sub-task 3:", risolvi_sistema_lineare([[2, 1], [1, 3]], [5, 7]))
    print("Sub-task 4:", correlazione_matrici([[1, 2], [3, 4]], [[4, 3 ], [2, 1]]))
    print("Sub-task 5:", operazioni_elemento_per_elemento([0, 0.5, 1, -0.5]))

if __name__ == "__main__":
    main()
