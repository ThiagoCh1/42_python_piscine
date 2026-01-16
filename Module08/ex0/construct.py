import sys
import os
import site


def main() -> None:
    try:
        if sys.prefix != sys.base_prefix:
            print("MATRIX STATUS: Welcome to the construct")
            print(f"Current Python: {sys.executable}")

            env_name = os.path.basename(sys.prefix)
            print(f"Virtual Environment: {env_name}")
            print(f"Environment Path: {sys.prefix}")

            print("SUCCESS: You're in an isolated environment!")
            print("Safe to install packages without "
                  "affecting the global system.")

            site_packages = site.getsitepackages()
            package_path = site_packages[0] if site_packages else "Unknown"
            print(f"Package installation path:\n{package_path}")

        else:
            print("MATRIX STATUS: You're still plugged in")
            print(f"Current Python: {sys.executable}")
            print("Virtual Environment: None detected")
            print("WARNING: You're in the global environment!")
            print("The machines can see everything you install.")
            print("To enter the construct, run:")
            print("python -m venv matrix_env")
            print("source matrix_env/bin/activate")
            print("matrix_env\\Scripts\\activate")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
