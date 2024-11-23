def shaker_sort(array): 
    length = len(array) 
    swapped = True
    start_index = 0
    end_index = length - 1
    
    while (swapped == True): 
        
        swapped = False
          
        # ������ ����� �������
        for i in range(start_index, end_index): 
            if (array[i] > array[i + 1]) : 
                # ����� ���������
                array[i], array[i + 1] = array[i + 1], array[i] 
                swapped = True
  
        # ���� �� ���� ������� ��������� ����
        if (not(swapped)): 
            break

        swapped = False

        end_index = end_index - 1
  
        #������ ������ ������
        for i in range(end_index - 1, start_index - 1, -1): 
            if (array[i] > array[i + 1]): 
                # ����� ���������
                array[i], array[i + 1] = array[i + 1], array[i] 
                swapped = True
 
        start_index = start_index + 1

print("shaker sorting")
arr = []
length = int(input("enter the length of the array: ")) 
for i in range(0, length): 
    element = int(input("arr[" + str(i + 1) + "] = "))   
    arr.append(element)
shaker_sort(arr) 
print("sorted array: ") 
print(arr)
