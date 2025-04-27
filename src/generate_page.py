import os
from block_markdown import markdown_to_html_node, extract_title
from pathlib import Path

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    template_path_text = ''
    with open(from_path) as from_file:
        from_path_text = from_file.read()
        title = extract_title(from_path_text)
        from_path_html = markdown_to_html_node(from_path_text).to_html()
        with open(template_path) as template_file:
            template_path_text = template_file.read()
            template_path_text = template_path_text.replace('{{ Title }}', title)
            template_path_text = template_path_text.replace('{{ Content }}', from_path_html)

    dest_path_splited = dest_path.split("/")
    if len(dest_path_splited) == 0:
        raise Exception("Please provide a valid destination path.")
    for path_index in range(len(dest_path_splited)):
        if path_index + 1 == len(dest_path_splited):
            html_dest_path = dest_path.replace('.md', '.html')
            if os.path.isfile(html_dest_path):
                f = open(html_dest_path, 'w')
                f.write(template_path_text)
                f.close()
            else:
                f = open(html_dest_path, 'x')
                f.write(template_path_text)
                f.close()
            break
        else:
            cur_dest_path = '/'.join(dest_path_splited[0:path_index+1])
            if os.path.isdir(cur_dest_path):
                continue
            else:
                os.mkdir(cur_dest_path)

def generate_page_recursive(dir_path_content, template_path, dest_dir_path):
    dirs = os.listdir(dir_path_content)
    print(dirs)

    if len(dirs) == 0:
        return
    
    for entry in dirs:
        new_dir_path_content = os.path.join(dir_path_content, entry)
        new_dest_dir_path = os.path.join(dest_dir_path, entry)
        print(Path(new_dir_path_content).is_file() and Path(new_dir_path_content).suffix == '.md')
        if Path(new_dir_path_content).is_file() and Path(new_dir_path_content).suffix == '.md':
            generate_page(new_dir_path_content, template_path, new_dest_dir_path)
            continue
        if not os.path.exists(new_dest_dir_path):
            os.mkdir(new_dest_dir_path)
            generate_page_recursive(new_dir_path_content, template_path, new_dest_dir_path)
        
    