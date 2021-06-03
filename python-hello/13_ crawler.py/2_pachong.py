from urllib import request

# url = 'http://www.baidu.com'
# response = request.urlopen(url, timeout=1)
# print(response.read().decode('utf-8'))

# GET、POST

data = bytes(parse.urlencode({'world':'hello'}), encoding='utf-8')