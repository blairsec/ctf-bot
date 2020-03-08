"use strict";
const Discord = require('discord.js');
const client = new Discord.Client();
const http = require('http')
const server = http.createServer((a,b)=>b.end('ok'))
server.listen(2900,_=>_)
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
	let actf = client.guilds.resolve("686027739966341154");
	let roles = actf.channels.resolve("686028786508103737");
	roles.messages.fetch("686029687469637653",true);
});

client.on('message', msg => {
	const sender = msg.guild?msg.guild.member(msg.author):null;
	if (msg.content == "!ping" && msg.channel.id=="686030136406966311") {
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
	
	if (~msg.content.indexOf('kmh') && msg.channel.id=="686030136406966311") {
		msg.channel.send(emojify(kmh[~~(Math.random()*kmh.length)]));
	}
	
	if (~msg.content.indexOf('defund') && msg.channel.id=="686030136406966311") {
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
	if (reaction.message.id=="686029687469637653") {
		const guild = reaction.message.guild;
		const sender = guild?guild.member(user):null;
		const emoji = reaction.emoji;
		if (emoji.name == '🔔') {
			sender.roles.add("686030992657612806")
		}
	}
});

client.on('messageReactionRemove', (reaction,user) => {
	if (reaction.message.id=="686029687469637653") {
		const guild = reaction.message.guild;
		const sender = guild?guild.member(user):null;
		const emoji = reaction.emoji;
		if (emoji.name == '🔔') {
			try { sender.roles.remove("686030992657612806") } catch (e) {}
		}
	}
});

client.on('guildMemberAdd', member => {
	console.log(member)
	member.roles.add("686028267475697666")
})

client.login(process.env.TOKEN);
