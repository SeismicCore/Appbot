const Discord = require('discord.js')
const simple = require('../libs/embed')
var weather = require('weather-js');

module.exports.run = async (client, message, args, isOwner) => {
if(!args[0]) return simple.embed('Please enter a location!', message)
weather.find({search: args.join(" "), degreeType: "F"}, function(err, result) { //finds wethar for location entered
    if (err) {
        const errorEmbed = new Discord.RichEmbed()
        .setTimestamp()
        .setAuthor('An error occured!')
        .setDescription(`${err}`)
        .addFooter(message.author.tagname)
    
        message.channel.get("580515191243145236").send(errorEmbed)}
        // logs if theres an error to <#580515191243145236>s


    else {
    
    console.log(result)
    if(!result[0]) {
        return simple.embed('You must enter a valid location!', message)
}
    var location = result[0].location //bad spelling
    var current = result[0].current;

    if (!location || !current)
        return simple.embed('You must enter a valid location!', message)  

    const weatherEmbed = new Discord.RichEmbed()
    .addField('Observation Time:', `${current.day}, ${current.date} at ${current.observationtime} UTC${location.timezone}`, true)
    .addField(`Sky:`, `${current.skytext}`)
    .setAuthor(`Current weather for ${current.observationpoint}`)
    .setThumbnail(current.imageUrl)
    .setColor('RANDOM')
    .addField('Temperature:', `${Math.round((current.temperature - 32) * 5/9)}° C / ${current.temperature}° F`, true)
    .addField('Feels Like Temp:', `${Math.round((current.feelslike - 32) * 5/9)}° C / ${current.feelslike}° F`, true)
    .addField('Winds:', `${current.winddisplay}`, true)
    .addField('Humidity:', `${current.humidity}%`)
    message.channel.send(weatherEmbed)//weatherEmbed)
    // sends current weather info
}})}
module.exports.help = {
    name: 'weather',
    description: 'Gives the weather',
    permissions: undefined
};