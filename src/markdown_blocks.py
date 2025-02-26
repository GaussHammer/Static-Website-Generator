from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADER = "header"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "unordered_list"
    OLIST = "ordered_list"

def markdown_to_blocks(markdown):
    markdown_list = []
    split_markdown = markdown.split("\n\n")
    for line in split_markdown:
        if line != "":
            markdown_list.append(line.strip())
    return markdown_list

def is_ordered_list_item(line, expected_number):
    expected = f"{expected_number}. "
    return line.startswith(expected)

def block_to_block_type(block):
    count_headers = 0
    count_code_before = 0
    count_code_after = 0
    lines = block.split("\n")
    is_ordered = True
    for char in block:
        if char == '#':
            count_headers += 1
        elif char == '`':
            count_code_before += 1
        else:
            break
    for i, line in enumerate(lines, start=1):
        if not is_ordered_list_item(line, i):
            is_ordered = False
            break
    if all(line.startswith('>') for line in lines):
        blocktype = BlockType.QUOTE
    elif count_headers >= 1 and count_headers <= 6 and block[count_headers] == " ": 
        blocktype = BlockType.HEADER
    elif count_code_before == 3:
        for char in reversed(block):
            if char == '`':
                count_code_after += 1
            else:
                break
        if count_code_after == count_code_before:
            blocktype = BlockType.CODE
    elif all(line.startswith('* ') or line.startswith('- ') for line in lines):
        blocktype = BlockType.ULIST
    elif is_ordered == True:
        blocktype = BlockType.OLIST
    else:
        blocktype = BlockType.PARAGRAPH
            
    return blocktype

