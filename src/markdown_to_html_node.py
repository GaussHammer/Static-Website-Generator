from markdown_blocks import *
from splitnode_utils import *
from parentnode import *
from textnode import *

def markdown_to_html_node(markdown):
    parent = HTMLNode("div",None,[],None)
    markdown_blocks = markdown_to_blocks(markdown)
    for block in markdown_blocks:
        if block_to_block_type(block).value == "paragraph":
            text_child_node = HTMLNode("p",None,[],{})
            block = block.replace("\n", " ").strip()
            textnodes = text_to_textnodes(block)
            for text in textnodes:
                text_html_text = text_node_to_html_node(text)                    
                text_child_node.children.append(text_html_text)
            parent.children.append(text_child_node)
        elif block_to_block_type(block).value == "header":
            header_counter = 0
            for i in range(len(block)):
                if block[i] == "#":
                    header_counter += 1
            header_child_node = HTMLNode(f"h{header_counter}", None, [], None)
            header_text = block[header_counter:].strip()
            header_text_nodes = text_to_textnodes(header_text)
            for text in header_text_nodes:
                html_header_text = text_node_to_html_node(text)
                header_child_node.children.append(html_header_text)
            parent.children.append(header_child_node)
        elif block_to_block_type(block).value == "code":
            pre = HTMLNode("pre", None, [], None)
            code = HTMLNode("code", None,[], None)
            code_text = block.replace("`", "").strip()
            code_textnode = TextNode(code_text, TextType.TEXT)
            code_html = text_node_to_html_node(code_textnode)
            code.children.append(code_html)
            pre.children.append(code)
            parent.children.append(pre)
        elif block_to_block_type(block).value == "quote":
            quote_child_node = HTMLNode("blockquote", None, [], None)
            block = block.replace("\n", " ").strip()
            quote_text = block.replace(">","").strip()
            quote_text = " ".join(quote_text.split())
            quote_text = quote_text.replace(" --", "  --")
            quote_text_nodes = text_to_textnodes(quote_text)
            for text in quote_text_nodes:
                quote_html_text = text_node_to_html_node(text)
                quote_child_node.children.append(quote_html_text)
            parent.children.append(quote_child_node)
        elif block_to_block_type(block).value == "unordered_list":
            unordered_list_child_node = HTMLNode("ul", None, [], None)
            unordered_lines = block.split("\n")
            for line in unordered_lines:
                ul_li_node = HTMLNode("li", None, [], None)
                ul_stripped = line.strip()
                ul_text = ul_stripped[1:].strip()
                ul_text_to_text_nodes = text_to_textnodes(ul_text)
                for node in ul_text_to_text_nodes:
                    ul_html = text_node_to_html_node(node)
                    ul_li_node.children.append(ul_html)
                unordered_list_child_node.children.append(ul_li_node)
            parent.children.append(unordered_list_child_node)
        elif block_to_block_type(block).value == "ordered_list":
            ordered_list_child_node = HTMLNode("ol", None, [], None)
            ordered_lines = block.split("\n")
            for line in ordered_lines:
                ol_li_node = HTMLNode("li", None, [], None)
                ol_stripped = line.strip()
                period_pos = ol_stripped.find(".")
                ol_text = ol_stripped[period_pos + 1:].strip()
                ol_text_to_text_nodes = text_to_textnodes(ol_text)
                for node in ol_text_to_text_nodes:
                    ol_html = text_node_to_html_node(node)
                    ol_li_node.children.append(ol_html)
                ordered_list_child_node.children.append(ol_li_node)
            parent.children.append(ordered_list_child_node)
    return parent