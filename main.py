import os
from flask import Flask, request, make_response, redirect

app = Flask(__name__)

if os.environ.get('_ENV'):
    ENV = os.environ.get('_ENV')
else:
    ENV = "LOCAL"

print(f"ENV: {ENV}")

instance = create_app(ENV)
manager_commands = Manage(instance)
manager_commands.add_command('db',MigrateCommand)
schedule = StatusService(instance, check_seg=120)


if __name__ == '__main__':
    manager_commands.run()
    #app.run(port = 5000, debug = True)