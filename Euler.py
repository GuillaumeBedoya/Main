# -*- coding: utf-8 -*-
def clearall():
  all = [var for var in globals() if var[0] != "_"]
  for var in all:
    del globals()[var]
    
#%%
# Problem 1: Find the sum of all the multiples of 3 or 5 below 1000
#x = 1000
#s = 0
#for i in range(1, x):
#    if i%3 == 0 or i%5 == 0: s += i
#print(s)

#better:
m = 1000
a = sum([x for x in range(m) if x%3 == 0 or x%5 == 0])
print('pbm1:', a)
#%%
# Problem 2: Find the sum of the even-valued terms of the Fibonacci sequence
x = 4000000
s = 0
a, b, c = 1, 1, 2
while c <= x:
  c = a + b
  if c%2 == 0:
    s += c
  a, b = b, c
print('pbm2:', s)
#%%
# Problem 3: What is the largest prime factor of the number 600851475143
from math import sqrt
def Problem3(number):

  isprime = True
  for i in range(2, 1 + int(sqrt(number))):
    if number%i == 0:
      isprime = False
      break

  if isprime:
    return number
  else:
    primes = []
    for i in range(2, 1 + int(number/2)):
      isprime = True
      for j in range(i - 1, 1, -1):
        if i%j == 0:
          isprime = False
          break
      if isprime:
        primes.append(i)
    primes.reverse()
    for p in primes:
      if number%p == 0:
        return p

a = Problem3(13) #600851475143
print('pbm3:', a)
#%%
#better:
import time
start = time.time()

def isprime(x):
	if x == 2: return True
	if x < 2 or x%2 == 0: return False
	for i in range(3, int(x**.5) + 1, 2):
		if x%i == 0: return False
	return True

number = 13195
primes = [i for i in range(number + 1) if isprime(i)]

def factors(n):
	return sorted({i for i in primes if n%i == 0})

print(max(factors(600851475143)))
	
print('execution time:', round(time.time() - start, 5))
#%%
#better:
import time
start = time.time()

prim = 600851475143
i = 2

while prim > 1:
    if prim % i == 0:
        prim = prim / i
    i += 1
print(i - 1)

print('execution time:', round(time.time() - start, 5))

#%%
# Problem 4: Find the largest palindrome made from the product of two 3-digit numbers
#def Problem4(nbDigits):
#  for i in range(10 ** nbDigits - 1, 10 ** (nbDigits - 1) - 1, -1):
#    for j in range(i, 10 ** (nbDigits - 1) - 1, -1):
#      isPalindrome = True
#      a = str(i * j)
#      b = len(a)
#      for n in range(1, b + 1):
#        if a[n - 1] != a[b - n]:
#          isPalindrome = False
#          break
#      if isPalindrome:
#        return '{} x {} = {}'.format(i, j, i*j)
#
#a = Problem4(3)
#print('pbm4:', a)

#better:
import time
start = time.time()

def palindrome(n):
    pa=[]
    for x in range(1,n):
    	for y in range(1,n):
            prod=x*y
            if str(prod)==str(prod)[::-1]:
                pa.append(prod)
    return max(pa)

print(palindrome(1000))

print('execution time:', round(time.time() - start, 5))

#better:
import time
start = time.time()

def Problem4(nbDigits):
  pal = []
  for i in range(10 ** nbDigits - 1, 10 ** (nbDigits - 1) - 1, -1):
    for j in range(i, 10 ** (nbDigits - 1) - 1, -1):
      isPalindrome = True
      a = str(i * j)
      b = len(a)
      for n in range(1, b + 1):
        if a[n - 1] != a[b - n]:
          isPalindrome = False
          break
      if isPalindrome:
      	pal.append(i*j)
  return max(pal)

print('pbm4:', Problem4(3))

print('execution time:', round(time.time() - start, 5))

#%%
# Problem 5: What is the smallest number that is evenly divisible by all of the numbers from 1 to 20
n = 20
r = 1
for k in range(1, n + 1):
  if r % k > 0:
    for j in range(1, n + 1):
      if (r*j) % k == 0:
        r *= j
        break
print('pbm5:', r)
#%%
# Problem 6: Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
number = 100
SqS = (sum(j for j in range(number + 1))) ** 2
sSq = sum(j ** 2 for j in range(number + 1))
print('pbm6:', SqS - sSq)
#%%
# Problem 7: What is the 10001st prime number?
#number = 3
#prime = 2
#cnt = 1
#p = 0
#while p <= (number - 1):
#  isprime = True
#  cnt += 1
#  for j in range(cnt - 1, 1, -1):
#    if cnt % j == 0:
#      isprime = False
#      break
#  if isprime:
#    prime = cnt
#    p += 1
#print('pbm7:', prime)

#better:
import time
start = time.time()

def isprime(n):
  if n == 2: return True
  if n < 2 or n%2 == 0: return False
  for j in range(3, int(n**.5) + 1, 2):
    if n%j == 0: return False
  return True

primes = [i for i in range(111000) if isprime(i)]
print('pbm7:', primes[10000])

print('execution time:', round(time.time() - start, 5))

#%%
# Problem 8: Find the 13 adjacent digits that have the greatest product. 
nDigits = 13

myString = '73167176531330624919225119674426574742355349194934\
96983520312774506326239578318016984801869478851843\
85861560789112949495459501737958331952853208805511\
12540698747158523863050715693290963295227443043557\
66896648950445244523161731856403098711121722383113\
62229893423380308135336276614282806444486645238749\
30358907296290491560440772390713810515859307960866\
70172427121883998797908792274921901699720888093776\
65727333001053367881220235421809751254540594752243\
52584907711670556013604839586446706324415722155397\
53697817977846174064955149290862569321978468622482\
83972241375657056057490261407972968652414535100474\
82166370484403199890008895243450658541227588666881\
16427171479924442928230863465674813919123162824586\
17866458359124566529476545682848912883142607690042\
24219022671055626321111109370544217506941658960408\
07198403850962455444362981230987879927244284909188\
84580156166097919133875499200524063689912560717606\
05886116467109405077541002256983155200055935729725\
71636269561882670428252483600823257530420752963450'

iMax = 1
for pos in range(len(myString) - nDigits + 1):
  prod = 1
  for adj in range(pos, pos + nDigits):
    prod *= int(myString[adj])
  if prod > iMax:
    iMax = prod
    iPos = myString[pos:pos + nDigits]
print('pbm8: {} - {}'.format(iPos, iMax))
#%%
# Problem 9: There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

import time
start = time.time()

a = b = c = 0
SUM = 1000

while a + b + c != SUM and a <= SUM:
    a += 1
    b,c = 0,0
    while a + b + c != SUM and b <= SUM:
        b += 1
        c = (a**2 + b**2)**0.5
        if a + b + c == SUM:
            print('a = {}, b = {}, c = {}, abc = {}'.format(int(a),int(b),int(c), int(a*b*c)))
            
print('execution time:', round(time.time() - start, 5))

#%%
#better:
start = time.time()
def findSpecialPythagoreanTriplet():
  for b in range(0, 1001):
    for c in range(0, 1001):
      calc = (1000 - b - c)**2 + b**2 - c**2
      if calc == 0:
        a = 1000 - b - c
        if a**2 + b**2 == c**2 and c > b and b > a:
          return (a * b * c)

print(findSpecialPythagoreanTriplet())
print('execution time:', round(time.time() - start, 5))

#%%
# Problem 10: Find the sum of all the primes below two million.

import time
start = time.time()

def isprime(n):
  if n == 2: return True
  if n < 2 or n%2 == 0: return False
  for p in range(3, int(n**.5) + 1, 2):
    if n%p == 0: return False
  return True

s, number = 0, 2000000
for i in range(number):
  if isprime(i):
    s += i
print(s)
#print('pbm10:', sum([i for i in range(number) if isprime(i)]))
#1179908154 doesn't work
#142913828922


print('execution time:', round(time.time() - start, 5))
#%%
# Problem 11: What is the greatest product of four adjacent numbers in the same direction in the 20×20 grid?
#%%
# Problem 12: What is the value of the first triangle number to have over five hundred divisors
#ndivmax = 5
#cpt = ndiv = maxndiv = 0
#while ndiv < ndivmax:
#  cpt += 1
#  ndiv = 0
#  r = sum(j for j in range(cpt + 1))
#  for j in range(1, r + 1):
#    if r%j == 0:
#      ndiv += 1
#      if ndiv > maxndiv:
#        maxndiv = ndiv
#        result = r
#print('pbm12: n =', r, '({} diviseurs)'.format(ndiv))

#better:
import time
start = time.time()

