# import sys
# def write_hello(file_path):
#     file = open(file_path, 'w+',encoding='utf-8')
#     file.write("Hello World")
#     file.close()
# if __name__ == '__main__':
#     write_hello(sys.argv[1])
# def use_create():
#     f = open("learning question","w+",encoding="utf-8")
#     f.write("今天天气真好\n")
#     f.write("可以一起约会吗")
#     f.close()
# if __name__ == '__main__':
#     use_create()
import re
def my_cmp():
    names = ["name1","_name","2_name","__name__"]
    for name in names:
        ret = re.match("[a-zA-Z_]",name)
        if ret:
            print(f'{name}是正确的')
        else:
            print(f'{name}是错误的')

if __name__ == '__main__':
    my_cmp()