const Discord = require('discord.js')
const simple = require('../libs/embed')
const urban = require('relevant-urban')

module.exports.run = async (client, message, args, isOwner) => {
    var term = args.join(" ")
    if (!term) return simple.embed('Please give a term to search!', message)
    let Chris = true;
    let res = await  urban(args.join(" ")).catch (e => {
        Chris = false;
        message.channel.send(`There is no match for **${term}** on the Urban Dictonary!`).catch(/*this can also throw an exception!*/);
    });
        
    if(!Chris)
        return;

    const urbanEmbed = new Discord.RichEmbed()
    .setColor('RANDOM')
    .setTitle(res.word)
    .setURL(res.urbanURL)
    .setTimestamp()
    .setFooter(message.author.tag)
    .setDescription('**Definition: **' + res.definition + `
    ` + `
    ` + '**Example: **' + res.example + `
    ` + `
    ` + '**Author**: ' + res.author  + `<:upvote:600588188402188288>${res.thumbsUp} <:downvote:600588177467768832>${res.thumbsDown}.`)
    message.channel.send(urbanEmbed)
}

module.exports.help = {
    name: 'urban',
    description: 'Finds a word form the Urban Dictonary',
    permissions: undefined
}