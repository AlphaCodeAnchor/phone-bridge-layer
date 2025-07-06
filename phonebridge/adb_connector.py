import subprocess
import os

def run_adb_query(uri: str) -> str:
    # Get the directory of the current file
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct path to adb.exe (one level up + platform-tools folder)
    adb_path = os.path.join(current_dir, "..", "platform-tools", "adb.exe")
    adb_path = os.path.abspath(adb_path)  # normalize path

    try:
        result = subprocess.run(
            [adb_path, 'shell', f'content query --uri {uri}'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding='utf-8',
            errors='ignore'
        )

        if result.returncode != 0:
            raise RuntimeError(f"ADB Error: {result.stderr.strip()}")

        return result.stdout.strip()

    except Exception as e:
        raise RuntimeError(f"Failed to run ADB query: {e}")
