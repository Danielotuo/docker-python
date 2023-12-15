import subprocess
import sys


def main():
    print("Logs from your program will appear here!")

    command = sys.argv[3]
    args = sys.argv[4:]

    completed_process = subprocess.run(
        [command, *args], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print("stdout:")
    print(completed_process.stdout)

    print("\nstderr:")
    print(completed_process.stderr)


if __name__ == "__main__":
    main()
