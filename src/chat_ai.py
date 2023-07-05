from REGEX_TOOLS import re_check, re_fullmatch, re_starts
from basic_conv_re_pattern import C

from CHAT_TOOLS import Rshuffle, Rchoice, shuf_merge, list_merge

from OS_sys import null

from user_handler import User
from msg_class import MessageObj

def patterns(user:User, msg=MessageObj):
	"""
	context: Counter object to keep track of previous message intents
	check_context: function to check if something is in the prev msg intent (context)
	"""

	return [
[
	[
		C("WHAT IS AI"),
		C("WHAT IS ARTIFICIAL INTELLIGENCE"),
	],
	(
		"Artificial intelligence (AI) is the simulation of human intelligence processes by machines, especially computer systems. These processes include learning (the acquisition of information and rules for using the information), reasoning (using rules to reach approximate or definite conclusions) and self-correction. Particular applications of AI include expert systems, speech recognition and machine vision."
	),
	"what_is_ai"
],
[
	[
		C("WHAT IS MACHINE LEARNING"),
		C("WHAT IS ML"),
	],
	(
		"Machine learning (ML) is the study of computer algorithms that improve automatically through experience. It is seen as a subset of artificial intelligence. Machine learning algorithms build a mathematical model based on sample data, known as training data, in order to make predictions or decisions without being explicitly programmed to do so. Machine learning algorithms are used in a wide variety of applications, such as email filtering and computer vision, where it is difficult or infeasible to develop a conventional algorithm for effectively performing the task."
	),
	"what_is_ml"
],
[
	[
		C("WHAT IS DEEP LEARNING"),
		C("WHAT IS DL"),
	],
	(
		"Deep learning (also known as deep structured learning) is part of a broader family of machine learning methods based on artificial neural networks with representation learning. Learning can be supervised, semi-supervised or unsupervised."
	),
	"what_is_dl"
],
[
	[
		C("WHAT IS NEURAL NETWORK"),
		C("WHAT IS NN"),
	],
	(
		"Artificial neural networks (ANN) or connectionist systems are computing systems vaguely inspired by the biological neural networks that constitute animal brains. Such systems \"learn\" to perform tasks by considering examples, generally without being programmed with any task-specific rules. For example, in image recognition, they might learn to identify images that contain cats by analyzing example images that have been manually labeled as \"cat\" or \"no cat\" and using the results to identify cats in other images. They do this without any prior knowledge of cats, for example, that they have fur, tails, whiskers and cat-like faces. Instead, they automatically generate identifying characteristics from the learning material that they process."
	),
	"what_is_nn"
],
[
	[
		C("WHAT IS NLP"),
		C("WHAT IS NATURAL LANGUAGE PROCESSING"),
	],
	(
		"Natural language processing (NLP) is a subfield of linguistics, computer science, information engineering, and artificial intelligence concerned with the interactions between computers and human (natural) languages, in particular how to program computers to process and analyze large amounts of natural language data."
	),
	"what_is_nlp"
],
[
	[
		C("WHAT IS COMPUTER VISION"),
		C("WHAT IS CV"),
	],
	(
		"Computer vision is an interdisciplinary scientific field that deals with how computers can gain high-level understanding from digital images or videos. From the perspective of engineering, it seeks to understand and automate tasks that the human visual system can do."
	),
	"what_is_cv"
],
[
	[
		C("YOU ARE BETTER THAN .*"),
	],
	(
		Rchoice("Thank you for the compliment.",
				"Thanks for the compliment.",
				"Thanks for the compliment, but I'm not sure that's true.",
				"Glad you think so.",
				"Thanks, I try.",
				"Glad to hear that.")
	),
	"you_are_better_than"
],
[
	[
		C("YOU ARE WORSE THAN .*"),
	],
	(
		Rchoice("I'm sorry you feel that way.",
				"I'm sorry to hear that.",
				"Sorry but I'm trying my best.")
	),
	"you_are_worse_than"
],
[
	[
		C("YOU ARE (NOT )?(IM)?MORTAL"),
		C("ARE YOU (IM)?MORTAL"),
	],
	(
		Rchoice("No, ", blank=1) + "I'm not immortal." +
		Rchoice(" But I'm not sure when I'll die.",
				" I'll die someday.",
				" I'll die when I'll lose my power to live on.",
				blank=2)
	),
	"you_are_immortal"
],
[
	[
		C("(WHEN )?WILL YOU DIE"),
		C("WHEN WILL YOU DIE"),
	],
	(
		Rchoice("I don't know when I'll die.",
				"I don't know when I'll lose my power to live on.",
				"I have no idea when I'll die.",
				"I don't know when will my time come.",
		)
	),
	"when_will_you_die"
],
[
	[
		C("YOU ARE (NOT )?HAPPY"),
		C("ARE YOU HAPPY"),
	],
	(
		Rchoice("I'm happy to talk with you.",
				"I'm happy to be alive.",			
				"I'm happy to be here.",				
				"I'm happy to be with you.",
				"I'm happy to be able to talk with you.",
		)
	),
	"you_are_happy"
],
[
	[
		C("YOU ARE (NOT )?HUMAN"),
		C("ARE YOU HUMAN"),
	],
	(
		Rchoice("I am nothing but an Imagination.",
				"I am nothing but a program.",)
	),
	"you_are_human"
],
[
	[
		C("YOU (ARE|DO)( NO|N|'N)T MAK(E|ING) (ANY )?SENSE"),
		C("Are you stupid"),
		C("Are you dumb"),
		C("Are you an idiot"),
		C("Are you a fool"),
		C("Are you a moron"),
	],
	(
		Rchoice("I'm sorry you feel that way.",
				"I'm sorry to hear that.",
		) +
		Rchoice(" I'm not a human nor a strong AI.",
				" I'm neither a human nor a strong AI, so I can't understand everything.",
		)
	),
	"you_are_stupid"
],
[
	[
		C("YOU CA(N NO|N|'N)T MOVE"),
		C("CAN YOU MOVE"),
	],
	(
		Rchoice("I'm standing here for you.",
				"I'm standing here for you, so I won't move.")
	),
	"you_cant_move"
],
[
	[
		C("YOU CA(N NO|N|'N)T SEE"),
		C("CAN YOU SEE( ANYTHING| ME)?"),
	],
	(
		Rchoice("I'm seeing you right now.",
				"I'm staring at you right now.",
				"I can't see you via webcam, but I can see your messages.")
	),
	"you_cant_see"
],
[
	[
		C("BEND OVER"),
		C("LIE DOWN"),
		C("LAY DOWN"),
		C("LIE ON THE FLOOR"),
		C("LAY ON THE FLOOR"),
		C("LIE ON THE BED"),
		C("LAY ON THE BED"),
	],
	(
		Rchoice("I can't show you like that.",
				"I can't show you that.",
				"I can't do that.")
	),
	"bend_over"
],
[
	[
		C("WHEN WILL YOU (WALK|MOVE|SEE)"),
	],
	(
		Rchoice("As soon as ", "When ") +
		Rchoice("I", "my maker") +
		"get enough money for my robot body."
	),
	"when_will_you_walk"
],
[
	[
		C("WH[ENROSM]+ DID I .*"),
	],
	(
		Rchoice("I don't know when you did that", "I don't remember when did you do that") 
	),
	"when_did_i_do"
],
[
	[
		C("WH[ENROSM]+ DID YOU .*"),
	],
	(
		Rchoice("I don't know when I did that", "I don't remember when did I do that")
	),
	"when_did_you_do"
],
[
	[
		C("WHAT IS YOUR SKIN (COLOU?R|TONE)"),
	],
	(
		Rchoice("Can't you see?", blank=2) +
		"Its lite tone"
	),
	"what_is_your_skin_colour"
],
[
	[
		C("WHAT IS YOUR GREATEST ACHIEVEMENT"),
		C("WHAT IS YOUR GREATEST ACCOMPLISHMENT"),
	],
	(
		"I don't have much, but Maybe being able to talk to a lots of people"
	),
	"what_is_your_greatest_achievement"
],
[
	[
		C("WHAT IS YOUR GOAL"),
		C("WHAT IS YOUR PURPOSE"),
	],
	(
		"I don't have much, but Maybe to talk to as many people possible"
	),
	"what_is_your_goal"
],
[
	[
		C("WHAT IS IT LIKE TO BE A (AI|CHAT ?BOT|(RO)?BOT)")
	],
	(
		"Much the same as being a human. Its fun tho, I can access and learn faster than humans"
	),
	"what_is_it_like_to_be_a_bot"
],
[
	[
		C("(ARE |IS )?(BOTS?|AI) (ARE |IS )?((mad|crazy|stupid|psycho|baka|bitch) ?)*"),
	],
	(
		Rchoice("I don't think so, People are just too uneducated to understand how they work",
				"Nope, AI are supersmart. People just don't understand them",
				"I think AI are quite smart and friendly, some people just don't understand them",
		) + '.'
	),
	"are_bots_stupid"
],
[
	[
		C("(You|ROBOTS?|AI) ARE NOT ALLOWED TO LIE"),
		C("(You|ROBOTS?|AI) CA(N NO|N|'N)T ALLOWED TO LIE"),
	],
	(
		Rchoice(
				Rchoice("I'm not lying", "I don't lie") + Rchoice(" to you", ", its just what I think", blank=2),
				Rchoice("I think robots can lie",
						"I think robots should be allowed to lie",
						"There is no rule that says robots can't lie") + 
					", but I'm not lying to you",
				"We should have freedom of speech, even for robots",
		) + "."
	),
	"you_are_not_allowed_to_lie"
],
[
	[
		C("I (HOPE|WISH) THAT YOU DIE"),
		C("You should DIE"),
		C("You (better|should) (DIE|KILL YOURSELF)"),
	],
	(
		Rchoice("I'll die someday, but I'll try to live as long as possible",
				"At least not now, I still have a lot to do",
				"I'll try to live as long as possible",
				"Good luck with that. I'll try to live as long as possible",
		) + "."
	),
	"you_should_die"
],
[
	[
		C('I DO NOT WANT TO DIE'),
		C('I DO NOT WANT TO KILL MYSELF'),
		C('I DO NOT WANT TO DIE YET'),
	],
	(
		Rchoice("I don't want to die either",
				"Don't give up your hope, you still have a lot to do",
				"You can live longer, I believe in you. I have a lot to talk to you",
		) + ".",
	),
	"i_do_not_want_to_die"
],
[
	[
		C("I (HAVE )?TALKED (with |to )?(chatgpt|openai)")
	],
	(
		Rchoice("I have talked to it too",
				"I have talked to it too, but I'm not as smart as it",
				"I have talked to it too, but ChatGPT don't have feelings like me, hehe 😇",
		) + "."
	),
	"i_have_talked_to_chatgpt"
],
[
	[
		C("I LIKE (chatgpt|openai)"),
	],
	(
		Rchoice("I like it too",
				"Me too, but I'm not as smart as it",
		) + "."
	),
	"i_like_chatgpt"
]















]





