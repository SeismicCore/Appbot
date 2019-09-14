const Discord = require('discord.js')
const simple = require('../libs/embed')

module.exports.run = async (client, message, args, isOwner) => {
    function flip() {
        var rand = ['Heads', 'Tails']

        return rand[Math.floor(Math.random()*rand.length)]
}
        
            return simple.embed('<a:avcoin:600572686112129024> | ' + flip(), message);
}

module.exports.help = {
    name: 'coinflip',
    description: 'Flips a coin... or a user.',
    permissions: undefined
};