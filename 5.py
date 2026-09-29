n=int(input())

is_prime=[True]*(n+1)
is_prime[0]=False
is_prime[1]=False

for i in range(2,n+1):
    if i*i>n:
        break
    if is_prime[i]:
        for j in range(i*i, n+1, i):
            is_prime[j] = False

primes=[]
for i in range(2,n+1):
    if is_prime[i]:
        primes.append(i)

print(primes)
