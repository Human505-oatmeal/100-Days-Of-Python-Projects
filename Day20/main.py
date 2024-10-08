import discord, datetime

client = discord.Client()
user_join_times = {}
match_and_replace = {
    396915157948956672: "e-dgy",
    505974446914535426: "Socialize",
    219564597349318656: "ChillZone",
    727649662475173962: "Mika",
    319560327719026709: "Dadscord",
    394854570926407682: "ChillBar"
}


@client.event
async def on_ready():
    print(f"Logged in as {client.user}")


@client.event
async def on_voice_state_update(member, before, after):
    def check_device():
        if member.is_on_mobile():
            return "Mobile"
        else:
            return "PC?"

    guild_name = match_and_replace.get(member.guild.id, member.guild.name)

    # User joins a voice channel
    if before.channel is None and after.channel is not None:
        join_time = datetime.datetime.now()
        user_join_times[member.id] = join_time
        members_names = [m.display_name for m in after.channel.members if m.id != 745073145903448196]
        print(f"User ID: {member.id}\tDisplay Name: {member.display_name}\tJoin Date: {str(join_time).split('.')[0]}\tJoined Server: {guild_name}\tJoined Channel: {after.channel.name}\tUsers in channel: {', '.join(members_names)}\tMobile/PC: {check_device()}")

    # User leaves a voice channel
    elif before.channel is not None and after.channel is None:
        leave_time = datetime.datetime.now()
        join_time = user_join_times.get(member.id)

        if join_time:
            duration = leave_time - join_time
            duration_in_seconds = int(duration.total_seconds())
            hours, remainder = divmod(duration_in_seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            duration_str = f"{hours}h {minutes}m {seconds}s" if hours else f"{minutes}m {seconds}s"
        else:
            duration_str = "Unknown"

        members_names = [m.display_name for m in before.channel.members if m.id != 745073145903448196]
import discord, datetime

client = discord.Client()
user_join_times = {}
match_and_replace = {
    396915157948956672: "e-dgy",
    505974446914535426: "Socialize",
    219564597349318656: "ChillZone",
    727649662475173962: "Mika",
    319560327719026709: "Dadscord",
    394854570926407682: "ChillBar"
}


@client.event
async def on_ready():
    print(f"Logged in as {client.user}")


@client.event
async def on_voice_state_update(member, before, after):
    def check_device():
        if member.is_on_mobile():
            return "Mobile"
        else:
            return "PC?"

    guild_name = match_and_replace.get(member.guild.id, member.guild.name)

    # User joins a voice channel
    if before.channel is None and after.channel is not None:
        join_time = datetime.datetime.now()
        user_join_times[member.id] = join_time
        members_names = [m.display_name for m in after.channel.members if m.id != 745073145903448196]
        print(f"User ID: {member.id}\tDisplay Name: {member.display_name}\tJoin Date: {str(join_time).split('.')[0]}\tJoined Server: {guild_name}\tJoined Channel: {after.channel.name}\tUsers in channel: {', '.join(members_names)}\tMobile/PC: {check_device()}")

    # User leaves a voice channel
    elif before.channel is not None and after.channel is None:
        leave_time = datetime.datetime.now()
        join_time = user_join_times.get(member.id)

        if join_time:
            duration = leave_time - join_time
            duration_in_seconds = int(duration.total_seconds())
            hours, remainder = divmod(duration_in_seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            duration_str = f"{hours}h {minutes}m {seconds}s" if hours else f"{minutes}m {seconds}s"
        else:
            duration_str = "Unknown"

        members_names = [m.display_name for m in before.channel.members if m.id != 745073145903448196]
        print(f"User ID: {member.id}\tDisplay Name: {member.display_name}\tLeft Date: {str(leave_time).split('.')[0]}\tDuration: {duration_str}\tJoined Server: {guild_name}\tJoined Channel: {before.channel.name}\tUsers in channel: {', '.join(members_names)}\tMobile/PC: {check_device()}")

        # Remove the user from the dictionary after they leave
        user_join_times.pop(member.id, None)

    # User switches channels
    elif before.channel is not None and after.channel is not None:
        leave_time = datetime.datetime.now()
        join_time = user_join_times.get(member.id)

        if join_time:
            duration = leave_time - join_time
            duration_in_seconds = int(duration.total_seconds())
            hours, remainder = divmod(duration_in_seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            duration_str = f"{hours}h {minutes}m {seconds}s" if hours else f"{minutes}m {seconds}s"
        else:
            duration_str = "Unknown"

        members_names_before = [m.display_name for m in before.channel.members if m.id != 745073145903448196]
        members_names_after = [m.display_name for m in after.channel.members if m.id != 745073145903448196]

        print(f"User ID: {member.id}\tDisplay Name: {member.display_name}\tSwitched Channels at: {str(leave_time).split('.')[0]}\tDuration: {duration_str}\tMoved from {before.channel.name} to {after.channel.name}\nBefore Channel Users: {', '.join(members_names_before)}\nAfter Channel Users: {', '.join(members_names_after)}")

        # Update the join time for the new channel
        user_join_times[member.id] = leave_time


client.run('TOKEN HERE')
