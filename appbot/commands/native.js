const Discord = require('discord.js')
const simple = require('../libs/embed')

module.exports.run = async (client, message, args, isOwner) => {
    return simple.embed('To install AppValley, make sure you are not clicking the `native` option, just clck install under the AppValley logo!', message)
}

module.exports.help = {
    name: 'native',
    description: 'Gives a bit of extra help related to the native option',
    permissions: undefined
}