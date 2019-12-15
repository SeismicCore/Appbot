const Discord = require('discord.js')
const simple = require('../libs/embed')

module.exports.run = async (client, message, args, isOwner) => {   
        return simple.embed(`:game_die: You rolled a ${Math.floor(Math.random()*6)}! :game_die:`, message);
}

module.exports.help = {
    name: 'dice',
    description: 'Roll a 6-sided die.',
    permissions: undefined
}

