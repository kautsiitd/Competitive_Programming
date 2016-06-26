a = map(int, raw_input().split())
print min(a[0]+a[1]+a[2],2*(a[0]+a[1]),2*(a[0]+a[2]),2*(a[2]+a[1]))