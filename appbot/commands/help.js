const Discord = require('discord.js')
const fs = require('fs')
module.exports.run = async (client, message, args, isOwner) => {
    var permissions = new Discord.Permissions(message.channel.permissionsFor(client.user.id).bitfield)
    if (!message.guild.me.hasPermission('ADD_REACTIONS')) return message.channel.send('i need the `ADD_REACTIONS` permission for this command to work!')
    if (!permissions.has('ADD_REACTIONS')) return message.channel.send('i need the `ADD_REACTIONS` permission in this channel for this command to work!')
    if (!message.guild.me.hasPermission('USE_EXTERNAL_EMOJIS')) return message.channel.send('I need the `Use External Emojis` permission for the help command to work!')
    if (!permissions.has('USE_EXTERNAL_EMOJIS')) return message.channel.send('I need the `Use External Emojis` permission in this channel for the help command to work!')
    let page = 1
    let pages =
        ["__*Information*__\n**_help**: Shows this menu\n**_status**: Shows AppValley's current status\n**_link**: Gives a link to the official AppValley website\n**_twitter**: Gives a link to the official AppValley ttwitter\n**_rules**: Shows where to find the AppValley Server rules\n**_native**: Explains how to fix the 'native' error/issue"
            , "__*Information (2)*__\n**_vip**: Gives a link to the AppValley VIP website\n**_viphelp**: Gives a link to the AppValley VIP help page\n**_reddit**: Gives a link to the AppValey Official Reddit\n**_revoke**: Explaines what a 'revoke' is\n**safari**: Explains what browser to use when installing AppValley"
            , "__*Utility*__\n**_ping**: Displays AppBot's curent ping\n**_stats**: Gives information of AppBot's core systes\n**_suggest**: Suggest a server feature, or app to be update to the AppValley team\n**_feedback**: Provide feedback to the developers of AppBot\n**-Store**: This command is being added back in v2.3.2! (Currently in beta)\n**_remind**: Sets a reminder - Must have acctept DMs from server members ON"
            , "__*Fun*__\n**_weather**: Display a city's current weather\n**_8ball**: Ask the magic 8 bal a question\n**_coinflip**: Flip a coin!\n**_dice**: Role a number between 1 and 6\n**_urban**: Get a definition form the Urban Dictionary"
            , "__*Moderation*__\n**_kick**: Kicks a member from the server\n**_ban**: BEING REPROGRAMMED\n**_warn**: BEING REPROGRAMMED\n**_purge**: BEING REPROGRAMMED\n**_mute**: BEING REPROGRAMMED"
            , "__*Developer Only*__\n**_say**: Says a message through the bot\n**_status UPDATE**: Updates the 'Status' page"]
    const embed = new Discord.RichEmbed()
        .setTitle(`__Help Menu - Page ${page} Of ${pages.length}__`)
        .setDescription(pages[0])
        .setColor(0x00d17d)
        .setFooter(`Requested By: ${message.author.tag}`).setTimestamp()
    message.channel.send(embed).then(async msg => {
        await msg.react('a:arrowL:604186508668305408')
        await msg.react('a:arrowR:604186540888948769')

        const backFilter = (reaction, user) => reaction.emoji.name === 'arrowL' && user.id == message.author.id
        const fowardFilter = (reaction, user) => reaction.emoji.name === 'arrowR' && user.id == message.author.id

        const back = msg.createReactionCollector(backFilter, { time: 60000 })
        const foward = msg.createReactionCollector(fowardFilter, { time: 60000 })

        back.on('collect', r => {
            msg.reactions.find(r => r.emoji.name == 'arrowL').remove(message.author.id)
            if (page === 1) return
            page--
            embed.setTitle(`__Help Menu - Page ${page} Of ${pages.length}__`)
            embed.setDescription(pages[page - 1])
            msg.edit(embed)
        })
        foward.on('collect', r => {
            msg.reactions.find(r => r.emoji.name == 'arrowR').remove(message.author.id)
            if (page === pages.length) return
            page++
            embed.setTitle(`__Help Menu - Page ${page} Of ${pages.length}__`)
            embed.setDescription(pages[page - 1])
            msg.edit(embed)
        })
        foward.on('end', () => {
            embed.setTitle(`__Type _help__`)
            embed.setDescription('Reaction Menu Automatically Closed')
            embed.setColor(0xff0000)
            return msg.edit(embed)
        })
    })
}

module.exports.help = {
    name: 'help',
    description: 'Shows All Commands',
    permissions: undefined
}
