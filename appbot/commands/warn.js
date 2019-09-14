const Discord = require('discord.js')
const simple = require('../libs/embed')

module.exports.run = async (client, message, args, isOwner) => {
    return simple.embed('**COMMAND BEING FIXED**', message)
}

module.exports.help = {
    name: 'warn',
    description: 'Warns a member',
    permissions: undefined
}