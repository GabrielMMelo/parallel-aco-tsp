with open('./output/chn31_sequential.txt') as f:
    lines = f.readlines()
    chn31_seq = sum([float(i) for i in lines]) / len(lines)

with open('./output/chn31_parallel-8.txt') as f:
    lines = f.readlines()
    chn31_par_8 = sum([float(i) for i in lines]) / len(lines)

print("### chn31 ###")
print("8:", chn31_seq/chn31_par_8)

with open('./output/mu1979_sequential.txt') as f:
    lines = f.readlines()
    mu1979_seq = sum([float(i) for i in lines]) / len(lines)

with open('./output/mu1979_parallel-8.txt') as f:
    lines = f.readlines()
    mu1979_par_8 = sum([float(i) for i in lines]) / len(lines)

with open('./output/mu1979_parallel-4.txt') as f:
    lines = f.readlines()
    mu1979_par_4 = sum([float(i) for i in lines]) / len(lines)

print("### mu1979 ###")
print("8:", mu1979_seq/mu1979_par_8)
print("4:", mu1979_seq/mu1979_par_4)
