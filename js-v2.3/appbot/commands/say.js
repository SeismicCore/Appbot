const Discord = require('discord.js')
const simple = require('../libs/embed')

module.exports.run = async (client, message, args, isOwner) => {
    if(!isOwner) return simple.embed('You must be an Appbot developer to use this command!', message)
    if(!args.join(' ')) return simple.embed('You must enter a message with the say commands', message)
    return simple.embed(args.join(' '), message)
}

module.exports.help = {
    name: 'say',
    description: 'Make the bot say something',
    permissions: undefined
}