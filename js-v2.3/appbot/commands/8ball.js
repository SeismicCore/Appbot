const Discord = require('discord.js')
const simple = require('../libs/embed')

module.exports.run = async (client, message, args, isOwner) => {
    var question = args.join(" ")
    if (!question) return simple.embed('Im not a phycic, you must ask a question!', message)
    function eigthball() {
        var rand = ['Yes', 'No', 'This aint it cheif', 'certiantly', 'possibly', '~~Dont~~ try again later', ' You may rely on it', 'If i say yes will you go away?', 'Use your  i m a g i n a t i o n', 'Ya know, its not that hard to go to Walmart, buy an 8ball, and shake it. Why are you bothering me?', 'Maybe', 'Never', 'Yep']

        return rand[Math.floor(Math.random()*rand.length)]
}
        
            return simple.embed(message.member + ' asked: ' + '**' + question + '**' + `
            --------` + `
            `
            + '🎱 | ' + eigthball(), message);
}

module.exports.help = {
    name: '8ball',
    description: 'Gives an answer to any question',
    permissions: undefined
};