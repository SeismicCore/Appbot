const Discord = require('discord.js')
const simple = require('../libs/embed')

module.exports.run = async (client, message, args, isOwner) => {
    if(!args.join(' ')) return simple.embed(':warning: You must give a suggestion!', message)
        const feedbackEmbed = new Discord.RichEmbed()
        .setAuthor(`New Feedback - ${message.author.tag}`)
        .setDescription(args.join(' '))
        .setColor('RANDOM')
        .setThumbnail(message.author.avatarURL)
        .setTimestamp()
        client.channels.get('FEEDBACK_CHANNEL').send(feedbackEmbed)
    return simple.embed('Thanks for your feedback! If additional information is needed from my developers, they will contact you soon!', message)
}

module.exports.help = {
    name: 'feedback',
    description: 'Allows member to give feedback to the appbot devs',
    permissions: undefined
}
