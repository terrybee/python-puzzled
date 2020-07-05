import datetime

loop_count = 20000

def method1():
  out_str = ''
  for num in range(loop_count):
    out_str += str(num)
  return out_str

def method4():
  str_list = []
  for num in range(loop_count):
    str_list.append(str(num))
  return ''.join(str_list)

def method6():
  return ''.join([str(num) for num in range(loop_count)])

start = datetime.datetime.now()
method1()
finish = datetime.datetime.now()
print(finish-start)

start = datetime.datetime.now()
method4()
finish = datetime.datetime.now()
print(finish-start)

start = datetime.datetime.now()
method6()
finish = datetime.datetime.now()
print(finish-start)