def inversions(perm):
    """
    Compute the set of inversions of the given permutation 'perm'. 
    Inversions are pairs of index i < j such that
    perm[i] > perm[j]. 
    """
    N = len(perm)
    return [(i + 1, j + 1) for i in range(N) for j in range(N) if i < j and perm[i] > perm[j]]

def permutation_sign(perm):
    """
    Compute the sign of the given permutation using
    the size of the inversion set of perm. 
    """
    return (-1)**len(inversions(perm))


def lehmer_code(perm):
    """
    Compute the Lehmer code of the given permutation. 
    The code is defined by 
      Lehmer(perm)[i] := number of index j > i, such that perm[j] < perm[i]. 
    """
    N = len(perm)
    code = [0] * N # initiate array of size N
    for i in range(N):
        for j in range(i + 1, N):
            if perm[j] < perm[i]:
                code[i] += 1
    return code

def inversion_code(perm):
    """
    Compute the inversion code of the given permutation.
    The code is defined by 
      InvCode(perm)[i] := number of integers to the left of i in perm that is greater than i. 
    """
    N = len(perm)
    code = [0] * N
    for i in range(N):
        for j in range(i):
            if perm[j] > perm[i]:
                code[perm[i]] += 1
    return code

