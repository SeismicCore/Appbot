const Discord = require('discord.js')
const simple = require('../libs/embed')

module.exports.run = async (client, message, args, isOwner) => {
    return simple.embed('To find help with Builds.io, you can visit their help page at https://builds.io/help', message)
}

module.exports.help = {
    name: 'viphelp',
    description: 'Gives member some help with appvalley vip related issues',
    permissions: undefined
}