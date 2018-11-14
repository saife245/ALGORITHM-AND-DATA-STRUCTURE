def KMP(pattern, string): 
    m = len(pattern)
    n = len(string) 
    s = [0]*(n)
    j = 0 

    calc_next(pattern, m, s) 
  
    i = 0 
    while i < n: 
        if pattern[j] == string[i]: 
            i += 1
            j += 1
  
        if j == m: 
            print ("Found at " + str(i-j)) 
            j = s[j-1] 
  
        elif i < n and pattern[j] != string[i]: 
 
            if j != 0: 
                j = s[j-1] 
            else: 
                i += 1
  
def calc_next(pattern, n, s): 
    l = 0
    s[0]
    i = 1
    while i < n: 
        if pattern[i]== pattern[l]: 
            l += 1
            s[i] = l
            i += 1
        else:
            if l != 0: 
                l = s[l-1] 
            else: 
                s[i] = 0
                i += 1
  
string = "banananobano"
pattern = "nano"
KMP(pattern, string) 