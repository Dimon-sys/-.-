from re import *

pattern = compile(
    r'(?P<http>http://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})|'
    r'(?P<ftp>ftp://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})|'
    r'(?P<email>[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})'
)

def replace_with_links(text):
    def replacer(match):
        if match.group('http'):
            url = match.group('http')
            return f'<a href="{url}">{url}</a>'
        elif match.group('ftp'):
            url = match.group('ftp')
            return f'<a href="{url}">{url}</a>'
        elif match.group('email'):
            email = match.group('email')
            return f'<a href="mailto:{email}">{email}</a>'
        return match.group(0) 

    return pattern.sub(replacer, text)

def read_file(file_name):
    with open(file_name, encoding='utf-8') as file:
        for line in file:
            yield line 

for line in read_file('2.txt'):
    print(replace_with_links(line), end='')