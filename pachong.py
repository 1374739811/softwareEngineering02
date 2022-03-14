
import time

import requests


#爬取方法启动，返回抓包数组信息
def crawlAddress(userAgent,url):
    # 模拟安卓请求
    headers = {
        # 游览器类型
        'User-Agent': userAgent
    }

    url =url
    # 对url地址发送请求
    # 使用抓包工具时就用verify=False
    # resopnse=requests.get(url,headers=headers,verify=False).json()
    # 关闭抓包工具
    resopnse = requests.get(url, headers=headers).json()
    return resopnse


# 价格波动查询
# 每过time秒查询一次,times时间结束查询，商品名称，价格
def inquires(delayTime, times,name,text):
    flag = 1
    print('------------------"' + name + '"的价格波动------------------')
    timing = 0  # 计时
    while (flag):
        print("当前时间是" + time.strftime("%Y-%m-%d %R:%S") + ',价格为' + str(text))
        time.sleep(delayTime)  # 延迟time秒
        timing += 1
        if timing == times:
            flag = 0

#对扑扑的抓包进行显示
def pupu(resopnse):
    # 用[]获取对应的值
    # 商品名name，规格spec，价格text，折扣discount_label，详细内容sub_title
    for products in resopnse['data']['products']:
        spec = products['spec']
        name = products['name']
        sub_title = products['sub_title']
        discount_label = products['discount_label']
        text = products['price'] / 100
        print('----------------商品：' + name + '----------------')
        print('规格：' + spec)

        # 因为有的没折扣，所以用长度判断，要不要在价格后面添加折扣
        if len(discount_label) < 1:
            print('价格：' + str(text))
        else:
            print('价格：' + str(text) + '/' + discount_label)

        print('详细内容：' + sub_title)
        print()
        # 每次延迟1秒，持续时间3秒,商品名称，价格
        inquires(1, 3,name,text)


def main():
    #启动抓包方法(游览器类型，url地址)，并且返回数组信息
    resopnse=crawlAddress('Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat','https://j1.pupuapi.com/client/marketing/storeproduct/v2/search?store_id=deef1dd8-65ee-46bc-9e18-8cf1478a67e9&page=1&size=20&name=&category_id=&sort=0&tag=&brands=&in_stock=-1&is_commend=-1&business=scenes&business_id=130')
    #扑扑的查询方法
    pupu(resopnse)

if __name__ == '__main__':
    main()

