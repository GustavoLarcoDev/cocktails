import os
import subprocess

def run_command(command):
    """Run a shell command and print the output."""
    result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print(result.stdout)
    if result.stderr:
        print(result.stderr)

def main():
    print("Applying database migrations...")
    run_command("python manage.py migrate")

    print("Collecting static files...")
    run_command("python manage.py collectstatic --noinput")

    print("Compiling translation files (if any)...")
    run_command("python manage.py compilemessages")

    print("Running tests...")
    run_command("python manage.py test")

    print("Checking deployment configuration...")
    run_command("python manage.py check --deploy")

if __name__ == "__main__":
    main()
