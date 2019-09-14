const Discord = require('discord.js')
const simple = require('../libs/embed')

module.exports.run = async (client, message, args, isOwner) => {
    if(!args.join(' ')) return simple.embed(':warning: You must give a suggestion!', message)
        const suggestEmbed = new Discord.RichEmbed()
        .setAuthor(`New suggestion - ${message.author.tag}`)
        .setDescription(args.join(' '))
        .setColor('RANDOM')
        .setThumbnail(message.author.avatarURL)
        .setTimestamp()
        client.channels.get('507908076439994388').send(suggestEmbed)
        .then(async msg=>{
            await msg.react('✅')
            await msg.react('❌')
    })
    return simple.embed('Suggestion sent! Please check <#507908076439994388>', message)
}

module.exports.help = {
    name: 'suggest',
    description: 'Allows member to suggest something',
    permissions: undefined
}