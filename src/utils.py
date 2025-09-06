
import os

def detectEcosystem() -> str:
    project_dir = '/Users/nick/fall2025-sbom-project/tests/'

    ecosystem_files = {

        'python' : ['pyproject.toml', 'requrements.txt', 'Pipfile', 'setup.py'], 
        'nodejs': ['package.json'],
        'maven' : ['pom.xml'],
        'gradle' : ['build.gradle', 'build.gradle.kts'],
        'ruby' : ['Gemfile'],
        'php' : ['composer.json'],
        'dotnet' : ['.csproj', '.fsproj', '.vbproj', 'packages.config'],
        'rust' : ['Cargo.toml'],
        'go' : ['go.mod'],
        #'javascript' : ['package.json'],
        'cpp' : ['CMakeLists.txt', 'vcpkg.json']    
    }


    

    for eco in ecosystem_files:
        key = ecosystem_files[eco]

        for file in key:
            full_path = project_dir + file
            
            if os.path.isfile(full_path):
                print(eco)
                return eco
                
    
    print('No supported file was found')   
    return FileNotFoundError



if __name__ == "__main__":
    detectEcosystem()
