# for i in range(3):
#     print(i)

# i=0
# while(i<5):
#         print(i)
#         i=i+1
        # print("done with the loop")

#incremental while loop
# count=1
# while(count > 10):
#          print(count)
# count=count+1

#print numbers from 1 to 100
count=1
while count<=100:
        print(f"print",{count},"=",count)
        count+=1

#print numbers from 100 to 1
print("print numbers from 100 to 1")
count1=100
while count1>=1:
        print(count1)
        count1-=1

#question-3
print("question-3")
nums=[1,4,9,16,25,36,47,54,81,100]
idx=0
while idx<len(nums):
        print(nums[idx])
        idx+=1

#question -5
print("question -5")
nums=[1,4,49,16,25,36,49,64,81,100,49]
x=49
i=0
while i<len(nums):
        if(nums[i]==x):
                print("found at index no.")
        else:
                print("finding..")
        i+=1

