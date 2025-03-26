def find_second_largest_and_second_smallest(arr):
    if len(arr) < 2:
        return None, None  
    
    
    largest = second_largest = arr[0]
    smallest = second_smallest = arr[0]
    
   
    for num in arr:
        
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
        
      
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num
    
    return second_largest, second_smallest
# Example usage:
array = [3, 5, 1, 8, -3, 7, 2]
second_largest, second_smallest = find_second_largest_and_second_smallest(array)
print("Second largest element:", second_largest)
print("Second smallest element:", second_smallest)
