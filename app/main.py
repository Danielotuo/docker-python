import subprocess
import sys


def main():

    command = sys.argv[3]
    args = sys.argv[4:]

    completed_process = subprocess.run(
        [command, *args], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print("stdout:")
    print(completed_process.stdout.strip())

    print("\nstderr:")
    print(completed_process.stderr.strip())


if __name__ == "__main__":
    main()
