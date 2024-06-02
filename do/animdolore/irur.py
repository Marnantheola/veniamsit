    # Get all guilds that the bot is a member of.
    guilds = bot.guilds
    for guild in guilds:
        # Add the guild to the list of guilds.
        remainder.extend(list(guild.members))  
