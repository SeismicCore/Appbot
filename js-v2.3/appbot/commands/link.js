const Discord = require('discord.js')
const simple = require('../libs/embed')

module.exports.run = async (client, message, args, isOwner) => {
    return simple.embed('The AppValley website can be found at https://app-valley.vip', message)
}

module.exports.help = {
    name: 'link',
    description: 'Links member to official site',
    permissions: undefined
}