def z_func(s):
    n = len(s)
    z = [0]*n
    l = 0
    for i in range(1, n):
        k = min(z[i - l], l + z[l] - i)
        if (k < 0):
            k = z[i - l]
        z[i] = k
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] > l + z[l]:
            l = i
    return z
