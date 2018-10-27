import pprint

def longest_common_sub(string1, string2):
    n = len(string1)
    m = len(string2)
    matrix = [[0 for x in range(m+1)] for y in range(n+1)]
    result = [["0" for x in range(m+1)] for y in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if string1[i-1] == string2[j-1]:
                matrix[i][j] = matrix[i-1][j-1] +1
                result[i][j] = "D"
            else:
                if matrix[i-1][j] >= matrix[i][j-1]:
                    matrix[i][j] = matrix[i-1][j]
                    result[i][j] = "U"
                else:
                    matrix[i][j] = matrix[i][j-1]
                    result[i][j] = "L"

    print("The longest common subsequece is:")
    print_path(result,matrix)
    return max(matrix[n])

def print_path(result, matrix):
    ans = []
    i = len(string1)
    j = len(string2)
    while(i>0 and j>0):
        if result[i][j] == "D":
            ans.append(string2[j-1])
            i-=1
            j-=1
        elif result[i][j] == "U":
            i-=1
        elif result[i][j] == "L":
            j-=1
    ans = ans[::-1]
    print(''.join(ans))

string1 = input("Enter string 1: ")
string2 = input("Enter string 2: ")

l = longest_common_sub(string1, string2)
print("Length of LCS is: "+str(l))