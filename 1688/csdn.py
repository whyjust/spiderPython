import json

def get_ip_port(dict):
    pass


def process_ip_port(ip_port):
    print(json.loads(ip_port,encoding='utf-8'),type(json.loads(ip_port)))
    # for i in list(ip_port):
    #     print(i)




if __name__ == '__main__':
    with open('1.txt','r',encoding='utf-8',errors='ignore') as fp:
        ip_port = fp.read()
        ipDict = process_ip_port(ip_port)
        get_ip_port(ipDict)