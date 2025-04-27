import os
import glob
import shutil
import sys

from textnode import TextNode, TextType
from inline_markdown import split_nodes_delimiter, extract_markdown_images
from block_markdown import markdown_to_blocks
from copy_static import copy_files_recursive
from generate_page import generate_page, generate_page_recursive

public_path = 'docs'
static_path = 'static'

def generate_public_directory():
    files = os.scandir(public_path)
    for file in files:
        if file.is_dir():
            shutil.rmtree(f"{public_path}/{file.name}")
        else:
            os.remove(f"{public_path}/{file.name}")

    static_files = os.scandir(static_path)

    for static_entry in static_files:
        if static_entry.is_dir():
            shutil.copytree(f"{static_path}/{static_entry.name}", f"{public_path}/{static_entry.name}")
        else:
            shutil.copy2(f"{static_path}/{static_entry.name}", f"{public_path}/{static_entry.name}")

def copy_static():
    print("Deleting public directory...")
    if os.path.exists(public_path):
        shutil.rmtree(public_path)

    print("Copying static files to public directory...")
    copy_files_recursive(static_path, public_path)


def main():
    # textnode = TextNode('war changed me!', TextType.LINK, 'https://www.toptenz.net/top-10-badass-yet-forgotten-ancient-warriors-through-history.php')
    # # print(textnode)

    # node = TextNode("This is text with a `code block` word", TextType.TEXT)
    # new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    # # print(new_nodes)

    # img = extract_markdown_images("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)")
    # # print(img)

    # md = """
    # This is **bolded** paragraph

    # This is another paragraph with _italic_ text and `code` here
    # This is the same paragraph on a new line

    # - This is a list
    # - with items
    # """
    # blocks = markdown_to_blocks(md)
    # print(blocks)

    base_path = sys.argv[1] if len(sys.argv) == 2 else '/'
    generate_public_directory()
    generate_page_recursive('content', 'template.html', 'docs', base_path)
    # generate_page('content/index.md', 'template.html', 'public/index.html')

main()