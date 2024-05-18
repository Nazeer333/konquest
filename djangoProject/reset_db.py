import os
import subprocess
import shutil

# Define the Django manage.py command
def run_manage_py_command(command):
    result = subprocess.run(['python', 'manage.py'] + command.split(), capture_output=True, text=True)
    return result.stdout, result.stderr

# Remove the SQLite database file if it exists
db_path = 'db.sqlite3'
if os.path.exists(db_path):
    os.remove(db_path)

# Remove the migration files in the taskMgmt/migrations/ directory except for __init__.py
migrations_dir = 'taskMgmt/migrations/'
if os.path.exists(migrations_dir):
    for filename in os.listdir(migrations_dir):
        file_path = os.path.join(migrations_dir, filename)
        if filename != '__init__.py':
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.remove(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)

# Run the Django makemigrations and migrate commands
output_makemigrations, error_makemigrations = run_manage_py_command('makemigrations')
output_migrate, error_migrate = run_manage_py_command('migrate')

# Create a superuser with the given credentials
superuser_command = [
    'createsuperuser',
    '--noinput',
    '--username', 'SuperAdmin',
    '--email', 'superadmin@example.com'
]

# Set the environment variable for the superuser password
os.environ['DJANGO_SUPERUSER_PASSWORD'] = 'WorkPleaseNow#33!'

output_createsuperuser, error_createsuperuser = run_manage_py_command(' '.join(superuser_command))

print("Makemigrations Output:", output_makemigrations)
print("Makemigrations Error:", error_makemigrations)
print("Migrate Output:", output_migrate)
print("Migrate Error:", error_migrate)
print("Createsuperuser Output:", output_createsuperuser)
print("Createsuperuser Error:", error_createsuperuser)