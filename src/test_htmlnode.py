import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        html_node = HTMLNode('a', props={"href": "https://www.google.com","target": "_blank"})
        print(html_node)

    def test_props(self):
        html_node = HTMLNode('a', props={"href": "https://www.google.com","target": "_blank"})
        props = html_node.props_to_html()
        self.assertTrue('href=https://www.google.com target=_blank' == props)

    def test_props_2(self):
        html_node = HTMLNode('a', props={"href": "https://www.google.com","target": "_blank"})
        html_node_2 = HTMLNode('a')
        props_1 = html_node.props_to_html()
        props_2 =  html_node_2.props_to_html()

        self.assertNotEqual(props_1, props_2)