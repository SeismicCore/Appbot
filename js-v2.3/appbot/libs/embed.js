const Discord = require('discord.js')
exports.embed = (text, messsage)=>{
    msg = messsage
    msg.channel.send(new Discord.RichEmbed()
    .setColor(0x0080ff)
    .setDescription(text)
    .setTimestamp(new Date())
    .setFooter(msg.author.tag))
}