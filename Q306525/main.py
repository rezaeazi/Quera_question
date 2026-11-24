import sys
from collections import defaultdict

def solve():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
    
    n = int(input_data[0].strip())
    
    scores = defaultdict(float)
    
    line_idx = 1
    for _ in range(n):
        if line_idx >= len(input_data):
            break
            
        s_p_line = input_data[line_idx].strip()
        if not s_p_line:
            line_idx += 1
            continue
            
        S, P = map(int, s_p_line.split())
        line_idx += 1
        
        if P == 0:
            line_idx += 1
            continue
            
        participants = input_data[line_idx].strip().split(',')
        line_idx += 1
        
        for idx, username in enumerate(participants):
            R = idx + 1
            
            if P == 1:
                score = float(S)
            else:
                score = S * (P - R) / (P - 1)
                
            scores[username] += score

    sorted_participants = sorted(scores.items(), key=lambda item: item[1], reverse=True)
    
    for username, score in sorted_participants:
        print(username)

if __name__ == '__main__':
    solve()