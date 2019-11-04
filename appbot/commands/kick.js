const Discord = require('discord.js')

module.exports.run = async (client, message, args, isOwner) => {
    try {
    if (message.member.hasPermission("KICK_MEMBERS", {checkAdmin: true, checkOwners: true})) {
        let member = message.guild.member(message.mentions.users.first()) || args[0]
        let kickReason = args.slice(1).join(" ")
        let guildOwner = message.guild.owner.id
        if(!args[0]) return simple.embed("You must enter a user to kick!", message)
        let errorLogs = client.channels.get('ERROR_LOGS')
        if (!message.guild.me.hasPermission("KICK_MEMBERS", {checkAdmin: true, checkOwner: true})) return simple.embed("I dont have sufficiant permissions to run this command! Please make sure i have the `KICK_MEMBERS` permission, and i have a role higher than the use you are trying to kick!", message)
        if (!member.id) return simple.embed('You Must Enter A Valid User To Kick!', message)
        if (member.id === message.member.id) return simple.embed("You cannot kick yourself!", message)
        if (message.guild.me.roles.highest.comparePositionTo(member.roles.highest) < 1) return simple.embed("You cannot ban a user that has a higher role than Retr0n!", message)
        if (message.member.id !== guildOwner && message.member.roles.highest.comparePositionTo(member.roles.highest)  < 1) return simple.embed("You cannot kick a user with equal or higher permissions!", message)
        if (!kickReason) kickReason = 'None Provided'
        if (member.id === guildOwner) return simple.embed("You cannot kick the guild owner!", message)
        member.send(new Discord.RichEmbed()
        .setColor(0x36393E)
        .setAuthor("User Kicked!")
        .setTimestamp()
        .setFooter(message.author.tag)
        .setDescription(`Moderator: **${message.author.tag} (${message.author.id})** has kicked you from Guild: **${message.guild.name} (${message.guild.id})** for Reason: **${kickReason}**!`)
        )     

        member.kick(`Command "KICK" executed by: ${message.author.tag} (${message.author.id}) with reason: ${kickReason}`).then(() => {
            return message.channel.send(new Discord.RichEmbed()
            .setAuthor('User Kicked!', 'https://cdn.discordapp.com/attachments/577942049370800128/608803824697868299/emoji.png')
            .setDescription(`<a:check:567452249555730445> User: ${member} has successfully been kicked by Moderator: ${message.author.toString()} with Reason: **${kickReason}**`)
            .setColor(0x36393E)
            .setTimestamp()
            .setFooter(message.author.tag))
        })
        .catch(error => message.reply(`Make sure the member you entered is a valid @mention or valid User ID!`).then(errorLogs.send(`An error occured in guild: **${message.guild.name}** (${message.guild.id}) with command: \`kick\` \n \`\`\`${error}\`\`\``))
            )
    }
    else return simple.embed('You Must Have the `KICK_MEMBERS` Permission To Use This Command!', message)
}

catch (error) {
    return ("The user you are trying to ban must be below my role!", message)
}
module.exports.help = {
    name: 'kick',
    description: 'Kicks A Member',
}