def divisors(n):
  d = 2
  for i in range(2, n//2 + 1):
    if n%i == 0:
      d += 1
  return d

triangle = 1
c = 1
div = 0
while div < 100:
  c += 1
  triangle += c
  div = divisors(triangle)

print('{} has {} divisors'.format(triangle, div))

print('execution time:', round(time.time() - start, 5))
#%%
# Problem 13: Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
import time
start = time.time()

with open('p013.txt', 'r') as myfile:
  numbers = myfile.read()

print(str(sum([int(i) for i in numbers.split('\n')]))[:10])
print('execution time:', round(time.time() - start, 5))
#%%
# Problem 14: Which starting number, under one million, produces the longest chain?
#maxchain, res = 1, 2
#for n in range(2, 100):
#  #c=[]
#  i, chain = n, 0
#  while i >= 1:
#    #c.append(i)
#    chain += 1
#    if i == 1:
#      if chain > maxchain:
#         res, maxchain = n, chain
#      break
#    elif i%2 == 0:
#      i /= 2
#    else:
#      i = 3 * i + 1
#print('pbm14: number =', res, 'avec une chaine de', maxchain)
##print(c)

#better:

import time
#m = 1
#dit = {1: 1}  # save length of chains for occurring numbers {number: length}
#
#def calc_chain(n, count, state):
#    if n in dit:  # if n is the key number in dictionary
#        return count+dit[n]
#    if n % 2 == 0:  # n is even
#        count = calc_chain(n/2, count, state)
#    else:  # n is odd
#        count = calc_chain(n*3+1, count, state)
#    if state:
#        state = False
#        dit[n] = calc_chain(n, 0, state)
#    return count+1
#
#max_p = 0
#start = time.time()
#while m <= 1000000:
#    a = calc_chain(m, 0, True)
#    if a > max_p:
#        max_p = a
#        p = m
#    m += 1
#print("number:%d, length:%d" % (p, max_p))
#print("%ds" % int(time.time() - start))

#better:
start = time.time()
class Collatz:
  def __init__(self):
    self.memory = {}

  def count(self, n):
    if n in self.memory:
      return self.memory[n]
    if n == 1:
      return 1
    if (n % 2) == 0:
      new_count = self.count(n / 2) + 1
      self.memory[n] = new_count
      return new_count
    else:
      new_count = self.count((3 * n) + 1) + 1
      self.memory[n] = new_count
      return new_count

maximum, maxcount = -1, -1
collatz = Collatz()
for i in range(1, 1000000):
  count = collatz.count(i)
  if count > maxcount:
    maximum = i
    maxcount = count

print('pbm14: number:{}, Count:{}'.format(maximum, maxcount))
print('execution time:', round(time.time() - start, 3))
#%%
# Problem 15: How many such routes are there through a 20×20 grid?
#%%
# Problem 16: What is the sum of the digits of the number 2^1000?
#number = 2**1000
#from math import ceil, log
#def frac(x):
#  return (x - int(x))
#
#ndigits = ceil(log(number, 10))
#n, s = number, 0
#for i in range(1, ndigits + 1):
#  s += 10 * frac(n/10)
#  n = int(n / 10)
#print('pbm16: sum =', int(s))

#better:

s = sum([int(x) for x in str(2**1000)])
#s = sum(map(int,[str(2**1000)]))
print('pbm16: sum =', s)
#%%
# Problem 17: If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
#%%
# Problem 18: Find the maximum total from top to bottom of the triangle
import time
start = time.time()

#ss = '\
#75 \
#95 64 \
#17 47 82 \
#18 35 87 10 \
#20 04 82 47 65 \
#19 01 23 75 03 34 \
#88 02 77 73 07 63 67 \
#99 65 04 28 06 16 70 92 \
#41 41 26 56 83 40 80 70 33 \
#41 48 72 33 47 32 37 16 94 29 \
#53 71 44 65 25 43 91 52 97 51 14 \
#70 11 33 28 77 73 17 78 39 68 17 57 \
#91 71 52 38 17 14 91 43 58 50 27 29 48 \
#63 66 04 68 89 53 67 30 73 16 69 87 40 31 \
#04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'
#
#l = [int(i) for i in ss.split(' ')]
#
#lines = []
#d = 0
#for j in range(16):
#	lines.extend([l[:d]])
#	for i in range(d):
#		l.pop(0)
#	d += 1
#lines.pop(0)
#
#smax = []
#for n in range(0, 2**(len(lines) - 1)):
#  s = [75]
#  
#  b = bin(n)[2:]
#  while len(b) < len(lines) - 1:
#    b = '0' + b
#
#  s.append( lines[1][int(b[0])] )
#  for line in range(2, len(lines)):
#    s.append( lines[line][sum([int(i) for i in b[:line]])] )
#
#  if sum(s) > sum(smax): smax = s
#
#print('pbm18: path = {}\nand the sum is {}'.format(smax, sum(smax)))
#print('execution time:', round(time.time() - start, 3))
#
#
##better:
#def findMaxPathSum():
#  arr = []
#  numbers = list(map(int, ss.split()))
#  arr.append(numbers)
#  
#  for i in range(len(arr) - 2, -1, -1):
#    for j in range(0, len(arr[i]), 1):
#      arr[i][j] += max(arr[i + 1][j], arr[i + 1][j + 1])
#      # print("{0},{1}: ".format(i, j) + str(arr[i][j]))
#
#  return arr[0][0]


#better:
with open('p018.txt','r') as f:
  t = f.read().split("\n")

for l in range(len(t)):
  t[l] = t[l].split(" ")

def findMax(y,x):
  if y == len(t) - 1:
    return int(t[y][x])
  else:
    return int(t[y][x]) + max(findMax(y+1,x),findMax(y+1,x+1))

print(findMax(0,0))
print('execution time:', round(time.time() - start, 3))

#%%
# Problem 19: How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
d, c = 0, 0
for yr in range(1900, 2001):
  leap = 29 if yr % 400 == 0 or (yr % 4 == 0 and yr % 100 != 0) else 28
  dic = {1:31, 2:leap, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
  
  for month in dic.keys():
    for day in range(1, 1 + dic[month]):
      d += 1
      if d%7 == 0 and day == 1 and yr > 1900:
        c += 1

print('pbm19: number of sundays:', c)  

#better:
#import datetime; print([1 for y in range(1901, 2001) for m in range(1, 13) if datetime.datetime(y, m, 1).weekday() == 1].__len__())
#%%
# Problem 20: Find the sum of the digits in the number 100!
def fact(x):
  if x <= 1:
    return 1
  else:
    return x * fact(x-1)

s = sum([int(x) for x in str(fact(100))])
#s = sum(map(int,[str(2**1000)]))
print('pbm20: sum =', s)
#%%
# Problem 21: Evaluate the sum of all the amicable numbers under 10000
def divisors(n):
  div = [i for i in range(1, n) if n%i == 0]
  return sum(div)

s = 0
for i in range(2, 1001):
  if i == divisors(divisors(i)) and i != divisors(i):
    s += i + divisors(i)
    #print(i, divisors(i))
print('pbm21: sum =', int(s/2))
#%%
# Problem 22: What is the total of all the name scores in the file?
#start = time.time()
#import os
#os.getcwd()
#
#alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', \
#'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#
#with open('p022_names.txt', 'r') as myfile:
#  names = myfile.read()
#names = names.split(',')
#names = [n.lower() for n in names]
#names.sort()
#
#s = 0
#for name in names:
#  v = 0
#  for l in name:
#    v += 1 + alphabet.index(l)
#  s += v * (1 + names.index(name))
#
#print('pbm22: total =', s)
#print('execution time:', round(time.time() - start, 5))

#better:
#with open('p022_names.txt') as f:
#    names = sorted([s[1:-1] for s in f.read().split(',')])
#    print(sum([(i+1)*sum(map(lambda x:x-64,map(ord,word))) for i,word in enumerate(names)]))

#better:
start = time.time()
print('pbm22:', sum((i+1) * sum(ord(l) - 64 for l in e) for i, e in enumerate(sorted([n[1:-1] for n in open('p022_names.txt').read().split(',')]))))
print('execution time:', round(time.time() - start, 5))
#%%
# Problem 23: Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
def divisors(n):
  div = []
  for i in range(1, 2 + int(n/2)):
    if n % i == 0:
      div.append(i)
  return sum(div)
 
n = 10 #28123

abundant = []
for i in range(1, n + 1):
  if divisors(i) > i:
    abundant.append(i)
#print(abundant)

notake = []
for i in abundant:
  for j in abundant:
    notake.append(i + j)
  notakeSet = set(notake)
  notake = list(notakeSet)
  del notakeSet
  notake.sort()
#print(notake)
#print(sum(i for i in notake if i< n))
del abundant

s = n * (n + 1) / 2 - sum(i for i in notake if i <= n)
print('pbm23: sum =', s)

#better:
abun = []
for num in range(1, 28): #28123
    each = 1
    for i in range(2, round(num**0.5)+1):
        if num % i == 0:
            if num/i != i:
                each += (num/i)+i
            else:
                each += i
    if each > num:
        abun.append(num)
sums = []
for each in range(0, len(abun)):
    for k in range(each, len(abun)):
        sums.append(abun[each]+abun[k])
every = []
for i in range(1, 28):#28123
    every.append(i)
filtered = list(set(every)-set(sums))
print('pbm23: sum =',sum(filtered))

#better:
#up = 28 #28123
#isabundant = lambda num:sum(filter(lambda x:num%x==0,range(1,num/2+1)))>num
#set1=set(range(1,up+1))
#numbers=filter(lambda x:isabundant(x),range(1,up+1))
##numbers = [x for x in range(1, up + 1) if isabundant(x)]
#set2=set(filter(lambda x:x<up+1,(i+j for i in numbers for j in numbers)))
##set2 = set([i + j for i in numbers for j in numbers if i + j < up + 1])
#print(sum(set1-set2))


#%%
# Problem 24: What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
from itertools import permutations as per
#figures = '0123456789'
#a = [''.join(i) for i in p(figures, len(figures))]
#print(a[1000000 - 1])

#better:
start = time.time()
print('pbm24:', ''.join(map(str,list(per(range(10)))[999999])))
print('execution time:', round(time.time() - start, 5))
#%%
# Problem 25: What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
#from math import log10
#f = [1, 1,]
#i, n = 1, 0
#while n < 1000:
#  i += 1
#  f.append(f[i - 1] + f[i - 2])
#  n = 1 + int(log10(f[-1]))
#print(i + 1)

#better:
fibo = [1,1]
while len(str(fibo[-1])) < 1000:
  fibo.append(fibo[-1] + fibo[-2])
print('pbm25:', len(fibo))
#%%
# Problem 26: Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
#start = time.time()
#Max = 1000
#pmax, res = 1, 1
#per = [0] * (Max + 1)
#for number in range(2, 1 + Max):
#  for period in range(Max, 0, -1):
#    if (10**period - 1) % number == 0:
#      per[number] = period
#  if per[number] > pmax:
#    res, pmax = number, per[number]
#print('pbm26: max period =', pmax, 'for', res)
#print('execution time:', round(time.time() - start, 5))

#better:
start = time.time()
def findper(n):
  e = 1
  while 10**e % n != 1:
    e += 1
  return e

maxper = res = 0
for i in range(2, 1001):
  if i%2 != 0 and i%5 != 0:
    per = findper(i)
    if per > maxper:
      res = i
      maxper = per
print('pbm26: max period =', maxper, 'for', res)
print('execution time:', round(time.time() - start, 5))
#%%
# Problem 27: Find the product of the coefficients, a and b, for the quadratic expression
#that produces the maximum number of primes for consecutive values of n
start = time.time()
def isprime(n):
  n = abs(n)
  if n < 2: return False
  for i in range(2, 1 + int(sqrt(n))):
    if n%i == 0: return False
  return True

limit = 10
maxprimes = 0
for a in range(-limit - 1, limit + 1, 2): #a must be odd
  for b in range(2, limit + 1):
    number = 0
    while isprime(number**2 + a * number + b):
      number += 1
      if number > maxprimes: maxprimes, amax, bmax = number, a, b
print('pbm27: primes =', maxprimes, 'a={}, b={}'.format(amax, bmax))
print('execution time:', round(time.time() - start, 5))
#%%
# Problem 28: What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
start = time.time()
s, n, inc = 0, 1, 2
while inc + 1 <= 11:
    if n % inc == 1: s += n
    if n**0.5 % 2 == 1 and n != 1: inc += 2
    n += 1
print('pbm28: sum =', s)
print('execution time:', round(time.time() - start, 5))

#better:
#print(sum([x**2*4-6*(x-1) for x in range(3,1002,2)]) + 1)

#better:
print(sum([n**2-m*(n-1) for n in range(1,1002,2) for m in range(4)][3:]))
#%%
# Problem 29: How many distinct terms are in the sequence generated by a^b for 2 ≤ a ≤ 100 and 2 ≤ b ≤ 100?
#start = time.time()
#s = set()
#for a in range(2, 101):
#  for b in range(2, 101):
#    s.add(a**b)    
#print('pbm29:', len(s), 'distinct elements')
#print('execution time:', round(time.time() - start, 5))

#better:
start = time.time()
print('pbm29:', len({i**j for i in range(2,101) for j in range(2,101)}))
print('execution time:', round(time.time() - start, 5))
#%%
# Problem 30: Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
#from math import log10
#start = time.time()
#s = []
#def sumdigits(n, i):
#  #l = 1 + int(log10(n))
#  s = 0
#  for j in str(n):
#    s += int(j)**i    
#  return s
#  
#for number in range(2, 6*9**5):
#  if sumdigits(number, 5) == number:
#    s.append(number)
#    
#print('pbm30: sum =', sum(s))
#print('execution time:', round(time.time() - start, 5))

#better:
#sum5 = 0
#for i in range(2,6*9**5):
#    s = sum([int(x)**5 for x in str(i)])
#    if s == i:
#        sum5+=s
#print(sum5)

#better:
start = time.time()
#print('pbm30: sum =', sum(nb for nb in range(2, 6*9**5) if nb == sum(digit**5 for digit in map(int,str(nb)))))
print('execution time:', round(time.time() - start, 5))
#%%
# Problem 31: How many different ways can £2 be made using any number of coins?
#start = time.time()
#coins = [2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01,]
#coeffmax = [int(2/k) for k in coins]
#combi = 0
#
#def f31(coeffs):
#  return sum([coeffs[i] * coins[i] for i in range(8)])
#
#for n0_01 in range(0, 201):
#  for n0_02 in range(0, 101):
#    for n0_05 in range(0, 41):
#      for n0_1 in range(0, 21):
#        for n0_2 in range(0, 11):
#          for n0_5 in range(0, 5):
#            for n1 in range(0, 3):
#              for n2 in range(0, 2):
#                n = coinscoeffs([n2, n1, n0_5, n0_2, n0_1, n0_05, n0_02, n0_01])
#                if n > 2:
#                  break
#                if n == 2:
#                  combi += 1
#                  break
#
#print('pbm31: ', combi, 'ways')

#for c in range(8):
#  n = 0
#  prov = []
#  for j in range(coeffmax[c] + 1):
#    prov.append(j)
#    n = 2 * prov[0] + 1 * prov[1] + 0.5 * prov[2] + 0.2 * prov[3] + 0.1 * prov[4] + 0.05 * prov[5] + 0.02 * prov[6] + 0.01 * prov[7]
#  if f31(prov) == 2:
#    combi += 1
#  print(combi)
#  
#  
##n = [sum(i * coins[j]) for j in range(8) for i in range(int(coeffs[j]) + 1)]
#print('pbm31: sum =', combi)
#
#print('execution time:', round(time.time() - start, 5))
#sum(nb for nb in range(100000) if coeff[i] * coins[j] for j in range(0, 201) if sum(coeff[i] * coins[i] for i in range(8)) == 2)
import time; start = time.time()

ways = [0]*201
ways[0] = 1
for x in [1,2,5,10,20,50,100,200]:
    for i in range(x, 201):
        ways[i] += ways[i-x]
print(ways[200])

print('execution time:', round(time.time() - start, 5))

#%%
# Problem 32: Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
#start = time.time()
#def aDD(a, s):
#  for i in str(a):
#    s.add(int(i))
#
#ss = {i for i in range(1, 10)}
#p = set()
#for a in range(1, 9877):
#  for b in range(1, 9877):
#    if len(str(a)) + len(str(b)) + len(str(a * b)) > len(ss):
#      break
#    s = set()
#    for i in [a, b, a*b]: aDD(i, s)
#    if s == ss and (a*b) not in p:
#      p.add(a*b)
#      #print('a=',a,'b=',b, 'ab=',a*b)
#print('pbm32: sum =', sum(p))
#print('execution time:', round(time.time() - start, 5))

#better:
start = time.time()
r = []
ss = {i for i in range(1, 10)}
for i in range(2,5000):
  for j in range(3,99):
    s = str(i)+str(j)+str(i*j)
    if len(s) == 9:
      if  {str(x) for x in s} == {str(x) for x in ss} and i*j not in r:
        r += [i*j]
print('pbm32: sum =', sum(r))
print('execution time:', round(time.time() - start, 5))
#%%
# Problem 33: If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
from math import gcd
c = []
for a in range(10, 100):
 for b in range(a + 1, 100):
  if b % 10 != 0:
   if int(str(a)[1]) == int(b/10) and int(a/10) / int(str(b)[1]) == a/b:
    c.append('{}/{}'.format(a, b))
n = d = 1
for i in c:
 n *= int(i[0:2])
 d *= int(i[3:5])
g = gcd(n, d)
print('pbm33: {}/{}'.format(int(n/g), int(d/g)))
#%%
# Problem 34: Find the sum of all numbers which are equal to the sum of the factorial of their digits.
clearall()
def fact(n):
  if n <= 1: return 1
  return n * fact(n-1)
l = 100 #to change
a = sum([number for number in range(10, l + 1) if number == sum([fact(int(d)) for d in str(number)])])
print('pbm34:', a)
#%%
# Problem 35: How many circular primes are there below one million?
import time
start = time.time()

l = 1000000
circ = [2, 3, 5, 7,]

def isprime(n):
  if n == 2: return True
  if n < 2 or n%2 == 0: return False
  for i in range(3, int(n**.5) + 1,2):
    if n%i == 0: return False
  return True

for n in range(11, l + 1, 2):
  ADD = True
  if any([s not in '1379' for s in str(n)]) or not isprime(n): continue
  L = len(str(n))
  for i in range(L):
    nn = ''
    for j in range(L):
      nn += str(n)[ (j + i) % L]
    if not isprime(int(nn)):
      ADD = False
      break
  if ADD and n not in circ: circ.append(n)

print('pbm35: {} circular primes below {}'.format(len(circ), l))
print('execution time:', round(time.time() - start, 5))
#%%
# Problem 36: Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2
def bin(n):
  s = ''
  while n > 0:
    s += str(int(n%2))
    n = (n - n%2) / 2
  return int(s[::-1])

l = 100
s = 0
for i in range(1, l+1):
  if str(i)[-1] == '0' or str(bin(i))[-1] == '0': continue
  if str(i) == str(i)[::-1] and str(bin(i)) == str(bin(i))[::-1]:
    s += i
print('pbm36: sum =', s)

#better:
print('pbm36: sum =', sum([n for n in range(1, 1000000, 2) if str(n) == str(n)[::-1] and str(bin(n)) == str(bin(n))[::-1]]))
#%%
# Problem 37: Find the sum of the only eleven primes that are both truncatable from left to right and right to left
import time
start = time.time()

def isprime(n):
  if n == 2: return True
  if n < 2 or n%2 == 0: return False
  for i in range(3, int(n**.5) + 1,2):
    if n%i == 0: return False
  return True

c = 0
s = []
i = 11
while len(s) < 11:
  cont = True
  i += 2
  if not isprime(i): continue
  I = str(i)
  if any([j not in '1379' for j in I]) : continue
  for d in range(len(I)):
    if not isprime(int(I[:d + 1])) or not isprime(int(I[d:])):
      cont = False
      break
  if cont and i not in s:
    s.append(i)

print('pbm37:', s)

print('execution time:', round(time.time() - start, 5))
#%%
# Problem 38: What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
start = time.time()
ss = {i for i in range(1, 10)}
for n in range(3, 50000):
  s = ''
  for j in range(1, 600):
    s += str(n * j)
    if len(s) > 9: break
    if len(s) == 9:
      if {str(x) for x in s} == {str(x) for x in ss}:
        q = s
print('pbm38:', q)
print('execution time:', round(time.time() - start, 5))
#%%
# Problem 39: For which value of p ≤ 1000, is the number of solutions maximised?
#start = time.time()
#nbsolmax = pmax = 0
#smax = []
#l = 1001
#for p in range(1, l):
#  nbsol = 0
#  s = []
#  for a in range(1, l):
#    for b in range(1, l):
#      c = p - a - b
#      if c > 0 and a**2 + b**2 == c**2:
#        if sorted([a, b, c]) not in s:
#          nbsol += 1
#          s.append(sorted([a, b, c]))
#        if nbsol > nbsolmax:
#          nbsolmax = nbsol
#          pmax = p
#          smax = s
#print('pbm39: {} has {} solutions:\n{}'.format(pmax, nbsolmax, smax))
#print('execution time:', round(time.time() - start, 5))

#better:
import time
start = time.time()
p = 2
pmax = nbsolmax = 0
while p <= 1000:
  nbsol = 0
  s = []
  for a in range(1, int(p/3)):
    b = float(p) * (p/2 - a) / (p - a)
    if b.is_integer():
      if sorted([a, b, p-a-b]) not in s:
        nbsol += 1
        s.append(sorted([int(a), int(b), int(p-a-b)]))
      if nbsol > nbsolmax:
        pmax, nbsolmax, smax= p, nbsol, s
  p += 2
print('pbm39: {} has {} solutions:\n{}'.format(pmax, nbsolmax, smax))
print('execution time:', round(time.time() - start, 5))
#%%
# Problem 40: If dn represents the nth digit of the fractional part, find the value of the following expression.
start = time.time()

number = 1
digit = ''
while len(digit) < 10:
  for i in str(number):
    digit += i
  number += 1
s = 1
for i in range(0, 7):
  s *= int(digit[10**i - 1])
  #print('digit{} = {}'.format(10**i, digit[10**i - 1]))
print('pbm40:', s)
print('execution time:', round(time.time() - start, 5))
#%%
# Problem 41: What is the largest n-digit pandigital prime that exists?
import time
from itertools import permutations as per
start = time.time()
res = result = []

def isprime(n):
  if n < 2: return False
  if n == 2: return True
  for i in range(3, 1 + int(sqrt(n)), 2):
    if n%i == 0: return False
  return True

for i in range(2, 10):
  n = '123456789'[0:i]
  a = [''.join(i) for i in per(n)]
  res.extend( [j for j in a if j[-1] in '1379'] )

result = sorted([j for j in res if isprime(int(j))])

print('pbm41:', result[-1])
print('execution time:', round(time.time() - start, 5))

#better:

for i in range(1,9):
    l=list(per('1234567'[0:i]))
    p=[''.join(j) for j in l if isprime(int(''.join(j)))]
    if len(p)!=0:
      print(max(p))
      
#%%
# Problem 42: how many are triangle words?
import time
start = time.time()

dic = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26}

def sumword(word): return sum([dic[w.lower()] for w in word])

def istriangleword(word):
  i = 0
  n = 1
  s = sumword(word)
  while i < s:
    i = 0.5 * n * (n + 1)
    if i == s: return True
    n += 1
  return False

words = ['word1', 'word2']

result = []
for w in words:
  if istriangleword(w): result.append(w)
print(len(result))
print('execution time:', round(time.time() - start, 5))


#better:
def wordval(s):
    alph='0ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return sum([alph.find(i) for i in s])

with open("Euler042data.txt",'r') as f:
    st=f.read()
    l=''.join(c for c in st if c!='"').split(',')
t=[i*(i+1)//2 for i in range(1,50)]
tw=[s for s in l if wordval(s) in t]
print(len(tw))

#%%
# Problem 43: Find the sum of all 0 to 9 pandigital numbers with this property.
import time
from itertools import permutations as per
start = time.time()

string = '0123456789'
primes = [2,3,5,7,11,13,17]
pandigits = []
pandigits.extend( [''.join(i) for i in per(string) if i[0] != '0'] )

result = []
for number in pandigits:
 noadd = False
 for i in range(1, 8):
  if int(number[i:i+3]) % primes[i-1] != 0:
   noadd = True
   break
 if not noadd:
  result.append(int(number))

print('pbm43: sum =', sum(result))
print('execution time:', round(time.time() - start, 5))


#better:
#import time
#start = time.time()
#from itertools import permutations as per
#s, f = 0, [2,3,5,7,11,13,17]
#for b in list(per([i for i in range(10)])):
#    for e in [i for i in range(1,8)]:
#        if (100*b[e]+10*b[e+1]+b[e+2]) % f[e-1] != 0:
#         break
#        if e == 7: s += int(''.join(map(str, b)))
#print('pbm43: sum =', s)
#print('execution time:', round(time.time() - start, 5))

#%%
# Problem 44: Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference are pentagonal and D = |Pk − Pj| is minimised; what is the value of D?

from math import sqrt
import time
start = time.time()

def pent(n):
  return n*(3*n-1)//2

def ispent(x):
  a = (0.5 + sqrt(0.25 + 4 * 1.5 * x)) / 3.0
  return a.is_integer()


l = 10000
result = []
D = 1e50

for i in range(1, l + 1):
  p1 = pent(i)
  for j in range(1, i):
    p2 = pent(j)
    if ispent(p1 + p2) and ispent(abs(p1 - p2)):
      if abs(p1 - p2) < D:
        D = abs(p1 - p2)
        result = [p1, p2]

print('pbm44:', result)
print('execution time:', round(time.time() - start, 5))

#better:
import time
start = time.time()
from itertools import permutations
n = {x*(3*x-1)/2 for x in xrange(1, 2400)}
print(min([x-y for x,y in permutations(n, 2) if x>y and x+y in n and x-y in n]))

print('pbm44:', result)
print('execution time:', round(time.time() - start, 5))
#%%
# Problem 45: Find the next triangle number that is also pentagonal and hexagonal.
import time
start = time.time()

l = 200000
triangle   = {x*(x+1)/2   for x in range(1, l)}
pentagonal = {x*(3*x-1)/2 for x in range(1, l)}
hexagonal  = {x*(2*x-1)   for x in range(1, l)}

res = {i for i in range(1,l) if i in triangle.intersection(pentagonal).intersection(hexagonal)}
#print min([x-y for x,y in per(n, 2) if x>y and x+y in n and x-y in n])

print(res)
print('execution time:', round(time.time() - start, 5))


#better:
def tri(x):
  return (x*(x+1)) / 2

def pent(x):
  return (x*(3*x-1)) / 2

def hexa(x):
  return x*(2*x-1)

found = False

tri_index = pent_index = hexa_index = 144

while not found:
  while tri(tri_index) < pent(pent_index):
    tri_index += 1
  while pent(pent_index) < hexa(hexa_index):
    pent_index += 1
  while hexa(hexa_index) < tri(tri_index):
    hexa_index += 1
  if tri(tri_index) == pent(pent_index) == hexa(hexa_index):
    found = True
    print("Found (",tri_index,",",pent_index,",",hexa_index,")")
    print(hexa(hexa_index))

#better:
def triangle(n):
    return n*(n+1)//2

def pentagonal(n):
    return n*(3*n - 1)//2

def hexagonal(n):
    return n*(2*n -1)

first_10000_triangle = {triangle(x): x for x in range(1,100001)}
first_10000_pentagonal = {pentagonal(x): x for x in range(1,100001)}
first_10000_hexagonal = {hexagonal(x): x for x in range(1,100001)}

for i in first_10000_triangle:
    if i in first_10000_hexagonal and\
       i in first_10000_pentagonal:
        print(i)

#better:
t = set(i*(i+1)//2 for i in range(1,60000))
p = set(i*(3*i-1)//2 for i in range(1,60000))
h = set(i*(2*i-1) for i in range(1,60000))
print(t.intersection(p,h))
#%%
# Problem 46: What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
import time
start = time.time()

def isprime(n):
  if n == 2: return True
  for j in range(2, int(n/2) + 2):
    if n%j == 0: return False
  return True

l = 100

primes = [2]
for i in range(3, l + 1, 2):
  if isprime(i): primes.append(i)

for number in range(9, l, 2):
  if isprime(number): continue
  found, depassement = False, False
  while not found and not depassement:
    for i in primes:
      for j in range(1, 200):
        if i+2*j**2 > number:
          depassement = True
          break
        if i+2*j**2 == number:
          found = True
          break
  if not found:
    print('pbm46:', number)
    break
print('execution time:', round(time.time() - start, 5))

#better:
start = time.time()
from math import ceil, sqrt
primes=[2]
for x in range(3, 100, 2):
  found = False
  if isprime(x):
    primes.append(x)
  elif x%2:
    for p in primes:
      if found == True: break
      for s in range(1, ceil(sqrt(x))):
        if x == p+2*s**2:
          found = True
          break
    if not found:
      print('pbm46:', x)
      print('execution time:', round(time.time() - start, 5))
      break

#better:
start = time.time()

from math import sqrt
def isPrime(n):
  if n < 2: return False
  if n == 2: return True
  for i in range(2, int(sqrt(n)) + 1):
    if n % i == 0: return False
  return True

primes = [isPrime(i) for i in range(10000)]

def goodByGoldbach(number):
  for prIndex in range(len(primes[:number])):
    if primes[prIndex] and number != prIndex and sqrt((number - prIndex)/2) % 1 == 0:
      return True
  return False

for i in range(9, len(primes)):
  if not primes[i] and i%2 == 1 and not goodByGoldbach(i):
    print('pbm46:', i)
    break

print('execution time:', round(time.time() - start, 5))
#%%
# Problem 47: Find the first four consecutive integers to have four distinct prime factors. What is the first of these numbers?
import time
start = time.time()

def isprime(n):
 if n < 2: return False
 if n == 2: return True
 for p in range(2, int(n**0.5) + 1):
  if n%p == 0: return False
 return True

l = 150000
cons = 4

primes = [i for i in range(l + 1) if isprime(i)]
decompose = {}
for number in range(2, l):
 if number in primes: continue
 decompose[number] = [p for p in primes if number%p == 0]
 
 if number in decompose and \
  number + 1 in decompose and \
  number + 2 in decompose and \
  number + 3 in decompose and \
  len(decompose[number + 0]) == cons and \
     len(decompose[number + 1]) == cons and \
     len(decompose[number + 2]) == cons and \
     len(decompose[number + 3]) == cons:
      print(number)
      break

print('execution time:', round(time.time() - start, 5))

#better:
from math import sqrt

def primes(n):
 primfac = 0
 if n % 2 == 0: primfac += 1
 while n%2 == 0: n //= 2
 d = 3
 while d*d <= n:
  if (n % d) == 0:
   primfac += 1
   if primfac > 4: return 0
  while (n%d) == 0: n //= d
  d += 2
 if n > 1: primfac += 1
 return primfac

def run(num=4):
 running = True
 n = num
 
 while running:
  if primes(n) == num:
   flag = True
   
   for i in range(n-1,n-num,-1):
    if primes(i) != num:
     n = i+num
     flag = False
     break

   if flag:
    return n-(num-1)
  else:
   n+=num
   
print(run(4))

#%%
#better:
import time
start = time.time()

Limit = 1000000 
factors = [0] * Limit
count = 0
for i in range(2, Limit):
    if factors[i]==0:
        # i is prime
        count = 0
        val = i
        while val < Limit:
            factors[val] += 1
            val += i
    elif factors[i] == 4:
        count +=1
        if count == 4:
            print(i-3)# First number
            break
    else:
        count = 0

print('execution time:', round(time.time() - start, 5))
#%%
# Problem 48: Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000
import time
start = time.time()

print(str(sum([i**i for i in range(1, 1001)]))[-10:])

print('execution time:', round(time.time() - start, 5))
#%%
# Problem 49: What 12-digit number do you form by concatenating the three terms in this sequence?

import time
start = time.time()
from itertools import permutations as per

def isprime(n):
  if n < 2 or n%2 == 0: return False
  if n == 2: return True
  for p in range(3, int(n**.5) + 1, 2):
    if n%p == 0: return False
  return True

a = [''.join(p) for p in per('1234567890', 4) if p[0] != '0']
b = [p for p in a if isprime(int(p))]
c = [int(i) for i in b]

for el in b:
  if all([per(el) in b]):
    print(per(el))
#for element in b:
#  for element2 in b:
#    for element3 in b:
#      if element != element2 and element != element3 and element2 != element3:
#        if all([i in element2 for i in element]) and all([i in element3 for i in element]):
#          if abs(int(element3) - int(element2)) == abs(int(element2) - int(element)):
#            print(element, element2, element3)

print('execution time:', round(time.time() - start, 5))
#%%
# Problem 50: Which prime, below one-million, can be written as the sum of the most consecutive primes?
#def isprime(n, pr):
#  for i in pr:
#    if n % i == 0:
#      return False
#  return True
#  
#nmax = 1001
#primes = [2]
#find = False
#for i in range(3, 1 + nmax):
#  if isprime(i, primes):
#    primes.append(i)
#  S = 0
#  for j in primes:
#    S += j
#    if isprime(S, primes):
#      q, qq = j, S
#    if S >= 10**6:
#      find = True 
#      break
#  if find: break
#print('pbm50: sum of primes until', q, ':', qq)
#answer = 958577 but does not work
#%%
# Problem 51: Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.
import time; start = time.time()
 
def isprime(n):
  if type(n) == int:
    if n == 2: return True
    if n < 2 or n%2 == 0 or any([n%j == 0 for j in range(3, int(n**.5) + 1, 2)]): return False
    return True
  if type(n) == list:
    if len(n) == 0: return False
    if not all([isprime(i) for i in n]): return False
    return True

number = 99
found = False
while not found:
	number += 2
	if not isprime(number): continue
	s = str(number)
	for i in range(0, len(s) - 2):
		for j in range(i + 1, len(s) - 1):
			count, a = 0, []
			for d in '0123456789':
				b = s[:i] + d + s[i+1:j] + d + s[j+1:]
				if len(str(int(b))) == len(s): a.append(b)
			for n in a:
				if isprime(int(n)): count += 1
				if count == 8:
					found = True
					print(a)
					break
			#print(a)

print('execution time:', round(time.time() - start, 5))
#%%
# Problem 52: Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
import time
start = time.time()
i = 1
found = False
while not found:
  i += 1
  if set([j for j in str(i)]) == set([j for j in str(2*i)]) == set([j for j in str(3*i)]) == set([j for j in str(4*i)]) == set([j for j in str(5*i)]) == set([j for j in str(6*i)]):
    found = True
    print([j*i for j in range(1, 7)])

print('execution time:', round(time.time() - start, 5))

#better:
start = time.time()
n = 1
found = False
while not found:
  for mul in range(2, 7):
    if sorted(str(mul * n)) != sorted(str(n)): break
    else:
      print(n)
      found = True
      break
  n += 1
  
print('execution time:', round(time.time() - start, 5))
#%%
# Problem 53: 
import time
start = time.time()

def f(x):
  if x == 1: return 1
  return x * f(x - 1)

def C(n, k):
  n, k = max(n, k), min(n, k)
  return int(f(n) / (f(k) * f(n - k)))
 
c = 0
for n in range(1, 101):
  for k in range(1, n):
    if C(n, k) > 1e6:
      c += 1

print(c)
 
print('execution time:', round(time.time() - start, 5))
#%%
# Problem 55: How many Lychrel numbers are there below ten-thousand?
import time
start = time.time()

def ispal(n):
  s = str(n)
  for i in range(len(s)):
    if s[i] != s[-1 - i]: return False
  return True

def mirror(n):
  return int(str(n)[::-1])
  
L = 0
limit = 10000

for number in range(limit + 1):
  j = number
  isLychrel = True
  for i in range(51):
    j = j + mirror(j)
    if ispal(j):
      isLychrel = False
      break
  if isLychrel: L += 1
      
  
print('pbm55: {} Lychrel numbers below {}'.format(L, limit))
print('execution time:', round(time.time() - start, 5))

# better:
start = time.time()
def isLychrel(n):
  for i in range(50):
    n = n + int(str(n)[::-1])
    if str(n) == str(n)[::-1]: return False
  return True
    
print ('pbm55: {} Lychrel numbers below {}'.format(len([x for x in range(limit) if isLychrel(x)]), limit))
print('execution time:', round(time.time() - start, 5))
#%%
# Problem 56: Considering natural numbers of the form, a^b, where a, b < 100, what is the maximum digital sum?
import time
start = time.time()

rm = 0
for a in range(1, 101):
  for b in range(1, 101):
    s = sum(int(i) for i in str(a**b))
    if s > rm:
      rm = s
      ra = a
      rb = b

print ('pbm56: {}^{} = {}, sum = {}'.format(ra, rb, ra**rb, rm))
print('execution time:', round(time.time() - start, 5))

#better:
import time
start = time.time()

def digitSum(n):
#  s = 0
#  while n:
#    s += n % 10
#    n //= 10
#  return s
  return sum(int(i) for i in str(n))

print(max(digitSum(i**j) for i in range(101) for j in range(101)))
print('execution time:', round(time.time() - start, 5))
#%%
# Problem 57: In the first one-thousand expansions, how many fractions contain a numerator with more digits than denominator?
from math import gcd
import time; start = time.time()

fraction = [[3,2],]
c = 0
for j in range(1000):
  a = fraction[j][0]
  b = fraction[j][1]
  fraction.append([2*b+a, b+a])
  if len(str(fraction[j][0])) > len(str(fraction[j][1])): c += 1

print ('pbm57:', c)
print('execution time:', round(time.time() - start, 5))

#better:
start = time.time()
n, d, c = 3, 2, 0
for i in range(1000):
    n, d = n + 2*d, d+n
    if len(str(n)) > len(str(d)): c += 1
print(count)


print ('pbm57:', c)
print('execution time:', round(time.time() - start, 5))
#%%
# Problem 59: decrypt the message and find the sum of the ASCII values in the original text
import time
start = time.time()
from random import choice

def f(n):
	if n <= 1: return 1
	return n * f(n - 1)

with open('p059.txt','r') as f:
  t = f.read().split(",")

for o in range(256):
  keys += chr(o)

key = choice(keys) + choice(keys) + choice(keys)
'azertyuiopqsdfghjklmwxcvbn,1234567890;:!./§?^¨ù%*µ$£¤AZERTYUIOPMLKJHGFDSQWXCVBN<>&é"(-è_çà)`\[{#~|@]}+°='
a = ''
for i in range(10):
  a += chr(int(t[i]) ^ ord(key))
  
print(a)
print('execution time:', round(time.time() - start, 5))
#%%
# Problem 79: Given that the 3 characters are always asked for in order, analyse the file so as to determine the shortest possible secret passcode of unknown length.
import time
start = time.time()

passes = [i.strip() for i in open("p079.txt")]
chars = set(''.join(passes))
before = {i:[] for i in chars}
for i in passes:
    p = list(i)
    if p[1] not in before[p[2]]: before[p[2]] += [p[1]]
    if p[0] not in before[p[2]]: before[p[2]] += [p[0]]
    if p[0] not in before[p[1]]: before[p[1]] += [p[0]]
      
l = sorted([[k] + v for k,v in before.items()], key = len)
print ('pbm79:')
for i in l: print(i[0], end = '')
print('\nexecution time:', round(time.time() - start, 5))
#%%
# Problem 63: How many n-digit positive integers exist which are also an nth power?
import time
start = time.time()

c = []
for i in range(1, 1000):
	for digit in range(1, 100):
		if len(str(i**digit)) == digit:
			#c += 1
			c.append([i, digit, i**digit])
print(len(c))
print('execution time:', round(time.time() - start, 5))

#better:
import math as m
print(len([1 for a in range(1,10) for b in range(1,22) if m.floor(m.log(a**b,10))+1 == b]))

#better:
from math import ceil, pow
print(sum(10 - ceil(pow(10,(k-1)/k)) for k in range(1,100)))
#%%
# Problem 67: Find the maximum total from top to bottom in triangle.txt
import time; start = time.time()
import os
os.chdir('C:\\Users\\guigui\\OneDrive\\Documents\\IT\\Python')

data = []
with open('p067.txt','r') as f:
  for line in f:
    row = []
    for num in line.split():
        row.append(int(num))
    data.append(row)

#print(data)
while len(data) > 1:
  lastRow = len(data) - 1
  for col in range(len(data[lastRow]) - 1):
    data[lastRow - 1][col] += max(data[lastRow][col], data[lastRow][col+1])
  data.pop()
    
print(data[0][0])
print('execution time:', round(time.time() - start, 5))

#better:
import time; start = time.time()
from functools import reduce
from operator import add
numbers = [[int(i) for i in line.split()] for line in open('p067.txt')]
def rmax(row1, row2):
    row1 = map(max, zip(*(row1[i:] for i in range(2))))
    return list(map(add, row1, row2))
print(reduce(rmax, reversed(numbers)))
print('execution time:', round(time.time() - start, 5))

#%%
# Problem 54: How many poker hands does Player 1 win?
import time; start = time.time()

with open('p054_poker.txt','r') as f:
  content = f.read().split()

#content = content.split()
Suits_dic = {'D': 'Diamonds', 'C': 'Clubs', 'S': 'Spades', 'H': 'Hearts'}
Values_dic = {'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}
for i in ''.join([str(i) for i in range(2, 10)]):
  Values_dic[i] = int(i)
	
Hands_dic = {'Royal Flush':10, 'Straight Flush':9, 'Four of a Kind':8,
'Full House':7, 'Flush':6, 'Straight':5, 'Three of a Kind':4, 'Two Pairs':3, 'Pair':2, 'High Card':1}



def checkhand(myslist):
  suite = 'A23456789TJQKA'
  a, b = [], []
  for e in myslist:
    a.append(e[0]) #value
    b.append(e[1]) #suit
  # Royal Flush:
  for i in b:
  	if b.count(i) == 5 and all([j in 'TJQKA' for j in a]): return ['Royal Flush', i]
  # Straight Flush:
  for i in range(10):
  	c = ''.join(a)
  	if suite[i] in c and suite[i+1] in c and suite[i+2] in c and suite[i+3] in c and suite[i+4] in c:
  		for j in b:
  			if b.count(j) == 5: return ['Straight Flush', suite[i+4]]
  # Four of a kind:
  for i in a:
  	if a.count(i) == 4: return ['Four of a Kind', i]
  # Full House:
  for i in a:
  	if a.count(i) == 3:
  		for j in a:
  			if a.count(j) == 2: return ['Full House', i, j]
  # Flush:
  for i in b:
  	if b.count(i) == 5: return ['Flush', i]
  # Straight:
  for i in range(10):
    c = ''.join(a)
    if suite[i] in c and suite[i+1] in c and suite[i+2] in c \
    and suite[i+3] in c and suite[i+4] in c:
    	return ['Straight', suite[i+4]]
  # Three of a Kind:
  for i in a:
  	if a.count(i) == 3: return ['Three of a Kind', i]
  # Pair and Two Pairs:
  pair = 0
  J = set()
  for i in a:
  	if a.count(i) == 2 and i not in J:
  		pair +=1
  		J.add(i)
  if pair == 2: return ['Two Pairs', sorted(list(J))[0], sorted(list(J))[1]]
  elif pair == 1: return ['Pair', list(J)[0]]
  # High Card:
  j = 0
  for i in a:
  	if Values_dic[i] > j:
	  	J = i
	  	j = Values_dic[i]
  if j != 0: return ['High Card', J]



p1_wins, hands = 0, []
while len(content) > 0:
  hands.append(list(content[0:10]))
  del content[:10]

for hand in hands:
	p1 = checkhand(hand[:5])
	p2 = checkhand(hand[5:])
	if p1 is None or p2 is None: continue
	if Hands_dic[p1[0]] > Hands_dic[p2[0]]:
		p1_wins += 1
	elif Hands_dic[p1[0]] == Hands_dic[p2[0]]:
		if Values_dic[p1[1]] > Values_dic[p2[1]]:
			p1_wins += 1
	
	
print('p1 wins {} times'.format(p1_wins))
print('execution time:', round(time.time() - start, 5))


#better:
from enum import IntEnum
start = time.time()

CardVals = { '2':2, '3':3, '4':4, '5':5, '6':6, '7':7,'8':8,
             '9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A':14 }

class Rank(IntEnum):
    HighCard      = 1
    OnePair       = 2
    TwoPair       = 3
    ThreeOfAKind  = 4
    Straight      = 5
    Flush         = 6
    FullHouse     = 7
    FourOfAKind   = 8
    StraightFlush = 9
    RoyalFlush    = 10

class Hand:
    """
    A hand is encoded as a rank and a list of 5 tuples, each tuple recording
    the count of cards having the same value, then the value from 1 (ace low)
    to 14 (ace high).  The list is sorted in reverse order, by card count then
    card value.  This allows for easy comparisons.  The suit is thrown away,
    after detecting a flush.
    """
    def __init__(self, cards):
        flush = len(set(card[1] for card in cards)) == 1
        vals = [CardVals[card[0]] for card in cards]
        self.cards = sorted([(vals.count(val), val) for val in vals], reverse=True)
        if self.cards[0][0] == 4:            self.rank = Rank.FourOfAKind
        elif self.cards[0][0] == 3:
            if self.cards[3][0] == 2:        self.rank = Rank.FullHouse
            else:                            self.rank = Rank.ThreeOfAKind
        elif self.cards[0][0] == 2:
            if self.cards[2][0] == 2:        self.rank = Rank.TwoPair
            else:                            self.rank = Rank.OnePair
        else:   # nothing paired up, all counts will be 1
            if self.cards[0][1] == 14 and \
               self.cards[1][1] == 5 and \
               self.cards[4][1] == 2:
                # special case - straight with ace low
                self.cards[0] = (1, 1)
                self.cards.sort(reverse=True)
            if self.cards[0][1] == self.cards[4][1] + 4:
                if not flush:                self.rank = Rank.Straight
                elif self.cards[0][1] == 14: self.rank = Rank.RoyalFlush
                else:                        self.rank = Rank.StraightFlush
            elif flush:                      self.rank = Rank.Flush
            else:                            self.rank = Rank.HighCard

    def __lt__(self, other):
        if self.rank == other.rank:
            return self.cards < other.cards
        return self.rank < other.rank

def p54():
    count = 0
    with open("p054_poker.txt") as f:
        for line in f:
            cards = line.split()
            if Hand(cards[:5]) > Hand(cards[5:]):
                count += 1
    return count

print(p54())
print('execution time:', round(time.time() - start, 5))
#%%
# Problem 92: How many starting numbers below ten million will arrive at 89?
import time
start = time.time()

class Chain:
	def __init__(self):
		self.memory = {}

	def chain(self, n):
  		if n in self.memory: return self.memory[n]
  		if n in [1, 89]: return n
  		p = self.chain(sum(int(i)**2 for i in str(n)))
  		self.memory[n] = p
  		return p

mychain = Chain()
d = 0
for i in range(1, 10000000):
  ch = mychain.chain(i)
  if ch == 89: d +=1

print(d)
print('execution time:', round(time.time() - start, 5))
#%%
# Problem 97: Find the last ten digits of this prime number: 28433×2^7830457+1
import time
start = time.time()

print(str(28433*2**7830457+1)[-10:])

#better:
print(((28433*2**7830457) + 1) % 10000000000)

print('execution time:', round(time.time() - start, 5))
#%%
# Problem 99: determine which line number has the greatest numerical value

from math import log
import time
start = time.time()

with open('p099.txt', 'r') as myfile:
  s = myfile.read()
n = s.split('\n')

m = []
maxi = l = 0
for each in n:
	l += 1
	m = each.split(',')
	a = int(m[1]) * log (int(m[0]))
	if a > maxi:
		maxi = a
		res = l

print(res)
print('execution time:', round(time.time() - start, 5))


#better:
start = time.time()
b, e, n = 1, 1, None
for base, exp, num in [l.split(',') + [i] for i, l in enumerate(open('p099.txt'))]:
	b,e,n = (int(base), int(exp), num) if int(base)**(1/e) > b**(1/int(exp)) else (b,e,n)
print(n + 1)
print('execution time:', round(time.time() - start, 5))


#better:
start = time.time()
from math import log

with open('p099.txt', 'r') as f:
  l = [int(p[1])*log(int(p[0])) for p in [(i.rstrip('\n').split(",")) for i in f.readlines()]]
print(l.index(max(l))+1)
print('execution time:', round(time.time() - start, 5))
#%%
# Problem 549: #The smallest number m such that 10 divides m! is m=5.
#The smallest number m such that 25 divides m! is m=10.
#Let s(n) be the smallest number m such that n divides m!
#So s(10)=5 and s(25)=10.
#Let S(n) be ∑s(i) for 2 ≤ i ≤ n.
#S(100)=2012
#Find S(10**8)

import time
start = time.time()

def f(n):
	if n <= 1: return 1
	return n * f(n - 1)

def s(n):
	for m in range(2, n + 1):
		if f(m) % n == 0:
			return m

def S(n):
	return sum(s(i) for i in range(2, n + 1))
		
print(S(800))	
print('execution time:', round(time.time() - start, 5))
#%%
# Problem 372: Find R(2·10^6, 10^9).
import time
start = time.time()

def R(M, N):
  c = 0
  for x in range(M + 1, N + 1):
    for y in range(M + 1, N + 1):
      if int(y**2 / x**2) % 2 != 0:
        c += 1
  return c

print(R(0,100))
print('\nexecution time:', round(time.time() - start, 5))
#%%
#Problem 206: Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0, where each _ is a single digit
import time; start = time.time()
#import re
#for i in range(10**9, 10**10, 10):
#	if re.match(r'1.2.3.4.5.6.7.8.9.0', str(i**2)):
#		print(i)
#		break

#better:
for sq in (p + f for f in (30, 70) for p in range(1389026600, 1010101000, -100)):
    if str(sq * sq)[::2] == '1234567890': break
print(sq)
print('execution time:', round(time.time() - start, 5))


#better:
start = time.time()
from re import compile, match
patt = compile('1.2.3.4.5.6.7.8.9.0')
for sq in (p + f for f in (30, 70) for p in range(1389026600, 1010101000, -100)):
    if patt.match(str(sq*sq)): break
print(sq)
print('execution time:', round(time.time() - start, 5))
#%%
#Problem 59: decrypt the message and find the sum of the ASCII values in the original text
import time; start = time.time()

#code=[]
#for i in range(103,123):
#    for j in range(97,123):
#        for k in range(97,123):
#            code.append([i,j,k])
#
#for k in code:
#    back=[text[i]^k[i%3] for i in range(len(text))]    
#    outp = ''.join([chr(i) for i in back])
#    if 'The ' in outp or 'the ' in outp:
#        outp = ''.join([chr(i) for i in back])
#        print k, outp
#        break
#print sum([ord(i) for i in outp])
#print "DONE"
#print('execution time:', round(time.time() - start, 5))

#better:
#start = time.time()
#with open('p059_cipher.txt', 'r') as f:
#  txt = f.read().split(',')
#  
#''.join([chr(ord(x)^ord(y)) for (x, y) in zip(key * ((len(txt)) // len(key)) + 1), txt)])
#print('execution time:', round(time.time() - start, 5))

#better:
start = time.time()
from collections import Counter
nums = eval('[' + open('p059_cipher.txt').read() + ']')
keys = list(Counter(nums[i::3]).most_common()[0][0] ^ ord(' ') for i in range(3))
print(sum(n ^ keys[i%3] for i,n in enumerate(nums)))
print('execution time:', round(time.time() - start, 5))
#%%
#Problem 69: Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.
import time; start = time.time()
from math import gcd

#N = 1000000
#
#m = 3
#for number in range(2, N, 2):
#  c = 0
#  for i in range(1, number):
#    if gcd(number,i) == 1:
#      c += 1
#      if number/c < m: break
#  if number/c > m:
#    m = number/c
#    J = number
#print('max = {} for n = {}'.format(m, J))
    
#return [gcd(n,i) for i in range(n)].count(1)
    
#a = list()
#for n in range(2, N, 2):
#  b = [i for i in range(1, n) if gcd(n,i) == 1]
#  a.append(n / len(b))

#print( max([n / len([i for i in range(1, n) if gcd(n,i) == 1]) for n in range(2, N, 2)]) )

#for j in range(2, 10000, 2):
#	if j/totient(j) > m:
#		m = j/totient(j)
#		J = j
l = 1000000

def isprime(n):
  if n == 2: return True
  if n < 2 or n%2 == 0: return False
  for j in range(3, int(n**.5) + 1, 2):
    if n%j == 0: return False
  return True

primes = [i for i in range(200) if isprime(i)]
n, i = 1, 0
while n * primes[i] < l:
  n *= primes[i]
  i += 1
  
print('max for n = {}'.format(n))
print('execution time:', round(time.time() - start, 5))
#%%
#Problem 71: By listing the set of reduced proper fractions for d ≤ 1,000,000 in ascending order of size, find the numerator of the fraction immediately to the left of 3/7
import time; start = time.time()
from math import gcd


#fractions = {}
#for dd in range(2, d + 1):
#	for nn in range(1, dd):
#		g = gcd(nn, dd)
#		fractions[(nn/g) / (dd/g)] = '{}/{}'.format(int(nn/g), int(dd/g))
#
#liste = [[key, fractions[key]] for key in sorted(fractions)]
#del fractions
#i = liste.index([3/7, '3/7'])
#print(liste[i-1][1])
#print('execution time:', round(time.time() - start, 5))


#better:
#start = time.time()
#
#s = []
#for den in range(2, d + 1):
#  s.extend(num / den for num in range(1, den))
#s = list(set(s))
#s.sort(reverse = False)
#a = s.index(3/7)
#
#for i in range(int(d/2), 1, -1):
#  if i * s[a-1] == int(i * s[a-1]):
#    num = i
#    break
#print('{}/{}'.format(int(i * s[a-1]), i))

#better:
d = 1000000
a, b = 3/7-1/(1000*d), 3/7
diffmin = 1
for den in range(d, int(0.95*d), -1):
  for num in range(int(den*a), int(den*b) + 1):
    diff = 3/7 - num / den
    if diff < 0: break
    if 0 < diff < diffmin:
      diffmin = diff
      N = num/gcd(num,den)
      D = den/gcd(num,den)
      
print('%d/%d' % (N,D))
print('execution time:', round(time.time() - start, 5))

#better:
start = time.time()
M = 1000000
n,d = 2, 5
while d + 7 <= M:
    n += 3
    d += 7

print('%d/%d' % (n,d))
print('execution time:', round(time.time() - start, 5))
#%%
#Problem 76: How many different ways can one hundred be written as a sum of at least two positive integers?


import time; start = time.time()

N = 100

l = [1] + [0] * N
for i in range(1, len(l)):
    for j in range(i, len(l)):
        l[j] += l[j - i]

for i in range(len(l)):
	l[i] -= 1

print('{} can be written in {} different ways'.format(N, l[N]))

print('execution time:', round(time.time() - start, 5))
#%%
#Problem 357
'''Consider the divisors of 30: 1,2,3,5,6,10,15,30.
 It can be seen that for every divisor d of 30, d+30/d is prime. 

Find the sum of all positive integers n not exceeding 100 000 000
such that for every divisor d of n, d+n/d is prime. 
'''

import time; start = time.time()

N = 100

def isprime(n):
  if n == 2: return True
  if n < 2 or n%2 == 0 or any([n%j == 0 for j in range(3, int(n**.5) + 1, 2)]): return False
  return True


def divisors(n):
	div = [1, n]
	div += [i for i in range(2, n//2 + 1) if n%i == 0]
	return sorted(div)


result = []
for n in range(1, N):
	if isprime(n): continue
	if all([isprime(d + n/d) for d in divisors(n)]): result.append(n)

print(sum(result))
print('execution time:', round(time.time() - start, 5))

#better:
start = time.time()
def PE357(limit=10**8):
  lim=limit+2
  BA = bytearray
  prime = BA([True])*(lim+1)
  prime[:2] = BA(2)
  prime[4::2] = BA(limit>>1)
  for i in range(3, int(lim**0.5)+1, 2):
    if prime[i]:  prime[i*i::i]=BA(lim//i-i+1)
  res = 0
  for n in range(2, limit+1, 4): # killer : step by 4
      if prime[n+1] and prime[n//2+2] and \
      all(prime[d+n//d] for d in range(3, int(n**0.5)+1) if not n%d):
        res+=n
  return 1+res
  
print(PE357(10**8))
print('execution time:', round(time.time() - start, 5))
#%%
#Problem 81: Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing a 80 by 80 matrix, from the top left to the bottom right by only moving right and down.

import time; start = time.time()

data = [[131, 673, 234, 103, 18], [201, 96, 342, 965, 150], [630, 803, 746, 422, 111], [537, 699, 497, 121, 956], [805, 732, 524, 37, 331]]

l = len(data)
 
#calculate the solution for bottom right:
for i in range(l - 2, -1, -1):
	data[l-1][i] += data[l-1][i+1]
	data[i][l-1] += data[i+1][l-1]


for i in range(l-2, -1, -1):
	for j in range(l-2, -1, -1):
		data[i][j] += min(data[i+1][j], data[i][j+1])

print(data[i][j])
print('execution time:', round(time.time() - start, 5))
#%%
#Problem 387: Harshad numbers
import time; start = time.time()

def isprime(n):
	if n == 2: return True
	if not isinstance(n, int) or n < 2 or n%2 == 0: return False
	for j in range(3, int(n**.5) + 1, 2):
		if n%j == 0: return False
	return True

def sumDigits(n):
  return sum([int(i) for i in str(n)])

def isHarshad(n):
	return True if n % sumDigits(n) == 0 else False

def isStrongHarshad(n):
	return True if isHarshad(n) and isprime(n/sumDigits(n)) else False

def isRightTruncHarshad(n):
	N = str(n)
	if len(N) == 1: return True
	for i in range(1, len(N)):
		if not isHarshad(int(N[:i])): return False
	return True	

def isStrongRightTruncHarshadPrime(n):
	N = str(n)
	if len(N) < 2:
		a = int(N[:len(N)])
	else:
		a = int(N[:len(N)-1])
	return True if isprime(n) and isStrongHarshad(a) and isRightTruncHarshad(n) else False

s = []
for i in range(2, 10000):
	if isStrongRightTruncHarshadPrime(i): s.append(i)
	
print(s)

print('execution time:', round(time.time() - start, 5))

#%%
#Problem 493:

'''
70 colored balls are placed in an urn, 10 for each of the seven rainbow colors.
What is the expected number of distinct colors in 20 randomly picked balls?
'''

from functools import reduce
import operator

def fact(n):
	if n == 0: return 1
	return reduce(operator.mul, [i for i in range(1, n+1)], 1)

combin = lambda n,k: fact(n)//(fact(k)*fact(n-k))

'''
E(X) 
= E(X0+X1+...+X6) 
= E(X0) + E(X1) + ... + E(X6)        by linearity of expectation
= 7E(X0)                             by symmetry
= 7 * probability that a particular color is present
= 7 * (1- probability that a particular color is absent)
= 7 * (1 - (# ways to pick 20 avoiding a color)/(# ways to pick 20))
= 7 * (1 - (60 choose 20)/(70 choose 20))
'''

#better:
result = 1
for i in range(20):
   result *= (60-i)/(70.0-i)
result = 7*(1-result)

print(result)

#better:
result = 7 * (1 - combin(60, 20)/combin(70, 20))
print(result)

#%%
#Problem 549:
'''
The smallest number m such that 10 divides m! is m = 5
The smallest number m such that 25 divides m! is m = 10
Let s(n) be the smallest number m such that n divides m!
So s(10) = 5 and s(25) = 10
Let S(n) be ∑s(i) for 2 ≤ i ≤ n
S(100)=2012
Find S(10**8)
'''

import time; start = time.time()

def prod(*args):
	r = 1
	for i in args:
		for j in i:
			r *= j
	return r

def isprime(n):
	if n == 2: return True
	if not isinstance(n, int) or n < 2 or n%2 == 0: return False
	for i in range(3, int(n**.5) + 1, 2):
		if n%i == 0: return False
	return True

def decompose(n):
	if isprime(n): return [n]
	copy = n
	i = 2
	decomp = []
	while copy != 1:
		if copy%i == 0:
			decomp.append(i)
			copy /= i
			i -= 2
		if i == 2:
			i += 1
		else:
			i += 2
	return decomp

def f(n):
	if n <= 1: return 1
	r = 1
	for i in range(2, n+1):
		r *= i
	return r

def s(n):
	for m in range(2, n + 1):
		if f(m) % n == 0:
			return m


def S(n):
	return sum(s(i) for i in range(2, n + 1))
		
print(S(100))	


print('execution time:', round(time.time() - start, 5))

#%%
def print_directory_contents(sPath):
    import os                                       
    for sChild in os.listdir(sPath):                
        sChildPath = os.path.join(sPath,sChild)
        if os.path.isdir(sChildPath):
            print_directory_contents(sChildPath)
        else:
            print(sChildPath)
print_directory_contents('C:\\Users\\guigui\\OneDrive\\Documents\\IT\\Python')

#%%
in_a_row = 20
limit = 10000

liste = [0,] * (1 + limit)

for i in range(in_a_row, 1 + limit):
  liste[i] = 0.5**in_a_row + sum([0.5**k * liste[i - k] for k in range(1, in_a_row + 1)])

c, result = 0, []
for el in liste:
  c += 1
  if c%10 == 0: result.append(el) 
print(result)
#%%
# MOOC Programming Assignment #1
# compute the number of inversions

import time; start = time.time()
import os; os.chdir('C:\\Users\\guigui\\OneDrive\\Documents\\IT\\Python')

with open('MOOC_ex1.txt','r') as f:
  t = f.read().strip().split("\n")

A = [int(i) for i in t]
#print(len(t))
del t
inversion = 0

def mergeSort(alist):

  if len(alist) > 1:
    global inversion
    mid = len(alist)//2
    lefthalf = alist[:mid]
    righthalf = alist[mid:]

    mergeSort(lefthalf)
    mergeSort(righthalf)

    i = j = k = 0
    
    while i < len(lefthalf) and j < len(righthalf):
      if lefthalf[i] < righthalf[j]:
        alist[k] = lefthalf[i]
        i += 1
      else:
        alist[k] = righthalf[j]
        j += 1
        inversion += 1
      k += 1

    while i < len(lefthalf):
      alist[k] = lefthalf[i]
      i += 1
      k += 1

    while j < len(righthalf):
      alist[k] = righthalf[j]
      j += 1
      k += 1
  return inversion
      #print("Merging ", alist)

print(mergeSort(A))
print('execution time:', round(time.time() - start, 5))
#%%
count = 0
import time; start = time.time()
import os; os.chdir('C:\\Users\\guigui\\OneDrive\\Documents\\IT\\Python')

with open('MOOC_ex1.txt','r') as f:
  t = f.read().strip().split("\n")

A = [int(i) for i in t]
#print(len(t))

def merge_sort(li):

    if len(li) < 2: return li 
    m = len(li) // 2 
    return merge(merge_sort(li[:m]), merge_sort(li[m:])) 

def merge(l, r):
    global count
    result = [] 
    i = j = 0 
    while i < len(l) and j < len(r): 
        if l[i] < r[j]: 
            result.append(l[i])
            i += 1 
        else: 
            result.append(r[j])
            count = count + (len(l) - i)
            j += 1
    result.extend(l[i:]) 
    result.extend(r[j:]) 
    return result

print(merge_sort(A))
print(count)
#%%
#!/usr/bin/python
# -*- coding: utf-8 -*-
count = 0
import time; start = time.time()
import os; os.chdir('C:\\Users\\guigui\\OneDrive\\Documents\\IT\\Python')

with open('MOOC_ex2.txt','r') as f:
  t = f.read().strip().split('\n')

A = [int(i) for i in t]

def QuickSort(A):
  global count
  pivot = A[-1]
  i = 1
  for j in range(i, A[-1] + 1):
    if A[j] < pivot:
      A[i], A[j] = A[j], A[i]
      count += 1
      i += 1
  A[0], A[i] = A[i], A[0]
  return count, A[:10]

print(QuickSort(A))

#def trirapide(L, g, d):
#  global count
#  pivot = L[(g+d)//2]
#  i = g
#  j = d
#  while True:
#    while L[i] < pivot: i += 1
#    while L[j] > pivot: j -= 1
#    if i > j: break
#    if i < j:
#      L[i], L[j] = L[j], L[i]
#      count = count + 1#(len(l) - i)
#    i += 1
#    j -= 1
#  if g < j: trirapide(L,g,j)
#  if i < d: trirapide(L,i,d)
#  return count
#g = 0
#d = len(A)-1
#print(trirapide(A,g,d))

print('execution time:', round(time.time() - start, 5))
#%%
count = 0
import time; start = time.time()
import os; os.chdir('C:\\Users\\guigui\\OneDrive\\Documents\\IT\\Python')

with open('MOOC_ex2.txt','r') as f:
  t = f.read().strip().split('\n')

A = [int(i) for i in t]

def partition(mylist, start, end, count):
    pos = start
    for i in range(start, end):
        count += 1
        if mylist[i] < mylist[end]:
            mylist[i], mylist[pos] = mylist[pos], mylist[i]
            pos += 1
    mylist[pos], mylist[end] = mylist[end], mylist[pos]
    return pos, count

def quicksort(mylist, start, end, count):
    if start < end:
        pos, count = partition(mylist, start, end, count)        
        count = quicksort(mylist, start, pos - 1, count)
        count = quicksort(mylist, pos + 1, end, count)
    return count


#x = [2,3,1,6,9,7]
count = quicksort(A, 0, len(A)-1, 0)
print(count)
print('execution time:', round(time.time() - start, 5))

#%%
import time; start = time.time()
def FastPower(a,b):
  if b == 1: return a
  else:
    c = a*a
    ans = FastPower(c, int(b/2))
  if b % 2 != 0:
    return a*ans
  else:
    return ans

print(FastPower(5,200))
print('execution time:', round(time.time() - start, 5))

#%%
def count_letters(string_val):
  list_a = [string_val[0]]
  list_1 = [0]
  count = 0
  cl = 0
  for i in string_val:
    cl += 1
    if not i==list_a[-1]:
      list_a.append(i)
      list_1.append(0)
      cl = 1
      count += 1
      list_1[count] = cl
  
    for i in range(len(list_a)):
      list_a[i]=str(list_1[i])+list_a[i]
      
  return "".join(list_a)

print(count_letters("aaaaabbbbccccccaaaaaaa"))
#%%
'''
Monte Carlo Stock Price Simulation Using Random Walk
March 30, 2016 by Michael Grogan
The purpose of a Monte Carlo simulation is to observe a range of potential outcomes based on a numerical simulation. For instance, if an investor chooses to hold an asset with a given level of return and volatility, then the same can be modelled to examine a range of potential gains and losses over a specified period.
The below program calculates a price path of a stock using a random walk for a given level of return (mu) and volatility (vol). Moreover, our histogram plots allow us to observe a range of potential returns throughout the period as well as frequency of those returns:
''' 

#Import libraries:
#from __future__ import division
import numpy as np
import math
import matplotlib.pyplot as plt
#from scipy.stats import norm
 
#Define Variables
T = 250 #Number of trading days (we also run at 1000 for the purposes of comparison).
mu = 0.09 #Return
vol = 0.34 #Volatility
 
daily_returns = 1 + np.random.normal(mu/T, vol/math.sqrt(T), T)
 
price_list = [200]
for x in daily_returns:
  price_list.append(price_list[-1]*x)
 
#Generate Plots
plt.plot(price_list)
plt.hist(daily_returns-1, 100) #Note that we run the line plot and histogram separately, not simultaneously.
plt.show()
#%%
def clearall():
  all = [var for var in globals() if var[0] != "_"]
  for var in all:
    del globals()[var]
clearall()