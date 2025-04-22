from textnode import TextNode, TextType

def main():
    textnode = TextNode('war changed me!', TextType.LINK_TEXT, 'https://www.toptenz.net/top-10-badass-yet-forgotten-ancient-warriors-through-history.php')
    print(textnode)

main()