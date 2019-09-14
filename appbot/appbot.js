require('dotenv').config();
const Discord = require('discord.js')
const client = new Discord.Client({ disableEveryone: true })
const fs = require('fs')
client.commands = new Discord.Collection()
const simple = require('../appbot/libs/embed')
const owners = ['588521648349642753','516840368843522073']
const token = process.env.CLIENT_TOKEN

fs.readdir('./commands/', (err, files) => {
    if (err) console.error(err)
    let jsfile = files.filter(f => f.split('.').pop() === 'js')
    if (jsfile.length == 0) return console.warn("Couldn't find any commands.")

    jsfile.forEach((file, i) => {
        let props = require(`./commands/${file}`)
        console.log(`${file} loaded`)
        client.commands.set(props.help.name, props)
    })
})

client.on('ready', () => {
    client.user.setActivity('Running Appbot 2.3.1', { type: 'STREAMING' })
    console.log('Appbot v2.4.0 BETA Has Successfully Loaded')
})


client.on('message', async message => {
    if (message.channel.type == "dm") return
    if (!message.content.includes('_') || message.author.bot) return
    const isOwner = owners.includes(message.member.id)
    const args = message.content.slice(Object.keys('&').length).trim().split(/ +/g)
    const command = args.shift().toLowerCase()
    var errorLogs = client.channels.get('580515191243145236')

    let commandFile = client.commands.get(command.slice(0))

    //ONLY USE THIS SWITCH FOR DEVELOPING-UPDATING-OR CREATING NEW COMMANDS
    switch (command) {
        case 'test':
 
    }
    if (commandFile){ 
        message.delete(1000) 
        try { 
        commandFile.run(client, message, args, isOwner)
        }catch(error) {
            (errorLogs.send(`An error occured in guild: **${message.guild.name}** (${message.guild.id}) with command: \`kick\` \n \`\`\`${error}\`\`\``))
            
       }

    }
    else return
})

client.login(token)
