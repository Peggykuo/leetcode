'''
Input: target = 3
Output: 2

Input: target = 6
Output: 5
'''

def racecar(target):
    q = [(0, 1, 0)]

    while q:
        cp, cs, cd = q.pop(0)
        if cp == target:
            return cd
        q.append((cp+cs, cs*2, cd+1))

        if (cp+cs > target and cs > 0) or (cp+cs < target and cs < 0):
            if cs > 0:
                q.append((cp, -1, cd+1))
            else:
                q.append((cp, 1, cd+1))

    return

if __name__ == "__main__":
    print(racecar(3))