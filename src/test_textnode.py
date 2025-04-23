import unittest

from textnode import TextNode, TextType, text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_url_eq(self):
        node = TextNode('Test', TextType.LINK, 'https://warchanged.me')
        node2 = TextNode('Test', TextType.LINK)
        self.assertNotEqual(node, node2)

    def test_text(self):
        node = TextNode('This is a text node', TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, 'This is a text node')

    def test_link(self):
        node = TextNode('This is a link node', TextType.LINK, 'test.com')
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), '<a href="test.com">This is a link node</a>')

    def test_image(self):
        node = TextNode('testing hard', TextType.IMAGE, 'test.com')
        html_node = text_node_to_html_node(node)
        print(html_node.to_html())
        self.assertEqual(html_node.to_html(), '<img src="test.com" alt="testing hard"></img>')

    def test_image_2(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )

    def test_bold(self):
        node = TextNode("This is bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")

if __name__ == '__main__':
    unittest.main()