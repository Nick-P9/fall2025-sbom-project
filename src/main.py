import argparse
from utils import detectEcosystem

def main():
    parser = argparse.ArgumentParser(description="Custom SBoM Scanner")
    parser.add_argument("project_dir", help="Project directory to scan")
    #parser.add_argument("--ecosystem", choices=["python"], default="python", help="Ecosystem to scan (e.g., python)")
    parser.add_argument("--max-depth", type=int, default=0, help="Max dependency depth (0 for unlimited)")
    args = parser.parse_args()


    project_directory = args.project_dir
    
    max_depth = args.max_depth

    print(f"Scanning {args.project_dir}")

    try: 
        detectEcosystem(project_directory)

    except ValueError:
        print("No supported file found")






    

if __name__ == "__main__":
    main()