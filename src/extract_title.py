def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            line = line[2:].strip()
            return line
    raise Exception("You need a title")
        
