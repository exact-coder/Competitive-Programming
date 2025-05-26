
# https://codeforces.com/problemset/problem/1904/A

test_case = int(input())

while test_case:
    a,b = map(int,input().split(" "))
    xk,yk = map(int,input().split(" "))
    xq,yq = map(int,input().split(" "))
    output =0

    if(a==b):
        dx = [-a,-a,a,a]
        dy = [b,-b,b,-b]

        for i in range(4):
            for j in range(4):
                kpos_kx = xk+dx[i]
                kpos_ky = yk+dy[i]
                kpos_qx = xq+dx[j]
                kpos_qy = yq+dy[j]
                
                if kpos_kx == kpos_qx and kpos_ky == kpos_qy:
                    output+=1
    else:
        dx = [-a,-a,a,a,b,b,-b,-b]
        dy = [b,-b,b,-b,a,-a,a,-a]

        for i in range(8):
            for j in range(8):
                kpos_kx = xk+dx[i]
                kpos_ky = yk+dy[i]
                kpos_qx = xq+dx[j]
                kpos_qy = yq+dy[j]
                
                if kpos_kx == kpos_qx and kpos_ky == kpos_qy:
                    output+=1
    print(output)


    test_case-=1
