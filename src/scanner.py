def scan_dependencies(ecosystem: str, file: str, max_depth: int) -> list:
    
    file_content = open(file)

    content = file_content.readlines()

    print(content)

   
    return



def generate_spdx(dependencies: list, ecosystem: str, project_dir: str) -> dict:

    return