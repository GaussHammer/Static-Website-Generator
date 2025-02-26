from htmlnode import HTMLNode
from leafnode import LeafNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("the parent node must have a tag")
        elif self.children == None or self.children == []:
            raise ValueError("the parent class needs children")
        else:
            parent_node = f"<{self.tag}{self.props_to_html()}>"
            for child in self.children:
                new_node = child.to_html()
                parent_node = parent_node + new_node
            parent_node = parent_node + f"</{self.tag}>"
            return parent_node
