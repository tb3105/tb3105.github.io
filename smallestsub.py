def max_d(str, n): 
    count = [0] * 26
    for i in range(n): 
        count[(ord(str[i])-97)] += 1
      
    max_d_c = 0
    for i in range(26): 
        if (count[i] != 0): 
            max_d_c += 1    
      
    return max_d_c
  
def s_sub_max_d(str): 
  
    n = len(str)
  
    max_dc = max_d(str, n) 
    min_c = n     

    for i in range(n): 
        for j in range(n): 
            sub_s = str[i:j] 
            s_len = len(sub_s) 
            sub_dc = max_d(sub_s,s_len) 
            if (s_len < min_c and max_dc==sub_dc): 
                min_c = s_len
  
    return min_c
    
if __name__ == "__main__": 
      
    str=input()
    k = s_sub_max_d(str); 
    print(k) 