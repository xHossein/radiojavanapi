import re

def url_to_id(url: str) -> str:
    return re.findall(
            r'.*[video|mp3|song|podcast|artist|story|preview|u]/([\d\w\-_()+\.]+)',url)[0]

def to_int(string: str) -> int:
    return int(string.replace(',','').replace('+',''))

def extract_cookie(string: str) -> str:
    return re.findall(r'(_rj_web=.*?;)', string)[0]