class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None) :
        self.tag = tag
        self.value = value
        self.children = [] if children is None else children
        self.props = {} if props is None else props
    
    def to_html(self):
         # Start with opening tag
        html = f"<{self.tag}"
    
        # Add attributes if any exist
        if self.props is not None:
            for key, value in self.props.items():
                html += f' {key}="{value}"'

        # Close opening tag
        html += ">"
    
        # Add children's HTML
        if self.children is not None:
            for child in self.children:
                html += child.to_html()
    
        # Add closing tag
        html += f"</{self.tag}>"
    
        return html
    
    def props_to_html(self):
        inline_props=""
        for prop in self.props:
            inline_props = inline_props + f" {prop}=\"{self.props[prop]}\""
        return inline_props
    
    def __repr__(self):
        if not self.props:
            return ""
        else:
            return f"HTMLNode({self.tag}, {self.value}, {len(self.children)}, {self.props})"