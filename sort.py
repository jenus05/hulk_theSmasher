# def even_odd_sort(list):
#     evn = []
#     odd = []
#     for num in list:
#         if num%2==0:
#             evn.append(num)
#             evn.sort(key=int)
#         else:
#             odd.append(num)
#             odd.sort(key=int)
#     print evn,"the even numbers"
#     print odd, "the odd numbers"
#     print evn + odd

# list = [2,34,5,6,8,9,77,5]
# even_odd_sort(list)

# def even_odd_sort_modified(list):
#     lambda evn,odd: num%2==0: evn.append(num) else: odd.append(num), list
#     print evn,"the even numbers"
#     print odd, "the odd numbers"
#     print evn + odd


# def prime_numbers(list):
#     prime_arr = []
#     for i in range(2,len(list)):
#         if (i==2 or i==3 or i==5 or i==7) or (i%2!=0 and i%3!=0 and i%5!=0 and i%7!=0 and i%(i**(float(0.5)))!=0):
#             prime_arr=prime_arr+[i]
#     print prime_arr

# list = [2,34,5,6,8,9,77,5]
# prime_numbers(list)


# num = input('get the value:')
# for i in range(2,num+1):
#     count = 0
#     for j in range(2,i):
#         if i%j != 0:
#             count += 1
#     if count == i-2:
#         print i,

# def prime_number(a):
#     yes=[]
#     for i in range (2,a):
#         if (i==2 or i==3 or i==5 or i==7) or (i%2!=0 and i%3!=0 and i%5!=0 and i%7!=0 and i%(i**(float(0.5)))!=0):
#             yes=yes+[i]
#     print (yes)

# prime_number(200)

# def uniques_num(n):
#     for i in range(n):
#         quotient = i/10
#         remainder = i%10
#         if quotient == remainder:
#             # print "same digit"
#             continue
#         else:
#             print i

# uniques_num(50)


# def uniques_num(n):
#     def check(i):
#         return i%10 == i/10
#     new_list = [i for i in range(n) if not check(i)]
#     print new_list

# uniques_num(50)

import schedule
import time

def job():
    print("I'm working...")

schedule.every(10).minutes.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("10:30").do(job)
schedule.every().monday.do(job)
schedule.every().wednesday.at("13:15").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)