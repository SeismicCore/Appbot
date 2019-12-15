const fs = require('fs')
const _ = require('lodash')
const cheerio = require('cheerio')

exports.parse = (fileURL, client, message) => {
    let str = null
    str = fs.readFileSync(fileURL).toString()
    const $ = cheerio.load(str)
    const member = $('require').attr('member')
    const modifiers = {
        bot: {
            'ping': Math.round(client.ping),
            'id': client.user.id,
            'createdOn': client.user.createdAt,
            'avatar': client.user.avatarURL,
            'presence:status': (client.user.presence != null) ? client.user.presence.status: null

        },
        author: {
            'id': message.author.id,
            'tag': message.author.tag,
            'avatar': message.author.avatarURL,
            'username': message.author.username,
            'nickname': message.member.nickname,
            'isBot': message.author.bot,
            'createdOn': message.author.createdAt,
            'presence:status': (message.author.presence != null) ? message.author.presence.status: null,
            'presence:name': (message.author.presence.game != null) ? message.author.presence.game.name: null,
            'presence:details': (message.author.presence.game != null) ? message.author.presence.game.details: null,
            'presence:state': (message.author.presence.game != null) ? message.author.presence.game.state: null,
            'presence:time:start': (message.author.presence.time != null) ? message.author.presence.game.timestamps.start: null,
            'presence:time:end': (message.author.presence.time != null) ? message.author.presence.game.timestamps.end: null
        },
        member: {
            'tag': (member) ? client.users.get(member).tag: null,
            'avatar': (member) ? client.users.get(member).avatarURL: null,
            'username': (member) ? client.users.get(member).username: null,
            'createdOn': (member) ? client.users.get(member).createdAt: null,
        },
        message: {
            'content': message.author.lastMessage.content,

        },
        guild: {
            'name': message.guild.name,
            'owner': message.guild.owner.user.tag,
            'owner:nickname': message.guild.owner.nickname,
            'owner:id': message.guild.owner.id,
            'owner:createdOn': message.guild.owner.user.createdAt
        }
    }
    _.each(modifiers, (value, key) => {
        _.each(modifiers[key], (value, subkey) => {
            str = str.replace(new RegExp(`{{${key + ':' + subkey}}}`, 'g'), value)
        })
    })
    str = str.replace(/^\s+/gm, '')    
    return str
}