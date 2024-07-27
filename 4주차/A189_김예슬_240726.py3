h,m = list(map(int, input().split()))
if m<45 :
    m = m+15
    if h - 1 < 0 :
        h = 23
    else :
        h = h-1
else :
    m = m-45
print(h,m)