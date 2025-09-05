
import os

def detectEcosystem() -> str:
    project_dir = '/Users/nick/fall2025-sbom-project/tests/'

    ecosystem_files = {

        'python' : ['pytroject.toml', 'requirements.txt', 'Pipfile', 'setup.py'], 
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
            try:
                with open(project_dir + file) as f:
                    print(eco)
                    
            except FileNotFoundError:
                print('scanning')
           
       
            


if __name__ == "__main__":
    detectEcosystem()
