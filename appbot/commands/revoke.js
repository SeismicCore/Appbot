const Discord = require('discord.js')
const simple = require('../libs/embed')

module.exports.run = async (client, message, args, isOwner) => {
    return simple.embed('What we call a revoke, is something that happens when someone reports a third-party app store to apple and takes away our permissions to use our signed programs. they take away our permissions to allow you to download apps and force anyone to delete any currently downloaded apps; however, revokes can be avoided by purchasing a VIP membership at https://appvalley.builds.io !', message)
}
module.exports.help = {
    name: 'revoke',
    description: 'Explains what a revoke is',
    permissions: undefined
}