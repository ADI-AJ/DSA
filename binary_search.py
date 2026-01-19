# def binary_search(input_list,target):
#     input_list.sort()
    
#     first = 0
#     last = len(input_list)-1

#     while first<=last:
#         mid = (first+last)//2

#         if input_list[mid]==target:
#             return (mid)

#         elif input_list[mid]<target:
#             first = mid+1
        
#         else:
#             last = mid-1

#     return None 
       
#print(binary_search([1,5,7,0,3,56,8,9],9))


def recursive_binary_search(input_list,target):
    if len(input_list)==0:
        return False    
    else:
        mid = len(input_list)//2

        if input_list[mid]==target:
            return True
        else:
            if input_list[mid]<target:
                return recursive_binary_search(input_list[mid+1:],target)
            else:
                recursive_binary_search(input_list[:mid],target)

print(recursive_binary_search([1,5,7,0,3,56,8,9],6))   

