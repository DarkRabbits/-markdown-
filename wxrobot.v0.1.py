import requests

def send_weixin(productnumber, adjustment_content, invlovedcompany, products, schedule):
    url = "将这段文本替换为你群里的机器人webhook地址"  # 群机器人的Webhook地址

    headers = {"Content-Type": "application/json"}  # http数据头，类型为json
    product_list = "\n".join(f"<font color=\"info\">{product.strip()}</font>" for product in products.split("；"))

    # 构建消息内容，动态替换产品数量和调整内容
    data = {
        "msgtype": "markdown",
        "markdown": {
            "content": f"# 现有<font color=\"warning\">**{productnumber}款**</font>产品调整，烦请注意。\n> ## 保司:<font color=\"comment\">**{invlovedcompany}**</font>\n> ## 涉及产品:\n**{product_list}**\n>  ## 调整内容:<font color=\"comment\">{adjustment_content}</font>\n> ## 调整时间：<font color=\"warning\">**{schedule}**</font>\n><@所有人>"
        }
    }

    r = requests.post(url, headers=headers, json=data)  # 利用requests库发送post请求
    return r.status_code, r.text  # 返回状态码和响应内容

# 运行程序时询问用户
productnumber = input("此次产品调整数量")
invlovedcompany = input("哪家保司的？")
products = input("啥产品？（用逗号分隔）")
adjustment_content = input("请输入调整内容：")
schedule = input("调整时间？")

# 调用函数并传入用户输入的值
status_code, response = send_weixin(productnumber, adjustment_content, invlovedcompany,products, schedule)

# 打印响应状态码和内容
print("状态码：", status_code)
print("响应内容：", response)
input('输入任意内容退出')