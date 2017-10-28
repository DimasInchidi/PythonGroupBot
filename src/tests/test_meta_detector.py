import unittest
from meta_detector import *


class MetaDetectorTest(unittest.TestCase):
    def setUp(self):
        # data since 18-10-2017
        self.not_filtered_yet_msg = {
            # 'Also, do anyone know what happened to #359 issue about SSL errors with telegram+webhooks?',
            # 'For anyone interested, I replaced  JSON.parse(e.postData.contents) with evaluation (e.postData.contents) '+
            # 'and now it gives me the group id correctly 👍',
            # 'Hey Guys From a last few week we(me and my Team) are working on a project, currently we need some extra '
            # 'hand  (Machine Learning Developer, Python Developer) If anyone interested just ping me Location : Delhi',
            # 'Does anyone have the link for joining the python telegram channel?',
            # 'Ive learned to not listen to anyone wearing Red / cyan glasses' +
            # 'How to verbal English practice; can anyone teach?' +
            # 'does anyone have a code example webhook?',
            # 'Hey together. Can anyone explain me, how Retroshare could replace a phpBB-Forum?' +
            # 'On one side - How is it possible to fully connect a community alltogether? Who decides how much of the ' +
            # 'community activity I will see and experience? Will i see everey interaction that is public on a ' +
            # 'phpbb-forum in the same way at retroshare? ' +
            # 'How are "posts" and "comments" (are they called that way?) viewable by every member of the community?' +
            # 'And on the other Hand - How can guests view "posts" and "comments"?' +
            # 'Or is Retroshare a tool for a different purpose? Is it in the end an infrastructure for a decentral ' +
            # 'network, where I will only see what those, that trust me, allow me to see?',
            # 'Hi guys!' +
            # 'I\'m wonder telegram bot. I\'ve installed a bot on my raspberry pi and it\'s living it very happy :-). I '
            # 'coded it at python.' +
            # 'Frequently, my sharing files server based on samba is down when I use my bot. I think the problem is '
            # 'python because samba is coded partially on python. Has anyone had this problem? Thank you ',
            # 'And also, if anyone can contribute I\'d be more than greatful' +
            # 'https://github.com/Y45HW4N7/profile-management/tree/wip',
            # 'if anyone figures out why, tell me, I\'m curious, lol',
            # 'Hello. Anyone use python to make mobile games here? I\'ve been Googling but I couldn\'t find anything '
            # 'but a framework for 2D games and for desktop',
            # 'It\'s not python, though. Strictly speaking is off-topic here. Note that the underlying code needs '
            # 'testing, if anyone is interested in helping test go to the mighty_make github page, download the test '
            # 'branch, and report back with suggestions.',
            # 'Hey Guys, I am developing a basic social network site, but I am confused which web framework should I '
            # 'use? Should I go for Flask, or Django or something else? Can anyone help me with this?',
            # 'Hey Folks, we need volunteers for workshops for Pycon India 2017. Anyone who can help out with this, '
            # 'please PM.',
            # 'Please how does anyone have a good eBook on Django installation on window 7',
            # 'does anyone know why?',
            # 'anyone successfully use kick_chat_member with until_date working well? i tried to set a several '
            # 'different until_date and it still stayed as banning forever',
            # 'Anyone used python with Google app engine? Planning to deploy a script I  have and need some '
            # 'clarifications about what is supported and what is not.',
            # 'Hi, does anyone know how to get buttons?',
            # 'Hello everyone. I need my bot to write chat_id, user_id and some more info in database. Can anyone give '
            # 'me some advice please?',
            # 'Hello everyone. I was trying to do a schedule bot, but got stuck in the schedule thing in Python. Anyone '
            # 'know any good library or way to make a schedule (repeat everyday, or hour, or minute). Also, '
            # 'is there already a schedule functionality in the Bot() class? Thanks.',
            # 'anyone if you can give me information that how you user or design Road and trees in a Game Using c or '
            # 'c++  programming Language',
            # 'Can anyone ping me any doc link which says how to use API',
            # 'does anyone have more examples of conversation handlers? I just want to receive username and password in '
            # 'a single message',
            # 'Hey, I am trying to find a regex, that would match anything except certain commands - does anyone have '
            # 'something like that?',
            # 'anyone wanting to test out my semi-rootkit written in python on a local windows machine they dont care '
            # 'about?',
            # 'Hi friends, can anyone point me to an API for bot telegram, which allows me to send and receive messages '
            # 'easily, but can also send images, or do the bot return an image when it receives the link from the '
            # 'image?',
            # 'I need a simple thing which will show me a really basic ml project about that. :))',
            # 'Anyone',
            # 'Who can teach me python?',
            # 'Did someone do german with rosetta stone?',
            # 'Hi guys...am trying to tackle some python questions...can i post here to be assisted',
        }
        self.nota_meta_questions_list = {
            
        }
        self.meta_questions_list = (
            'hi people. Anyone here knows a kivy group?',
            'Anyone good with Bootstrap? Would need some help. :/',
            'anyone here worked with shodan api ??',
            'Anyone know a good book of NLP?',
            'Hi everyone!Did anyone try to use telegram bot on webhooks from docker container?',
            'Anyone want to introduce some groups for me',
            'Anyone done Messenger bots in here?',
            'Has anyone used scp in pexpect?',
            'Excuse me, has anyone ever used CARP protocol in Debian?',
            'hey does anyone have that meme',
            'Hi Im new to python and having trouble making a program i want to do, could anyone help me?',
            'Hi guys, I have a question about Django. Can anyone help me please?',
            'Anyone here to help??',
            'Anyone knows it',
            'Hello, have anyone got telegram error with empty telegram id?',
            'I didn\'t message anyone yet. I just rerun the application.',
            'Is there anyone online',
            'Does anyone have python for R users suggestions..books videos',
            'Anyone familiar with mongoDb and getting it connected to Django here?',
            'Anyone familiar with *HELL* forum here..',
            'Do anyone knows off a group of forum or anything for emscripten',
            'anyone can do an parttime coding job?',
            'Does anyone knows to recover arena ransomware. Since my computer is effected with this.',
            'anyone worked with Emscipten?',
            'so, uh anyone ever done django+bootstrap or django+foundation or another css framework',
            'Anyone know a raspberry pi telegram groups?',
            'Anyone here who can voluntarily put me through building intelligent chatbot with python?',
            'Anyone working in QA?',
            'ot, has anyone tried squarespace?',
            'can anyone suggest some books to study c ++?',
            'doesn\'t anyone have a pool bot that edit the message every time a vote is sent?',
            'Do anyone tried to use Electron with Python? I\'m trying to discover new approaches to develop GUI apps',
            'can anyone suggest some books to study c ++?',
            'I\'ve never seen anyone use hashtable',
            'anyone good with regular expressions?',
            'I uninstalled telegram if anyone is wondering btw',
            'Does anyone know Python Instant View Articles TG group?',
            'that rarely anyone uses',
            'Does anyone have an HTML5 Game example that I could check out?',
            'Does anyone here work with stock market? I\'m new on this stuff and need some advice.',
            'Anyone into natural language processing?',
            'Does anyone use vscode for python?',
            'anyone used AWS lambda?',
            'Does anyone here codes for stock or crypto market?',
            'hello. is there anyone who develops machine learning projects with Python? I\'m interested with that, ',
            'Hi please any Electrical/Electronics Engineer on here?',
            'Anyone familiar with vxWorks',
            'anyone up?',
            'someone can use AHK here?',
            'nativescript anyone?',
        )
        self.not_meta_questions_list = (
            'Why would anyone believe Salman?',
            '',
            '',
            '',
        )

    def test(self):
        for m in self.meta_questions_list:
            self.assertEqual(
                is_meta_question(m),
                True,
                'this message considered as not a meta question:\n\n' + m
            )
