from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    TEXT = 'text'
    BOLD = 'bold'
    ITALIC = 'italic'
    CODE = 'code'
    LINK = 'link'
    IMAGE = 'image'

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
    
def text_node_to_html_node(text_node):
    # if not text_node.text_type:
    #     raise ValueError("This text type doesn't exist.")
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode('b', text_node.text)
        case TextType.ITALIC:
            return LeafNode('i', text_node.text)
        case TextType.CODE:
            return LeafNode('code', text_node.text)
        case TextType.LINK:
            return LeafNode('a', text_node.text, {
                "href": text_node.url
            })
        case TextType.IMAGE:
            return LeafNode('img', '', {
                "src": text_node.url,
                "alt": text_node.text
            })
        case _:
            raise ValueError("This text type doesn't exist.")


