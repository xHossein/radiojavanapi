import re

def url_to_id(url:str) -> str:
    return re.findall(
            r'.*[video|mp3|podcast|artist|story]/([\d\w\-_+]+)',url)[0]

def toInt(string:str) -> int:
    for i in [',','+']:
        string = string.replace(i,'')
    return int(string)
            
