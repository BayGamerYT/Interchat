import json
import main


async def store_guild(guild):
    servers = main.get_servers()

    if str(guild.id) in servers:
        return

    servers[str(guild.id)] = {}
    servers[str(guild.id)]['channel'] = 1

    with open('data/servers.json', 'w', encoding='utf-8') as f:
        json.dump(servers, f, indent=4)

async def delete_guild(guild):
    servers = main.get_servers()

    if str(guild.id) not in servers:
        return

    del servers[str(guild.id)]

    with open('data/servers.json', 'w', encoding='utf-8') as f:
        json.dump(servers, f, indent=4)