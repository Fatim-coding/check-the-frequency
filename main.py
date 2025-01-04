# initialize dictionary
test_dict = {'codingal' : 2, 'is' :2, 'best' :2, 'for' :5, 'coding' :1}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# Initialiize value
k = 2

# using loop
# selective key values in dictionary
res = 0
for key in test_dict:
    if test_dict[key]== k:
        res = res + 1

# printing result
print("Frequency of k is : " + str(res))