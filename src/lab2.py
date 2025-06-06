def min_time_to_paint(K, T, L):
    def can_paint_in_time(max_time):
        painters = 1
        current_sum = 0
        
        for length in L:
            if current_sum + length > max_time:
                painters += 1
                current_sum = length
                if painters > K:
                    return False
            else:
                current_sum += length
        
        return True
    
    left, right = max(L), sum(L)
    
    while left < right:
        mid = (left + right) // 2
        if can_paint_in_time(mid):
            right = mid
        else:
            left = mid + 1
    
    return left * T

if __name__ == "__main__":
    K = 10
    T = 2
    L = [10,20,15,14]
    
    print(min_time_to_paint(K, T, L))
