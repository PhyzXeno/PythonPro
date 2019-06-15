# 两个位置：
# 1. https://github.com/jhao104/proxy_pool
# 2. https://github.com/ideawu/ssdb
# 1是免费代理地址抓取的python程序，python2，3都支持
# 2是1运行时需要用到的数据库程序，根据上面的说明，我在树莓派上编译了一个出来
# 运行2这个ssdb-server
# 然后到1的Run文件夹运行python3 main.py
# 之后就可以到这个服务器的5010端口要代理服务器的地址了，比如"http://192.168.1.8:5010/get/"，这个网页就会显示一个代理服务器地址
# 然后在本脚本中有相应的简单使用方法




import requests

def get_proxy():
    return requests.get("http://192.168.1.8:5010/get/").content

def delete_proxy(proxy):
    requests.get("http://192.168.1.8:5010/delete/?proxy={}".format(proxy))

# your spider code

def getHtml():
    # ....
    retry_count = 5
    proxy = get_proxy()
    while retry_count > 0:
        try:
            html = requests.get('http://ip4.me', proxies={"http": "http://{}".format(proxy)})
            # 使用代理访问
            return html
        except Exception:
            retry_count -= 1
    # 出错5次, 删除代理池中代理
    delete_proxy(proxy)
    return None

def req():
    proxy = get_proxy()
    proxy = str(proxy)[2:-1]
    print(proxy)
    # print(type(str(proxy)))
    r = requests.get('http://ip4.me', proxies={"http": "http://{}".format(proxy)})
    print(r.content)

req()