const Discord = require('discord.js')
const simple = require('../libs/embed')

module.exports.run = async (client, message, args, isOwner) => {
    return simple.embed('The AppValley official reddit page can be found at https://www.reddit.com/r/appvalley', message)
}

module.exports.help = {
    name: 'reddit',
    description: 'Links member to official reddit',
    permissions: undefined
}