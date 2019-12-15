const Discord = require('discord.js')
const fs = require('fs')
const os = require('os');
const sysinfo = require('systeminformation');
module.exports.run = async (client, message, args, isOwner) => {
    const cpu = await sysinfo.cpu()
    const system = await sysinfo.osInfo()
    const memory = await sysinfo.mem()
    var date = new Date(null);
    date.setSeconds(os.uptime); // specify value for SECONDS here
    var timeString = date.toISOString().substr(11, 8);
    return message.channel.send(new Discord.RichEmbed()
        .setAuthor('Statistics')
        .addField(':earth_americas: __Connected To:__', '```• ' + client.guilds.size + ' Servers\n• ' + client.channels.size + ' Channels\n• ' + client.users.size + ' Users```', true)
        .addField('<:textline_green:589715854900330497> __Codebase:__', '```• Written In: Node.js ' + process.version + '\n• Libraries: Discord.js v11.5.1```', true)
        .addField('<:emoji_8:589724098209251328> __VPS:__', '```• Operating System: ' + system.platform + '\n• Distribution: ' + system.distro + ' \n• CPU Processors: ' + cpu.speed + '\n• Uptime: ' +timeString+'```')
        .setFooter(`Requested By: ${message.author.tag}`, message.author.avatarURL)
        .setTimestamp()
        .setColor(0x00d17d))
}
module.exports.help = {
    name: 'stats',
    description: 'Shows System And Bot Statistics',
    permissions: undefined
}