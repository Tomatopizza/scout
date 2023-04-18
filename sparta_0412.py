# import multiprocessing as mp
# from multiprocessing import Process
# import os
# import time

# def func1():
#     c_process = mp.current_process()
#     p_process = mp.parent_process()
#     print('Started. , pid : ',c_process.pid,' ppid : ',p_process.pid)
#     time.sleep(1)
#     print('Ended. , pid : ',c_process.pid,' ppid : ',p_process.pid)

# def func2():
#     print('Started. , pid : ',os.getpid(),' ppid : ',os.getppid())
#     time.sleep(1)
#     print('Ended. , pid : ',os.getpid(),' ppid : ',os.getppid())


# if __name__ =='__main__':
#     print(os.getppid())
#     print(os.getpid())
#     proc1 = Process(target=func1)
#     proc2 = Process(target=func2)
#     proc1.start()
#     proc2.start()


from multiprocessing import Process
import threading
import os

def foo():
    print('child', os.getpid())
    print('my parent is', os.getppid())
def foo2():
    print("i'm thread")
    print('child', os.getpid())
    print('my parent is', os.getppid())
    
if __name__ == '__main__': #여기서부터 시작해라.
    # print('parent process', os.getppid())
    print('me process', os.getpid())
    child = Process(target=foo).start() #푸라는 애를 만들거고.바로실행해
    child1 = Process(target=foo).start()
    thread2 = threading.Thread(target=foo2).start() 
    child2 = Process(target=foo).start() 
    thread1 = threading.Thread(target=foo2).start()
    child3 = Process(target=foo).start() #푸라는 애를 만들거고.바로실행해
    child4 = Process(target=foo).start()
    thread3 = threading.Thread(target=foo2).start() 
    child5 = Process(target=foo).start() 
    thread4 = threading.Thread(target=foo2).start()
    child6 = Process(target=foo).start() #푸라는 애를 만들거고.바로실행해
    child7 = Process(target=foo).start()
    thread5 = threading.Thread(target=foo2).start() 
    child8 = Process(target=foo).start() 
    thread6 = threading.Thread(target=foo2).start()
    child9 = Process(target=foo).start() #푸라는 애를 만들거고.바로실행해
    child10 = Process(target=foo).start()
    thread7 = threading.Thread(target=foo2).start() 
    child11 = Process(target=foo).start() 
    thread8 = threading.Thread(target=foo2).start()
# print('hello os')
# print('my pid is', os.getpid())
text = "hello hell hello"
a = text.count("l")
print(f'count char{a}')

b = text.count("hell")
print(f'count str{b}')

c = text.find("el")
print(f'find{c}')

d = text.find("world")
print(f'find not in here: {d}')

try:
    e = text.index("world")
    print(f'index not in here: {e}')
except ValueError:
    print("ValueError")

text_list = ["chungju", "Suwon", "Seoul"]
new_text = " is Good city. "
joined_text = new_text.join(text_list)
print(f'join other string {joined_text}')
joined_text2 = "".join(text_list)
print(f'join "" {joined_text2}')

replaced_text = text.replace("hell", "heaven")
print(f'replace {replaced_text}')
# replaced_text_list = text_list.replace("u","r")
# print(f'replace list char {replaced_text_list}')

text_listed = text.split(" ")
print(f'split {text_listed}')

text_len = len(text)
print(f'len {text_len}')

numbers = [1,2,3,4,5]
del numbers[2]
numbers.remove(2)
print(f'del and remove {numbers}')

numbers.append(6)
print(f'append {numbers}')

numbers.sort(reverse=True)
print(f'reverse sort {numbers}')
new_numbers = sorted(numbers)
print(f'sorted {new_numbers}')
numbers.sort()
print(f'sort {numbers}')

numbers.reverse()
print(f'reverse {numbers}')

num_index = numbers.index(6)
print(f'index {num_index}')

numbers.insert(3, 100)
print(f'insert {numbers}')

num_poped = numbers.pop()
print(f'pop() {num_poped}')
num_poped = numbers.pop(2)
print(f'pop(2) {num_poped}')

numbers.append(100)
num_count = numbers.count(100)
print(f'count 100 {num_count}')

new_numbers = [1,5,4,1]
numbers.extend(new_numbers)
print(f'extend {numbers}')
numbers = numbers + new_numbers
print(f'+ {numbers}')

dict = {}
dict["hello"] = "World"
print(f'add pair{dict}')

del dict["hello"]
print(f'del{dict}')

dict["hello"] = "World"
dict_element = dict['hello']
print(f'get value {dict_element}')

dict["hello2"] = "World2"
dict["hello3"] = "World3"
keys_list = dict.keys()
print(f'keys {keys_list}')
values_list = dict.values()
print(f'values {values_list}')
items_list = dict.items()
print(f'items {items_list}')

dict.clear()
print(f'clear {dict}')

dict["hello2"] = "World2"
dict["hello3"] = "World3"
print(f'in key {"hello2" in dict}')
print(f'in value {"World2" in dict}')

print(f'in list {100 in numbers}')