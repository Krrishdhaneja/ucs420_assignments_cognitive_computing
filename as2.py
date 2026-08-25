# Assignment 2
# Q1

roll_no = int(input("Enter your 10 digit roll no: "))
extractor = []
for i in range(10):
    extractor.append(roll_no%10 * 10)
    roll_no //= 10
extractor.reverse()
print(extractor)

# Q2
extractor.append(96)
print(extractor)
extractor.insert(1,28)
print(extractor)

# Q3
extractor.remove(96)
print(extractor)
extractor.pop()
print(extractor)

# Q4
extractor.sort()
print(extractor)
extractor.sort(reverse=True)
print(extractor)

# Q5
print(extractor[:3])
print(extractor[-3:])

# Q6
avg = sum(extractor)/len(extractor)
print("Avg is: ", avg)
new_extractor = [x for x in extractor if x > avg]
print(new_extractor)
