import argparse

def main():
    parser = argparse.ArgumentParser(description="Custom SBoM Scanner")
    parser.add_argument("project_dir", help="Project directory to scan")
    parser.add_argument("--ecosystem", choices=["python"], default="python", help="Ecosystem to scan (e.g., python)")
    parser.add_argument("--max-depth", type=int, default=0, help="Max dependency depth (0 for unlimited)")
    args = parser.parse_args()
    print(f"Scanning {args.project_dir} for {args.ecosystem} with depth {args.max_depth}")

if __name__ == "__main__":
    main()