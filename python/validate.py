import re

class Validate_process(object):
    
    @staticmethod
    def val_strip_cap_text(text):
        text = text.rstrip(' ').lstrip(' ').lower()
        text = ' '.join(map(str.capitalize, [i for i in text.split(' ') if i]))
        return text

    @staticmethod
    def val_strip_lower_text(text):
        text = text.rstrip(' ').lstrip(' ').lower()
        text = ' '.join([i for i in text.split(' ') if i])
        return text

    @staticmethod
    def strip_text(text):
        text = text.rstrip(' ').lstrip(' ')
        text = ' '.join([i for i in text.split(' ') if i])
        return text

    @staticmethod
    def strip_text_sp(text, t):
        text = text.rstrip(t).lstrip(t)
        return text

    @staticmethod
    def del_spaces_text(text):
        text = text.replace(' ', '')
        return text

    @staticmethod
    def val_no_text(text):
        t = Validate_process.strip_text(text)
        if t == '':
            return None
        return text

    @staticmethod
    def val_integer(text): # year, pages, etc.
        if text=='':
            return None
        try:
            i = int(text)
        except ValueError:
            return -1
        if i<=0:
            return -1
        return i

    @staticmethod
    def val_integer_no_text(text): # year, pages, etc.
        if text=='':
            return -1
        try:
            i = int(text)
        except ValueError:
            return -1
        if i<=0:
            return -1
        return i

    # @staticmethod
    # def 

if __name__ == '__main__':
    # r = Validate_process.val_integer(' 23224 ')
    # print(r, isinstance(r, int))
    # print(r)
    pass