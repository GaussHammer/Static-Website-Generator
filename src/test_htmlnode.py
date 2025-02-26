import unittest

from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        html_node = HTMLNode("a","this is a value", None,{"href":"https://google.com","target":"blank"})
        #print(html_node.props_to_html())
    
    def test_leaf_node(self):
        leaf_node = LeafNode("a","this is a leaf node",{"href":"https://google.com","target":"blank"})
        print(leaf_node.to_html())
        leaf_node2 = LeafNode(None, "this is another leaf node")
        print(leaf_node2.to_html())

    def test_parent_node(self):
        parent = ParentNode("div", [LeafNode("p", "hello")])
        parent2 = ParentNode("div", [LeafNode("p", "hello")], {"class": "container"})
        print(parent.to_html())
        print(parent2.to_html())
        nested = ParentNode("div", [ParentNode("p", [LeafNode("span", "hello")])])
        print(nested.to_html())