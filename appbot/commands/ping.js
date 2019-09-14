const Discord = require('discord.js')

module.exports.run = async (client, message, args, isOwner) => {
    var m = await message.channel.send('Ping?')
    return m.edit(`:ping_pong: | Appbots Latency Is ${m.createdTimestamp - message.createdTimestamp}ms. API Latency Is ${Math.round(client.ping)}ms`)
}

module.exports.help = {
    name: 'ping',
    description: 'Shows Appbots Current Connection Speeds',
    permissions: undefined
}