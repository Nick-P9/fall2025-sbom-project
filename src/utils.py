
import os

ecosystem_files = {

        'python' : ['pyproject.toml', 'requirements.txt', 'Pipfile', 'setup.py'], 
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


def detectFile(project_directory: str) -> str:
     
     for eco in ecosystem_files:
        key = ecosystem_files[eco]

        for file in key:
            full_path = project_directory + file
            
            if os.path.isfile(full_path):
                print('File found:', file)
                return file
                
        raise ValueError



def detectEcosystem (project_directory: str) -> str:
    #project_dir = '/Users/nick/fall2025-sbom-project/tests/'

 

    for eco in ecosystem_files:
        key = ecosystem_files[eco]

        for file in key:
            full_path = project_directory + file
            
            if os.path.isfile(full_path):
                print('Ecosystem found:', eco)
                return eco
                
    raise ValueError





if __name__ == "__main__":
    detectEcosystem()
