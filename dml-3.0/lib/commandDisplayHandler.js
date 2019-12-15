const Discord = require('discord.js')

exports.embed = (messageElemCheck,$$, elem, message) => {
    /*THIS PORTION HANDLES MESSAGES*/
    //Checks If Message Isnt An Embed
    if (!$$(`${messageElemCheck} > embed`).length) return message.channel.send(elem.text())

    //Sends If Message Is An Embed
    let embed = new Discord.RichEmbed()
    if (elem.find('title').length !== 0) embed.setTitle(elem.find('title').first().text())
    if (elem.find('author').length !== 0) embed.setAuthor(elem.find('author').first().text())
    if (elem.find('description').length !== 0) embed.setDescription(elem.find('description').first().text())
    if (elem.find('thumbnail').length !== 0) embed.setThumbnail(elem.find('thumbnail').first().text())
    if (elem.find('field').length !== 0) elem.find('field').each((i, elem) => {
        embed.addField($$(elem).attr('title'), $$(elem).text())
    })
    if (elem.find('color').length !== 0) embed.setColor(elem.find('color').first().text())
    if (elem.find('footer').length !== 0) embed.setFooter(elem.find('footer').first().text(), elem.find('footer').attr('image'))
    if (elem.find('footer').attr('timestamp') === 'true') embed.setTimestamp()
    message.channel.send(embed)
    /*END*/
    /*THIS PORTION HANDLES CONSOLE EVENTS*/
    if(elem.find('console').length !== 0) elem.find('console').each((i, elem)=>{
        console.log($$(elem).text())
    })
}