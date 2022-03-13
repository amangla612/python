def count_substring(string, sub_string):
    count_substring=0
    count_substring=string.count(sub_string) 
    return(count_substring)

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
