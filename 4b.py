# 31.10.2023
# Viet Nguyen
# ICT 4b
def main():
    lists=[1,3];
    func_1 = '1. Stop running the program'
    func_2 = '2. Search – a function that will find an element from the list'
    func_3 = '3. Add – a function that adds a new element to the list'
    func_4 = '4. Remove – a function that deletes an element from the list'
    func_5 = '5. Sort – a function that sorts the elements in the list and prints the elements in sorted order'
    func_6 = '6. List – a function that lists all the elements in a list.'
    while True:
        print(f'***********')
        print(f'Current list has {len(lists)} elements: ')
        #print(*lists,sep=' ')
        print()
        print('Let choose function for the current list')
        print(func_1)
        print(func_2)
        print(func_3)
        print(func_4)
        print(func_5)
        print(func_6)
        print()
        a = int(input('What did you choose: '))
        if a == 1:
            print('Program stop')
            break
        elif a == 2:
            sear_no = int(input('Type number you would like to search in list: '))
            i = 0
            while i < len(lists):
                if lists[i] == sear_no:
                    print(f'The number you type {sear_no} in the lists at position {i+1}')
                    break
                i +=1
            else:
                print(f'The number you type {sear_no} not in the lists')
        elif a == 3:
            add_no= int(input('Type number you would like to add in list: '))
            lists.append(add_no)
            print('New List')
            print(*lists,sep=' ')
        elif a == 4:
            rev_no= int(input('Type number you would like to remove in list: '))
            lists.remove(rev_no)
            print(f'New list after removing')
            print(*lists,sep=' ')
        elif a == 5:
            lists.sort()
            print(f'New list after sorting')
            print(*lists,sep=' ')
        ##    maxi = lists[0]
        ##    for i in range(len(lists)-1):
        ##        if lists[i] > maxi:
        ##            maxi = lists[i]
        elif a == 6:
            print(f'Current list')
            print(*lists,sep=' ')
if __name__ == "__main__":
    main()
