import subprocess
import sys


def main():
    print("Logs from your program will appear here!")

    command = sys.argv[3]
    args = sys.argv[4:]

    completed_process = subprocess.run([command, *args], capture_output=True)
    sys.stdout.write(completed_process.stdout.decode("utf-8"))
    sys.stderr.write(completed_process.stderr.decode("utf-8"))


if __name__ == "__main__":
    main()
