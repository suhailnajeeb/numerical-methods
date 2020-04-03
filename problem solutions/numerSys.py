#------------Settings---------------

target = 'smallest positive'

bits = 9
exponent_bits = 4
mantissa_bits = 4

#----------Helpers------------------

def eval_mantissa(mantissa):
    value = 0
    for i, m in enumerate(mantissa):
        value = value + 2**(-(i+1))*m
    return value

def eval_exponent(exponent):
    value = 0
    for i, e in reversed(list(enumerate(exponent))):
        value = value + 2**(i)*e
    return value

def extract_number(number, exponent_bits):
    sign_bit = number[0]
    exponent_sign = number[1]
    exponent = number[2 : 2 + exponent_bits - 1]
    mantissa = number[2 + exponent_bits - 1:]
    return sign_bit, exponent_sign, exponent, mantissa

def eval_number(sign_bit, exponent_sign, exponent, mantissa):
    mantissa_value = eval_mantissa(mantissa)
    exponent_value = eval_exponent(exponent)

    if(exponent_sign == 1):
        exponent_value = exponent_value*(-1)

    value = mantissa_value*(2**exponent_value)

    if(sign_bit == 1):
        value = value*(-1)
    return value

# ----------- Setup ---------------------

if(target == 'smallest positive'): 
    sign_bit = 0
    mode = 'min'
if(target == 'smallest negative'):
    sign_bit = 1
    mode = 'max'
if(target == 'largest positive'):
    sign_bit = 0
    mode = 'max'
if(target == 'largest negative'):
    sign_bit = 1
    mode = 'min'

# --------- production --------------------

exponent = [1 for i in range(exponent_bits - 1)]

if(mode == 'min'):
    exponent_sign = 1
    mantissa = [1] + [0 for i in range(mantissa_bits -1)]
if(mode == 'max'):
    exponent_sign = 0
    mantissa = [1 for i in range(mantissa_bits)]    

number = [sign_bit] + [exponent_sign] + exponent + mantissa
value = eval_number(sign_bit, exponent_sign, exponent, mantissa)

print('The ' + target + ' number for the given number system: ')
print(number)
print('Value of the number: ' + str(value))