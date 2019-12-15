const Discord = require('discord.js')
const simple = require('../libs/embed')
const ms = require('ms');

module.exports.run = async (client, message, args, isOwner) => {

    let reminderTime = args[0]; 
    if (!reminderTime) {
        return("Please use the correct syntax: `_remind <# follwed by s, m, h, d, w, m, y> <reminder>. Example: `_remind 5m homework`.")
    }
    reminderTime = reminderTime.trim()
    let reminder = args.slice(1).join(" "); 

    if (/^[0-9]{1,3}[smhdwy]$/i.test(reminderTime)) {
        return simple.embed(`In ${reminderTime}, i will remind you:` + '```' + `${reminder}` + '```', message),


        setTimeout(function() {
            return message.author.send(new Discord.RichEmbed()
            .setAuthor('Im reminding you:')
            .setDescription('```' + reminder + '```' + `
            ` + `**-Please don't reply to this message. It will open a modmail thread with staff.-**`)
            .setColor('RANDOM')
            .setTimestamp()
            .setFooter(`Requested By: ${message.author.tag}`, message.author.avatarURL)
        )}, ms(reminderTime));
    }
    else message.channel.send("Please use the correct syntax: `_remind <# s, m, h, d, w, m, or y> <reminder>``` For example: `_remind 5m homework`.")

}
module.exports.help = {
    name: 'remind',
    description: 'Sets a reminder.',
    permissions: undefined
}