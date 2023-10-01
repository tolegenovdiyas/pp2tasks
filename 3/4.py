a=input().split()
for i in range(1, len(a),+1):
    if (int(a[i])>0 and int(a[i-1])>0) or (int(a[i])<0 and int(a[i-1])<0):
        print(a[i-1]+' '+a[i])
        break