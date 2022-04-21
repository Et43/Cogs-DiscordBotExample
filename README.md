OUTDATED BUT COGS SYSTEM IS STILL VALID

# Cogs-DiscordBotExample
## Simple Base Function Bot that runs on cogs.

### File Structure
> src/.

> |-- bot.py

> |-- databse.db.

> |-- cogs/.

> |----__init__.py.

> |----kick.py.

> |----ban.py.

> |----setup.py [ Commands that show how to setup and use databases with commands in discord ].

> |----me.py [ Example of owner only commands ].

> |----automod.py [ Example of a autmod ].

> |----mute.py.

> |----report.py [ Example of a basic report command, that kinda broke since the new discord api update ].

> |----say.py [ Super basic example of how a cog is setup ].

> |----warn.py [ Basic warning system ].

> |---- manager/.

> |------__init__.py.

> |------databaseManager.py [ Custom library i wrote that handles the sql queries for the bot ].


### Functions

#### Moderation:
- Ban
- Kick
- Mute
- Warn
- Report

#### Server Management:
- Setup command
- Logging
- Autmod

#### Storage:
- SQL Sytem for storing server details

#### Random:
- Say
- Bot Onwer only commands

### NOTE
The sql system is set up in a stupid way, so there migth be seom vulnerabilities in the way queries are handled which I could care less to fix.
