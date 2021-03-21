from flask.cli import AppGroup
from .users import seed_users, undo_users
from .shops import seed_shops, undo_shops
from .coffees import seed_coffees, undo_coffees
from .sips import seed_sips, undo_sips

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')

# Creates the `flask seed all` command

# to seed specific files, comment out any file that has already been seeded


@seed_commands.command('all')
def seed():
    seed_users()
    seed_shops()
    seed_coffees()
    seed_sips()
    # Add other seed functions here

# Creates the `flask seed undo` command


@seed_commands.command('undo')
def undo():
    undo_users()
    undo_shops()
    undo_coffees()
    undo_sips()
    # Add other undo functions here
