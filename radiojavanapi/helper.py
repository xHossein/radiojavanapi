import re

def url_to_id(url: str) -> str:
    return re.findall(
            r'.*[video|mp3|podcast|artist|story|u]/([\d\w\-_()+]+)',url)[0]

def to_int(string: str) -> int:
    return int(string.replace(',','').replace('+',''))