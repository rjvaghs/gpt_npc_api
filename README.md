# chatnpcapi
 
## The GPT-3 Model

GPT-3 model was fine-tuned using a training dataset for the specific case of interrogation situation. This model was then used to allow questions answering from the point of view of a character.

## API

API was created on Flask python. The request for the question is taken from the user and the answer is recieved by text generation in GPT-3 model. The questions are forwarded to app.py through prompt.py. The characters.py has the information about the situation and character description in dictionery object.

## Functioning 

1. prompts.py takes the input of questions
2. app.py accepts the character name that is going to be interrogated. The questions from prompts.py is taken up by the functions responsible for creating conversation memory and this memory is accessed by the fine-tuned GPT-3 model and a response to that question is provided. With each response the chat_log stores history of that conversation.
