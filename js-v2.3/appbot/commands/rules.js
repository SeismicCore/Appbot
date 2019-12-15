const Discord = require('discord.js')
const simple = require('../libs/embed')

module.exports.run = async (client, message, args, isOwner) => {
    return simple.embed('You can view our server rules here: <#509015468728909834> and our servers FAQ here: <#517554260355973169>', message)
}

module.exports.help = {
    name: 'rules',
    description: 'Links member to rules page',
    permissions: undefined
}