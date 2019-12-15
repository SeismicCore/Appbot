const Discord = require('discord.js')
const simple = require('../libs/embed')
const low = require('lowdb')
const FileSync = require('lowdb/adapters/FileSync')

const db = low(new FileSync('../database/appbot-main-database.json'))
db.defaults({
     status: {
         overall: '<a:check:567452249555730445> All systems are working as expected!', 
         revoke:'<a:check:567452249555730445> All servers working as expected.', 
         server:'<a:check:567452249555730445> All servers working as expected.',
         vip: '<a:check:567452249555730445> All VIP applications working as expected.',
         bot: '<a:check:567452249555730445> Appbot 2.3 is here with a new and improved command handler + more effecient command loading!'
        }
    }).write()

module.exports.run = async (client, message, args, isOwner) => {
    var status = db.get('status').value()
    if(args[0] == null){
        var statusEmbed = new Discord.RichEmbed()
        .setDescription(`__**Current Appvalley Status**__`)
        .setColor(0x00d17d)
        .addField('Overall Status: ', `${status.overall}`)
        .addField('Revoke Status: ', `${status.revoke}`)
        .addField('Server Status: ', `${status.server}`)
        .addField('VIP Status: ', `${status.vip}`)
        .addField('Bot Status: ', `${status.bot}`)
        .setTimestamp()
        .setFooter(`Requested By: ${message.author.tag}`, message.author.avatarURL)
        return message.channel.send(statusEmbed)
    }

    if(!isOwner) return simple.embed('You do not have permission to set appvalley status!', message)
    if(args[0] === 'overall'){
        if(!args[1]) return simple.embed(':warning: You must enter an `overall` message!', message)
        var msg = args.join(' ').slice(8)
        db.set('status.overall', msg).write()
        simple.embed(`Set overall to: ${msg}`, message)
    }
    if(args[0] === 'revoke'){
        if(!args[1]) return simple.embed(':warning: You must enter an `overall` message!', message)
        var msg = args.join(' ').slice(7)
        db.set('status.revoke', msg).write()
        simple.embed(`Set revoke to: ${msg}`, message)
    }
    if(args[0] === 'server'){
        if(!args[1]) return simple.embed(':warning: You must enter an `overall` message!', message)
        var msg = args.join(' ').slice(7)
        db.set('status.server', msg).write()
        simple.embed(`Set simple to: ${msg}`, message)
    }
    if(args[0] === 'vip'){
        if(!args[1]) return simple.embed(':warning: You must enter an `overall` message!', message)
        var msg = args.join(' ').slice(4)
        db.set('status.vip', msg).write()
        simple.embed(`Set simple to: ${msg}`, message)
    }
    if(args[0] === 'bot'){
        if(!args[1]) return simple.embed(':warning: You must enter an `overall` message!', message)
        var msg = args.join(' ').slice(4)
        db.set('status.bot', msg).write()
        simple.embed(`Set simple to: ${msg}`, message)
    }
    statusEmbed = new Discord.RichEmbed()
    .setDescription(`__**Current Appvalley Status**__`)
    .setColor(0x00d17d)
    .addField('Overall Status: ', `${status.overall}`)
    .addField('Revoke Status: ', `${status.revoke}`)
    .addField('Server Status: ', `${status.server}`)
    .addField('VIP Status: ', `${status.vip}`)
    .addField('Bot Status: ', `${status.bot}`)
    .setTimestamp()
    .setFooter(`Requested By: ${message.author.tag}`, message.author.avatarURL)
    return client.channels.get('552626824186822666').send(statusEmbed)

}

module.exports.help = {
    name: 'status',
    description: 'Changes appvalley status page',
    permissions: undefined
}