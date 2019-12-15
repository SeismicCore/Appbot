const Discord = require('discord.js')
const simple = require('../libs/embed')

module.exports.run = async (client, message, args, isOwner) => {
    return simple.embed('The AppValley official twitter account can be found at: https://twitter.com/app_valley_vip', message)
}

module.exports.help = {
    name: 'twitter',
    description: 'Shows appvalleys official twitter page',
    permissions: undefined
}