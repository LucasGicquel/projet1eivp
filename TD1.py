def is_palindrome(a):
    n=len(a)
    for i in range(n//2):
        if a[i]!=a[n-i-1]:
            return False
    return True



def bubbleSort(liste_a_trier):
    n=len(liste_a_trier)
    for i in range(n):
        for k in range(n-i-1):
            if liste_a_trier[k]>liste_a_trier[k+1]:
                liste_a_trier[k],liste_a_trier[k+1]=liste_a_trier[k+1],liste_a_trier[k]
    return(liste_a_trier)

          
def insertionSort(liste_a_trier):
    n=len(liste_a_trier)
    for i  in range(1,n):
        x=liste_a_trier[i]
        j=i
        while x<liste_a_trier[j-1] and j>0:
            liste_a_trier[j],liste_a_trier[j-1]=liste_a_trier[j-1],liste_a_trier[j]
            j-=1
    return(liste_a_trier)


def partition(arr,low,high):
    j=low
    x=arr[low]
    for i in range(low+1,high):
        if arr[i]<x:
            j+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[high],arr[j]=arr[j],arr[high]
    return(j)    

def quickSort(arr,low,high):
    if arr[low]<arr[high]:
        p=partition(arr,low,high)
        quickSort(arr,low,p)
        quickSort(arr,p+1,high)


Installer GUITH

