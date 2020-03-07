"use strict";
const Discord = require('discord.js');
const client = new Discord.Client();
const http = require('http')
const server = http.createServer((a,b)=>b.end('ok'))
server.listen(2900,_=>_)
const req = o=>o&&o.__esModule?o:{default:o};
const discordIRC = req(require('discord-irc'));
(0,discordIRC.default)({
	"nickname": "blebleblebleble",
	"server": "irc.freenode.net",
	"discordToken": process.env.TOKEN,
	"channelMapping": {
		"685520418827927612": "#angstromctf"
	},
	"format": { // Optional custom formatting options
		// Patterns, represented by {$patternName}, are replaced when sending messages
		"commandPrelude": "Message from IRC:", // Message sent before a command
		"ircText": "<{$displayUsername}> {$text}", // When sending a message to IRC
		"urlAttachment": "<{$displayUsername}> {$attachmentURL}", // When sending a Discord attachment to IRC
		"discord": "**<{$author}>** {$withMentions}", // When sending a message to Discord
		// Other patterns that can be used:
		// {$discordChannel} (e.g. #general)
		// {$ircChannel} (e.g. #irc)
		"webhookAvatarURL": "https://robohash.org/{$nickname}" // Default avatar to use for webhook messages
	},
	"webhooks": {
		"685520418827927612": "https://discordapp.com/api/webhooks/685930097920049182/QapIGe6qYxSxfyGXqW3lArwMbdNIBjCLOmz76L5cDtHlMXX3npNLqEDHs-eFhefHVdfu"
	}
});
let defund = `no more weebs
burn the weebs
waw is evil
down with big kristen
nazi mod
down with defund
overthrow william austin wang`.split("\n")

let kmh = `malware man
kevin michael higgs
higgy baby
kmh use discord
kmh stop using irc`.split("\n")
function emojify(m){
	return m.split("").map(x=>"abcdefghijklmnopqrstuvwxyz".indexOf(x)+1?`:regional_indicator_${x}:`:x).join(' ');
}
client.on('ready', () => {
	console.log(`Logged in as ${client.user.tag}!`);
	let actf = client.guilds.resolve("685493960696791051");
	let roles = actf.channels.resolve("685528228412260352");
	roles.messages.fetch("685531046095224842",true);
});

client.on('message', msg => {
	const sender = msg.guild?msg.guild.member(msg.author):null;
	if (msg.content == "!ping" && msg.channel.id=="685903047381352454") {
		msg.channel.send("pong");
	}
	if (/actf{.+}/.test(msg.content)) {
		msg.delete().then(m=>console.log(`deleted message (flag)`)).catch(console.error);
		if (sender) {
			sender.kick('flag sharing').then(m=>console.log(`kicked ${sender.user.tag}`)).catch(_=>_);
		}
	}
	if (/super_legit_flag_string/.test(msg.content)) {
		msg.delete().then(m=>console.log(`deleted message (legit flag)`)).catch(console.error);
		if (sender) {
			sender.ban('legit flag sharing').then(m=>console.log(`banned ${sender.user.tag}`)).catch(_=>_);
		}
	}
	
	if (~msg.content.indexOf('kmh') && msg.channel.id=="685903047381352454") {
		msg.channel.send(emojify(kmh[~~(Math.random()*kmh.length)]));
	}
	
	if (~msg.content.indexOf('defund') && msg.channel.id=="685903047381352454") {
		msg.channel.send(emojify(defund[~~(Math.random()*defund.length)]));
	}
	
});

client.on('messageUpdate', (oldMessage,newMessage) => {
	const sender = newMessage.guild?newMessage.guild.member(newMessage.author):null;
	if (/actf{.+}/.test(newMessage.content)) {
		newMessage.delete().then(m=>console.log(`deleted message: ${m}`)).catch(console.error);
		if (sender) {
			sender.kick('flag sharing').then(m=>console.log(`kicked ${sender.user.tag}`)).catch(console.error);
		}
	}
});

client.on('messageReactionAdd', (reaction,user) => {
	if (reaction.message.id=="685531046095224842") {
		const guild = reaction.message.guild;
		const sender = guild?guild.member(user):null;
		const emoji = reaction.emoji;
		if (emoji.name == '🔔') {
			sender.roles.add("685537540002152478")
		}
		if (emoji.name == '🚩') {
			sender.roles.add("685529428930854964")
		}
	}
});

client.on('messageReactionRemove', (reaction,user) => {
	if (reaction.message.id=="685531046095224842") {
		const guild = reaction.message.guild;
		const sender = guild?guild.member(user):null;
		const emoji = reaction.emoji;
		if (emoji.name == '🔔') {
			sender.roles.remove("685537540002152478")
		}
		if (emoji.name == '🚩') {
			sender.roles.remove("685529428930854964")
		}
	}
});

client.login(process.env.TOKEN);
