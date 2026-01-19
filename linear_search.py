def linear_search(input_list,target):
    for i in range(len(input_list)):
        if input_list[i]==target:
            return i
    return None

def verify(result):
    if result is not None:
        print("Target found at position: ",result)
    else:
        print("Target value not found")
verify(linear_search([1,2,3,4,5],5))

        