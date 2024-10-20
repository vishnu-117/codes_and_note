# from string import maketrans
bad_chars = [';', ':', '!', "*"] 
  
# initializing test string  
test_string = "Ge;ek * s:fo ! r;Ge * e*k:s !"
  
# printing original string  
print(test_string)
print(test_string.translate(None,bad_chars))