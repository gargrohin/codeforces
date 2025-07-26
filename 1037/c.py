def solve():

    n, k = map(int, input().split())
    h = [int(x) for x in input().split()]
    h_i = [(val, idx) for idx, val in enumerate(h)]
    h_i.sort()

    for idx, x in enumerate(h_i):
        if x[1]+1 == k:
            curr = idx
            break
    water = 1
    curr_h = h_i[curr][0]

    max_h = h_i[-1][0]
    max_i = n-1
    for idx, x in enumerate(reversed(h_i)):
        if max_h == x[0]:
            max_i = n - idx - 1
        else:
            break
    
    while curr_h >= water and curr < max_i:

        timetodie = curr_h - water + 1
        next = curr+1

        timetotele = h_i[next][0] - curr_h

        while timetotele <= timetodie and next < max_i:
            timetotele_n = h_i[next + 1][0] - curr_h
            if timetotele_n <= timetodie:
                next = next + 1
                timetotele = timetotele_n
            else:
                break
        
        if timetotele > timetodie:
            return "no"
        
        # tele
        curr_h = h_i[next][0]
        water = water + timetotele
        curr = next

        if curr_h == max_h:
            return "yes"
    
    if curr >= max_i:
        return "yes"
    
    return "no"

def main():
    T= int(input())
    for _ in range(T):
        ans = solve()
        print(ans)

if __name__ == "__main__":
    main()
    
