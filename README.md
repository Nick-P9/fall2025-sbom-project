# Fall 2025 SBoM Project

A custom Software Bill of Materials (SBoM) scanner for generating hierarchical SBoMs in CycloneDX format, analyzing 500 OSS projects, and clustering results.

## Setup
### Using Python venv (Recommended for Most Users)
1. Clone: `git clone https://github.com/Nick-P9/fall2025-sbom-project.git`
2. Navigate: `cd fall2025-sbom-project`
3. Create virtual env: `python -m venv venv`
4. Activate:
   - Unix/macOS: `source venv/bin/activate`
   - Windows: `venv\Scripts\activate`
5. Install deps: `pip install -r requirements.txt`
6. Run: `python src/main.py <project_dir> --ecosystem python --max-depth 0`

### Using Conda (Alternative)
1. Clone: `git clone https://github.com/Nick-P9/fall2025-sbom-project.git`
2. Navigate: `cd fall2025-sbom-project`
3. Create Conda env: `conda create -n sbom python=3.10`
4. Activate: `conda activate sbom`
5. Install deps: `pip install -r requirements.txt`
6. Run: `python src/main.py <project_dir> --ecosystem python --max-depth 0`

## Goals
- Build a scanner for hierarchical SBoMs in CycloneDX format.
- Detect latest versions via APIs.
- Generate a dataset for 500 open-source projects.
- Cluster projects based on update metrics.

