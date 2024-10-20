bad_chars = [';', ':', '!', "*"] 
  
# initializing test string  
test_string = "Ge;ek * s:fo ! r;Ge * e*k:s !"
  
# printing original string  
print(test_string)
test_string = ''.join(i for i in test_string if i not in bad_chars)
print(str(test_string))