from markdown_to_html_node import *
from extract_title import *
import os

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as content:
        content_text = content.read()
        title = extract_title(content_text)
        html_node_content = markdown_to_html_node(content_text)
        html_content = html_node_content.to_html()
    
    with open(template_path) as template:
        template_text = template.read()
        template_text = template_text.replace("{{ Title }}", title)
        template_text = template_text.replace("{{ Content }}", html_content)

    directory = os.path.dirname(dest_path)
    os.makedirs(directory, exist_ok=True)

    with open(dest_path, "w") as html:
        html.write(template_text)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    path_content = os.listdir(dir_path_content)
    for content in path_content:
        content = os.path.join(dir_path_content, content)
        if os.path.isfile(content):
            if not content.endswith('.md'):
                continue
            with open(content) as md_content:
                content_text = md_content.read()
                title = extract_title(content_text)
                html_node_content = markdown_to_html_node(content_text)
                html_content = html_node_content.to_html()
            
            with open(template_path) as template:
                template_text = template.read()
                template_text = template_text.replace("{{ Title }}", title)
                template_text = template_text.replace("{{ Content }}", html_content)
                template_text = template_text.replace("href=\"/", f"href=\"{basepath}")
                template_text = template_text.replace("src=\"/", f"src=\"{basepath}")

            rel_path = os.path.relpath(content, dir_path_content)
            html_path = rel_path.replace('.md', '.html')
            final_path = os.path.join(dest_dir_path, html_path)
            directory = os.path.dirname(final_path)
            os.makedirs(directory, exist_ok=True)

            with open(final_path, "w") as html:
                html.write(template_text)
        elif os.path.isdir(content):
            rel_path = os.path.relpath(content, dir_path_content)
            final_path = os.path.join(dest_dir_path, rel_path)
            generate_pages_recursive(content, template_path, final_path, basepath)
