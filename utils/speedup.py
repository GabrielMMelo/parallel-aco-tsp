with open('./output/chn31_sequential.txt') as f:
    lines = f.readlines()
    chn31_seq = sum([float(i) for i in lines]) / len(lines)

with open('./output/chn31_parallel-8.txt') as f:
    lines = f.readlines()
    chn31_par_8 = sum([float(i) for i in lines]) / len(lines)

with open('./output/chn31_parallel-4.txt') as f:
    lines = f.readlines()
    chn31_par_4 = sum([float(i) for i in lines]) / len(lines)

with open('./output/chn31_parallel-2.txt') as f:
    lines = f.readlines()
    chn31_par_2 = sum([float(i) for i in lines]) / len(lines)

print("### chn31 ###")
chn_speedup_8 = chn31_seq/chn31_par_8
print("Speedup (8):", chn_speedup_8)
print("Eficiência (8):", chn_speedup_8/8)
print("e (8):", (1/chn_speedup_8 - 1/8)/(1 - 1/8))
chn_speedup_4 = chn31_seq/chn31_par_4
print("Speedup (4):", chn_speedup_4)
print("Eficiência (4):", chn_speedup_4/4)
print("e (4):", (1/chn_speedup_4 - 1/4)/(1 - 1/4))
chn_speedup_2 = chn31_seq/chn31_par_2
print("Speedup (2):", chn_speedup_2)
print("Eficiência (2):", chn_speedup_2/2)
print("e (2):", (1/chn_speedup_2 - 1/2)/(1 - 1/2))

with open('./output/mu1979_sequential.txt') as f:
    lines = f.readlines()
    mu1979_seq = sum([float(i) for i in lines]) / len(lines)

with open('./output/mu1979_parallel-8.txt') as f:
    lines = f.readlines()
    mu1979_par_8 = sum([float(i) for i in lines]) / len(lines)

with open('./output/mu1979_parallel-4.txt') as f:
    lines = f.readlines()
    mu1979_par_4 = sum([float(i) for i in lines]) / len(lines)

with open('./output/mu1979_parallel-2.txt') as f:
    lines = f.readlines()
    mu1979_par_2 = sum([float(i) for i in lines]) / len(lines)

print("### mu1979 ###")
mu_speedup_8 = mu1979_seq/mu1979_par_8
print("Speedup (8):", mu_speedup_8 )
print("Eficiência (8):", (mu_speedup_8)/8)
print("e (8):", (1/mu_speedup_8 - 1/8)/(1 - 1/8))
mu_speedup_4 = mu1979_seq/mu1979_par_4
print("Speedup (4):", mu_speedup_4)
print("Eficiência (4):", mu_speedup_4/4)
print("e (4):", (1/mu_speedup_4 - 1/4)/(1 - 1/4))
mu_speedup_2 = mu1979_seq/mu1979_par_2
print("Speedup (2):", mu_speedup_2)
print("Eficiência (2):", mu_speedup_2/2)
print("e (2):", (1/mu_speedup_2 - 1/2)/(1 - 1/2))


import matplotlib.pyplot as plt
mu_processors = [2, 4, 8]
mu_speedups = [mu_speedup_2, mu_speedup_4, mu_speedup_8]
plt.bar(mu_processors, mu_speedups, color='red')
plt.xticks(mu_processors)
plt.yticks(mu_speedups)
plt.ylabel('Speedup')
plt.xlabel('Processadores')
plt.title('Speedup para instância mu1979')
plt.show()

chn_processors = [2, 4, 8]
chn_speedups = [chn_speedup_2, chn_speedup_4, chn_speedup_8]
plt.bar(chn_processors, chn_speedups, color='red')
plt.xticks(chn_processors)
plt.yticks(chn_speedups)
plt.ylabel('Speedup')
plt.xlabel('Processadores')
plt.title('Speedup para instância chn31')
plt.show()
