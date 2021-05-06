import re


def email_parse(text):
    pattern = re.compile(r"(?P<username>.+)@(?P<domain>\w+\.\w{2,3})")
    result = pattern.finditer(text)
    result_ = pattern.match(text)
    #print(result)
    if not result_:
        raise ValueError(f'Email is not correct: {text}')
    for i in result:
        print(i.groupdict())


email_parse("juliojm-1310@hotmail.com")
email_parse("juliojm-1310hotmailcom")