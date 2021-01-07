print('--------------------')
name = input("Enter your name: ")
print("Welcome", name, "to the binary search algrothim -_-")
print('--------------------')


the_list = [1,3,78,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,49,4,2,8]
the_target = int(input('Please enter a integer your looking for: '))
print('------------------')

def binarySearch(array,searchFor):
    array = sorted(array)
    print('Your list (sorted one): \n',array)
    tail = len(array)
    head = 0

    while tail > head:
        mid = ((head + tail)//2)
        if searchFor == array[mid]:
            print("Found at position: ",mid + 1)
            return mid
        elif searchFor < array[mid]:
            tail = mid
        elif searchFor > array[mid]:
            head = mid + 1

    print("Not found!!!!")


rerun = "y"
while rerun == "y":
    binarySearch(the_list,the_target)    
    rerun = input("Enter y to rerun or any thing else to end: ")
    if rerun == "y":
        print('----------------')
        the_target = int(input('Please enter a integer your looking for: '))
    else:
        break