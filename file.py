//this is my code
def mean(arr, ln):
    value = 0
    for i in arr:
        value += i
    mean_value = value / ln
    return mean_value

def variance(arr):
    arr2 = []
    l = len(arr)
    m = mean(arr, l)
    
    for x in arr:
        arr2.append((x - m) ** 2)
    
    # Calculate the variance
    variance_value = sum(arr2) / l  # For population variance
    # variance_value = sum(arr2) / (l - 1)  # For sample variance, uncomment if needed
    return variance_value

a = [5, 2, 1, 3, 4]
print("Variance:", variance(a))

