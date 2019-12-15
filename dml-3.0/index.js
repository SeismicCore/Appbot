const Discord = require('discord.js')
const client = new Discord.Client({ disableEveryone: true })
const simple = require('./lib/commandDisplayHandler')
const parser = require('./lib/stringParser')
const fs = require('fs-extra')
const cheerio = require('cheerio')
const chalk = require('chalk')
const _ = require('lodash');

const commands = new Set()
let botPrefix = null
let owner = null

if (!fs.existsSync('./markup/bot.dml')) {
    fs.createFileSync('./markup/bot.dml')
    fs.writeFileSync('./markup/bot.dml', fs.readFileSync('./generated/bot.txt'))
    console.error(chalk.red('We notcied your bot.dml file was missing, so DML automatically generated it for you. Please rerun your script'))
}
if (!fs.existsSync('./markup/commands/')) {
    fs.createFileSync('./markup/commands/ping.dml')
    fs.writeFileSync('./markup/commands/ping.dml', fs.readFileSync('./generated/ping.txt'))
    console.error(chalk.red('We noticed your commands directory was missing, so we automatically generated it along with an example ping script for you'))
}
const $ = cheerio.load(fs.readFileSync('./markup/bot.dml'))

fs.readdir('./markup/commands/', (err, files) => {
    files.forEach(file => {
        if (!file.endsWith('.dml')) return
        console.log(chalk.blue.bgGreen(`Loaded file: ${chalk.red(file)}`))
        let commandName = file.split(".")[0];
        commands.add(commandName)
    });
})

client.on('message', async message => {
    if (message.channel.type == "dm") return
    if (!message.content.startsWith(botPrefix) || message.author.bot) return

    const args = message.content.slice(Object.keys(botPrefix).length).trim().split(/ +/g)
    const command = args.shift().toLowerCase()
    if (!commands.has(command)) return
    const $$ = cheerio.load(parser.parse(`./markup/commands/${command}.dml`, client, message))
    const responseE = $$('response');
    if ($$('script').get()[0] != undefined) {
        const scripts = $$('script').get()[0].children[0].data
    try {
        eval(scripts)
    } catch (error) {
        throw new Error(chalk.red('DML Script Tag Error'))
    }}
    if (responseE.length === 0) return console.log(chalk.bgWhite.red('Command Missing <response> element!'))
    if (args.length === 0 || $$('arg').length === 0) return simple.embed('response', $$, responseE, message)
    else {
        $$('arg').each((i, el) => {
            if (args[0] > $$('arg').length) return
            elem = $$(el)
            if (args[0] === elem.attr('value')) {
                const argE = elem
                simple.embed(`arg[value=${i + 1}]`, $$, argE, message)
            }
        })
    }
})

client.on('ready', () => {

    const totalUsers = client.guilds.reduce((total, guild) => total + guild.memberCount, 0)

    client.channels.get('REDACTED').send(
        new Discord.RichEmbed()
            .setAuthor('Retre0n Startup')
            .setDescription(`<a:check:567452249555730445> AppBot **v3.0** has successfully started with **${totalUsers}** users on **${client.guilds.size}** guilds!`)
            .setColor(0x36393E)
            .setTimestamp())

    let presanceE = $('settings > presance').first()
    let presanceType;
    if (!presanceE.text()) console.log(chalk.green.underline('No presance entered!'))
    if (!presanceE.attr('type')) presanceType = 'PLAYING' 
    else (presanceType = presanceE.attr('type'))
    client.user.setActivity(presanceE.text(), {type: `${presanceType}`})

    let startupE = $('startup').first()
    console.log(chalk.green.underline('Discord Markup Language Has Launched Successfully!'))
    try {
        if (!startupE.attr('channel')) console.log(chalk.yellow.inverse('! No startup channel set in: bot.dml !'))
        else client.channels.get(startupE.attr('channel')).send((startupE.attr('embed') === 'true') ? new Discord.RichEmbed().setDescription(startupE.text()).setColor(startupE.attr('color')) : startupE.text())

        botPrefix = $('settings > prefix').text()
        owner = $('settings > owner').text().split(',')
        _.each(owner, (value) => {
            console.log(`${chalk.yellow(client.users.get(value).tag)} Is A Bot Owner!`)
        })
    }
    catch (e) {
        if (e.message.includes('send')) console.log(chalk.yellow.inverse(`Error sending message to startup channel. Possibly invalid channel ID?\nParser error: ${e.message}`))
        if (e.message.includes('tag')) console.log(chalk.yellow.inverse(`Error grabbing owner usernames. Possibly invalid user ID?\nParser error: ${e.message}`))
    }
})

client.on('error', (err) => {
    console.log(err)
})

client.on('warn', (warn) => {
    console.log(warn)
})



client.login($('settings > token').text()).catch(() => {
    console.error(chalk.red(`${chalk.blue($('settings > token').text())} is an incorrect bot token!`))
})
