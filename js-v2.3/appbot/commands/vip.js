const Discord = require('discord.js')
const simple = require('../libs/embed')

module.exports.run = async (client, message, args, isOwner) => {
    return simple.embed('The AppValey VIP website can be found at https://appvalley.builds.io', message)
}

module.exports.help = {
    name: 'vip',
    description: 'Links member to official vip site',
    permissions: undefined
}