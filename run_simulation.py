"""Run the traffic simulator from any working directory."""

from pathlib import Path
import runpy


def main():
    script = Path(__file__).resolve().with_name("simulation.py")
    runpy.run_path(str(script), run_name="__main__")


if __name__ == "__main__":
    main()
