import os
proxy = 'http://edcguest:edcguest@172.31.102.29:3128/'

os.environ['http_proxy'] = proxy
os.environ['HTTP_PROXY'] = proxy
os.environ['https_proxy'] = proxy
os.environ['HTTPS_PROXY'] = proxy
os.system('conda activate my_env')
os.system('pip install apiclient')
