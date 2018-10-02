import itchat

itchat.auto_login(hotReload=True)

the_str = ("oh，我的璨璨，起床了吗？下面让你见识一下我的微信轰炸功能，和我一起念：国过郭裹果锅哒，郭锅国锅锅锅哒，恭喜你下蛋成功！！！")
for i in range(len(the_str)):
    the_chr = the_str[i]
    itchat.send(the_chr, toUserName='@7c500aebd3ab3fd1ca0021aea9d963b7')
# account = itchat.get_friends('joyzcan')
# print(account)
