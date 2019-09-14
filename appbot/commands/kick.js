const Discord = require('discord.js')

module.exports.run = async (client, message, args, isOwner) => {
    if (isOwner || message.member.hasPermission(this.help.permissions, false, true, true)) {
        var member = message.guild.member(message.mentions.users.first())
        var kickReason = args.slice(1).join(" ")
        if (!member) return message.reply('You Must Enter A Valid user To Kick!')
        if (member.hasPermission('MANAGE_MESSAGES', false, true, true)) return message.reply('You Cannot Kick A Moderator!')
        if (!kickReason) kickReason = 'None Provided'
        member.kick(kickReason).then(() => {
            return message.channel.send(new Discord.RichEmbed()
            .setAuthor('Moderation - User Kicked', 'https://cdn2.iconfinder.com/data/icons/fighter-fighting-attacking-poses/300/fight-005-512.png')
            .setDescription(`__**Performed By:**__ **${message.member.user.tag}**`)
            .addField(`User Kicked: ${member.user.tag}`, `**Reason:** ${kickReason}`)
            .setColor(0xfff600))
        })
            .catch(error => {
                message.channel.send(`There Was An Error Kicking This User: ${error}`)
            })
    }
    else return message.reply('You Must Have `' + this.help.permissions + '` Permission To Use This Command!')
}

module.exports.help = {
    name: 'kick',
    description: 'Kicks A Member',
}