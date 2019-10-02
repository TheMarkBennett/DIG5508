#%%
def to_f(c):
    if c < -273.15:
        raise ValueError("Temperature value is below absolute zero.")
    return ((9/5) * c) + 32
    

def to_c(f):
    if f < -459.67:
        raise ValueError("Temperature value is below absolute zero.")
    return (5/9) * (f-32)

#%%
def sign(num):
    answer = '?'
    if num > 0:
        answer = '+'
    if num < 0:
         answer = '-'
    if num == 0:
        answer = ''
    return answer

#%%
def sign(num):
    answer = '?'
    if num > 0:
        answer = '+'
    elif num < 0:
         answer = '-'
    else:
        answer = ''
    return answer


#%%
def gender(name):
    indicated = '?'
    if name[-1] == 'a':
        indicated = 'female'
    if name[-1] == 'o':
        indicated = 'male'
    return indicated

#%%
