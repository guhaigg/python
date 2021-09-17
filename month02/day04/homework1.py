import  re
def datainet():
    while True:
        data =''
        inet = open("inet.log",'r')
        for line in inet:
            if line == "\n":
                break
            data += line
            if data:
                yield data
            else:
                return
def main():
        connector = input('请输入一个接口名称')
        for
        data = inet.read()
        result = re.search("",'').group()
        print(f'您输入的接口名称{connector}对应的address是{result}')
