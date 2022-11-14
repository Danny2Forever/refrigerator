T = int(input())
count_list = []

def main(T , count_list) :
    for l in range(T):
        N = int(input())
        N2 = input()
        num = ""
        num_list = []
        for i in N2 :
            try :
                type(int(i))
            except :
                num_list.append(int(num))
                num = ""
            finally : 
                num += i
        num_list.append(int(num))
        cal(num_list , count_list)
    
    for n in count_list :
        print(n)

def cal(num_list , count_list) :
    unexpired = True
    count = 0
    while unexpired :
        if 0 not in num_list:
            num_list.sort()
            for j in range(len(num_list)):
                num_list[j] -= 1
            num_list[0] += 1
            count += 1
        else :
            unexpired = False
            count_list.append(count)
            
if __name__ == "__main__" :
    main(T , count_list)