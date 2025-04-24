from textnode import TextNode, TextType
from inline_markdown import split_nodes_delimiter, extract_markdown_images
from block_markdown import markdown_to_blocks

def main():
    textnode = TextNode('war changed me!', TextType.LINK, 'https://www.toptenz.net/top-10-badass-yet-forgotten-ancient-warriors-through-history.php')
    # print(textnode)

    node = TextNode("This is text with a `code block` word", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    # print(new_nodes)

    img = extract_markdown_images("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)")
    # print(img)

    md = """
    This is **bolded** paragraph

    This is another paragraph with _italic_ text and `code` here
    This is the same paragraph on a new line

    - This is a list
    - with items
    """
    blocks = markdown_to_blocks(md)
    print(blocks)

main()