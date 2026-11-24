a, b, c = map(int, input().split())

shirfarhad_start, shirfarhad_end = map(int, input().split())
saharnaz_start, saharnaz_end = map(int, input().split())
shadooneh_start, shadooneh_end = map(int, input().split())

timeline = [0] * 101

for t in range(shirfarhad_start, shirfarhad_end):
    timeline[t] += 1
    
for t in range(saharnaz_start, saharnaz_end):
    timeline[t] += 1
    
for t in range(shadooneh_start, shadooneh_end):
    timeline[t] += 1
    
total_cost = 0
for count in timeline:
    if count == 1:
        total_cost += 1 * a
    elif count == 2:
        total_cost += 2 * b
    elif count == 3:
        total_cost += 3 * c
        
print(total_cost)