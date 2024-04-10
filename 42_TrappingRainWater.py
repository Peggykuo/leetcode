'''Testcases:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

Input: height = [4,2,0,3,2,5]
Output: 9
'''


def trap(height):
    l = 0
    r = len(height) - 1
    lh = height[l]
    rh = height[r]

    res = 0
    while l != r:
        diff = 0
        if height[l] >= height[r]:
            if height[r] > rh:
                rh = height[r]
            else:
                diff = rh - height[r]
            r = r - 1
        else:
            if height[l] > lh:
                lh = height[l]
            else:
                diff = lh - height[l]
            l += 1
        res += diff
    return res


if __name__ == "__main__":
    print(trap([4,2,0,3,2,5]))
