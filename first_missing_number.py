#remove negatives



def first_missing_number(sorted_nums, test_list):
    original = sorted_nums
    while len(test_list) > 1:

        print(sorted_nums)    
        center = len(sorted_nums) // 2
        
        print(center, sorted_nums[center])
        
        if original.index(sorted_nums[center]) == sorted_nums[center] - 1:
            sorted_nums = sorted_nums[center+1:]
            test_list = test_list[center+1:]
        else:
            sorted_nums = sorted_nums[:center]
            test_list = test_list[:center+1]
            
        print(sorted_nums)
        print(test_list)
     
        print("_________________________________________________")
    
    print(f"First Missing: {test_list[0]}")
sorted_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 25, 26, 27, 28]
test_list = [x for x in range(1, len(sorted_nums)+1)]

first_missing_number(sorted_nums, test_list)

    
