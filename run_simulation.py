"""Launch the simulator from any working directory.

Usage: python /path/to/Traffic-Simulation/run_simulation.py
Install the repository's requirements first. Run as a standalone process:
the legacy simulator loads images relative to the process working directory.
"""

import os
from pathlib import Path
import runpy


def main():
    project_directory = Path(__file__).resolve().parent
    original_directory = Path.cwd()
    try:
        os.chdir(project_directory)
        runpy.run_path(str(project_directory / "simulation.py"), run_name="__main__")
    finally:
        os.chdir(original_directory)


if __name__ == "__main__":
    main()
