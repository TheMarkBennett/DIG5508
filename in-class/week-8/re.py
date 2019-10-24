#%%

import re
txt ="The rain in spain"
x = re.search("a", txt)

print(x)


#%%
zipcode1 = "31245"
zipcode2 ="32124-2432"
zipcode3 ="3214"
zipcode4 ="oue23"

regexpression = "^\d{5}(-\d{4})?$"

print(re.search(regexpression ,zipcode1 ))
print(re.search(regexpression ,zipcode2 ))
print(re.search(regexpression ,zipcode3 ))
print(re.search(regexpression ,zipcode4 ))

#%%
##time of day
time1 = "5pm"
time2 ="12:00p"
time3 ="13:00a"
time4 ="00:02pm"

regexpression = "^\d{5}(-\d{4})?$"

print(re.search(regexpression ,time1 ))
print(re.search(regexpression ,time2 ))
print(re.search(regexpression ,time3 ))
print(re.search(regexpression ,time4 ))



#%%
