

#reverse a string
# str = "welcome"
# rev_str =""
# for i in range(6,-1,-1):
#     a = str[i]
#     rev_str=rev_str+a
# print(rev_str)

#prime number
# numbers = [7,22,9,4,8,19]
# for i in numbers:
#     for a in range(2,i-1,+1):
#         if i%a==0:
#             print("Number is NOT Prime =",i)
#             break
#         else:
#             print("Number is Prime =", i)
#             break
#

#Largest number from the list
# numbers = [7,22,89,4,8,19]
# print(max(numbers))

#reverse a string with using pre method
# str = "welcome"
# rev=str[::-1]
# print

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
#
# service= Service(executable_path="C:/Drivers/chromedriver-win64")
# driver =webdriver.Chrome(service=service)
#
# driver.get("www,facebook.com")
# driver.implicitly_wait(5)
#
# print(driver.title)


#reverse a string
# str = "welcome"
# rev_str =""
# for i in range(6,-1,-1):
#     #a = str[i]
#     rev_str=rev_str+str[i]
# print(rev_str)

# #remove duplicate from the list
# my_list = [10,20,50,10,60]
# new_list=[]
# for m in my_list:
#     if m not in new_list:
#         new_list.append(m)
# print(new_list)


#find duplicated from the list
# nums = [5, 3, 6, 3, 5, 7, 8, 5]
# my_output=[]
# for n in nums:
#     if nums.count(n)>1 and n not in my_output:
#         my_output.append(n)
# print(my_output)


#count items in the list
# nums = [5, 3, 6, 3, 5, 7, 8, 5]
# my_count=0
# for n in nums:
#     my_count+=1
# print(my_count)

#Find common items in two lists
# nums1 = [1,8,9,10,2]
# nums2 = [2,5,9,3,1]
# nums3=[]
#
# for n in nums1:
#     if n in nums2:
#         nums3.append(n)
# print(nums3)


#Find the maximum and second maximum
# nums = [10, 45, 2, 99, 45, 100,100]
# nums_2=[]
# for num in nums:
#     if num not in nums_2:
#         nums_2.append(num)
# print("First max",max(nums_2))
# nums_2.remove(max(nums_2))
# print("Second max:",max(nums_2))


#Get all even numbers from a list
# nums = [1, 2, 3, 4, 5, 6]
# nums_result=[]
# # Expected: [2, 4, 6]
# for num in nums:
#     if num%2==0:
#         nums_result.append(num)
#
# print("Even Numbers are :",nums_result)

#Sum of digits of a number
# nums = [1, 2, 3, 4, 5, 6]
# sum_result=0
# for num in nums:
#     sum_result=num+sum_result
#
# print("Sum is :",sum_result)



#sum of digits in list
# nums=[9,8,2,1]
# result = 0
# for num in nums:
#     result=num+result
# print("Result:",result)

# FizzBuzz(classic)
# Print numbers from 1 to 20
# If divisible by 3 → print "Fizz"
# If divisible by 5 → print "Buzz"
# If divisible by both → print "FizzBuzz"
# for i in range(1,20,1):
#     if i%3==0 and i%5==0:
#         print(i,"FizzBuzz")
#     elif i%3==0:
#         print(i,"Fizz")
#     elif i%5==0:
#         print(i,"Buzz")

#Find the most frequent character
# text = "aaaabbccc"
# freq={}
# # Expected: "c"
# for i in text:
#     if i in freq:
#         freq[i]+=1
#     else:
#         freq[i]=1
# print(freq)
# print(max(freq,key=freq.get))

#Remove all duplicate characters
# text = "programming"
# text2 =""
# # Expected: "progamin" (first occurrences only)
# for char in text:
#     #print(char)
#     if char not in text2:
#         text2=text2+char
# print(text2)

# # 1. Remove duplicates while preserving order
# nums = [1, 2, 2, 3, 4, 3, 5]
# # Expected: [1, 2, 3, 4, 5]
# result_num=[]
# for num in nums:
#     if num not in result_num:
#         result_num.append(num)
# print(result_num)

# #2. Find elements that appear more than once
# nums = [4, 5, 6, 7, 4, 6, 8, 9, 4]
# # Expected: [4, 6]
# num_result=[]
# for num in nums:
#     if num not in num_result and nums.count(num)>1:
#         num_result.append(num)
# print(num_result)

#3. Find the maximum and second maximum
# nums = [10, 45, 100, 2, 99, 45, 100]
# # Expected: 100 and 99
# nums1=[]
# for num in nums:
#     if num not in nums1:
#         nums1.append(num)
# print(max(nums1))
# nums1.remove(max(nums1))
# print(max(nums1))

# Reverse a list without using [::-1] or reverse()
# str_test ="welcome" #emoclew
# # Option -1
# # rev_str  =""
# # for s in str_test:
# #     rev_str=s+rev_str
# # print(rev_str)
# # Option-2
# # new = str_test[::-1]
# # print(new)
# #Option-3
# new=reverse(str_test)
# print(new)

# #4 Count how many times each number appears
# nums = [1, 2, 1, 3, 2, 1]
# # Expected: {1: 3, 2: 2, 3: 1}
# my_dic ={}
# for num in nums:
#     if num in my_dic:
#        my_dic[num]+=1
#     else:
#        my_dic[num]=1
# print(my_dic)

# 6. Check if a string is a palindrome
# text = "madam"
# rev_str = ""
# # # Expected: True
# for t in text:
#     rev_str=t+rev_str
# print(rev_str)
# if text ==rev_str:
#     print("Word is Palindrome")
# else:
#     print("Word is NOT Palindrome")

# 7. Count vowels and consonants
# text = "hello world"
# # Expected: Vowels = 3, Consonants = 7
# vowel_count1 = 0
# Consonants_count1 = 0
# for t in text:
#     if t.isalpha():
#         if t == 'a' or t =='e' or t =='i' or t =='o' or t =='u':
#             vowel_count1 += 1
#         else:
#             Consonants_count1 += 1
# print("Vowel count= ", vowel_count1)
# print("Consonants count= ", Consonants_count1)

# #even and odd from 1-100
# for i in range(2,101,2):
#     print(i)


#Prime number from the list
my_list = [5,7,6,4,22,11,9]
for m in my_list:
    for r in range(2,m-1,1):
        if m%r==0:
            print("Number is not prime =",m)
            break
        else:
            print("Number is  prime =",m)
            break

