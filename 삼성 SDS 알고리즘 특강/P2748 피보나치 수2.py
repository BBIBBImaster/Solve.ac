n = int(input())
def fibo(num):
    fibo_sequence = [0,1]
    for i in range(num):
        next_number = fibo_sequence[-1] + fibo_sequence[-2]
        fibo_sequence.append(next_number)
    return fibo_sequence

result = fibo(n)
print(result[n])