def remove_consecutive_sequences(nums):
    i = 0
    while i < len(nums) - 2:
         if nums[i] == nums [i+1] - 1 and nums[i] == nums[i+2] - 2:
          del nums[i:i+3]
    else:
        i+= 1


try: 
    num_count = int(input("Enter the number of integers: "))
    nums = []
    for a in range (num_count):
     num = int(input("Enter an integer: "))
     nums. append (num)

    print ("Original List:", nums) 
    
    remove_consecutive_sequences (nums)

    print("List after removing consecutive sequences of 3 integers:", nums)

except ValueError:
   
    print("Invalid input. Please enter integers.")
    