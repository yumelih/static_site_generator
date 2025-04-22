from enum import Enum

class TextType(Enum):
    NORMAL_TEXT = 'normal'
    BOLD_TEXT = 'bold'
    ITALIC_TEXT = 'italic'
    CODE_TEXT = 'code'
    LINK_TEXT = 'link'
    IMAGE_TEXT = 'image'

class TextNode():
    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        text_check = self.text == other.text
        text_type_check = self.text_type == other.text_type
        url_check = self.url == other.url
        if text_check and text_type_check and url_check:
            return True
        return False

    def __repr__(self):
        return f"{self.__class__.__name__}({self.text}, {self.text_type.value}, {self.url})"