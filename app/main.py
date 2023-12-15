import subprocess
import sys


def main():

    command = sys.argv[3]
    args = sys.argv[4:]

    completed_process = subprocess.run(
        [command, *args], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print(completed_process.stdout.strip())

    stderr_output = completed_process.stderr.strip()
    if stderr_output:
        print(stderr_output)


if __name__ == "__main__":
    main()
