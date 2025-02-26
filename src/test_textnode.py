import unittest

from textnode import TextNode, TextType
from splitnode_utils import *

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
        node3 = TextNode("This is another text node", TextType.BOLD)
        self.assertNotEqual(node,node3)
        node4 = TextNode("This is a text node", TextType.TEXT)
        self.assertNotEqual(node, node4)

    def test_text_node_to_html_node(self):
        link_node = TextNode("test link", TextType.LINK, "https://google.com")
        #print(link_node.text_node_to_html_node().to_html())
        image_node = TextNode("test image",TextType.IMAGE, "../Static/img01.png")
        #print(image_node.text_node_to_html_node().to_html())

    def test_split_node_delimiter(self):
        node = TextNode("test `split` delimiter", TextType.TEXT)
        #print(split_nodes_delimiter([node],"`",TextType.CODE))

    def test_split_node_image(self):
        node = TextNode("This is a test ![image](https://example.com/image.jpg) end.", TextType.TEXT)
        node2 = TextNode("This is a test ! end.", TextType.TEXT)

        #print(split_nodes_image([node]))
        #print(split_nodes_image([node2]))

    def test_split_node_links(self):
        node = TextNode("Here is [link 1](http://example1.com) surrounded by text and [link 2](http://example2.com)", TextType.TEXT)
        #print(split_nodes_link([node]))

    def test_text_to_textnode(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        print(text_to_textnodes(text))


if __name__ == "__main__":
    unittest.main()