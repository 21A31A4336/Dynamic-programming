value=[200,150,50]
weight=[10,20,30]
capacity=50
def knap(value,weight,capacity,n):
    if n==0 or capacity==0:
        return 0
    if weight[n-1]>capacity:
        knap(value,weight,capacity,n-1)
    else:
        return max(value[n-1]+knap(value,weight,capacity-weight[n-1],n-1),knap(value,weight,capacity,n-1))
n=len(value)
print(knap(value,weight,capacity,n))