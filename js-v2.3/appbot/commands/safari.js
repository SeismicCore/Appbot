const Discord = require('discord.js')
const simple = require('../libs/embed')

module.exports.run = async (client, message, args, isOwner) => {
    return simple.embed('To download AppValley, you must use the safari browser!', message)
}

module.exports.help = {
    name: 'safari',
    description: 'Tells member which browser they must use',
    permissions: undefined
}