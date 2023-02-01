from flask import Flask, request
import openai
import json
from characters import chars

openai.api_key = "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"
completion = openai.Completion()

start_sequence = "\nHarvey:"
restart_sequence = "\n\nPerson:"

character_name = input("Who would you like to interview? ")

session_prompt = "You are interrogating " + character_name + "\n" + chars["situation"] + "\n\n" + chars[character_name]
#Harvey is calm and focused man. \
#Harvey was in his office when he heard gunshots being fired in the bank. \
#When he went to check out, he saw 4 robbers with black skeleton masks on their face and guns. \
#He saw that two of them had SMGs and the other two had M4 rifles. \
#He got apprehended by the robbers. And he was then taken to his office and threatened to open the vault. \
#He opened the vault for the robbers. He saw that the robbers stole 10 million dollars in cash and 2 million worth of \
#gold bars. He was knocked down by being hit with a gun. \
#You can ask him anything you want and will get a witty answer. \n\n"


def ask(question, chat_log=None):
    prompt_text = f'{chat_log}{restart_sequence}: {question}{start_sequence}:'
    response = openai.Completion.create(
      engine="davinci:ft-xpertvr-georgian-team-2023-02-01-19-26-22",
      prompt=prompt_text,
      temperature=0.8,
      max_tokens=200,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0.3,
      stop=["\n"],
    )
    story = response['choices'][0]['text']
    return str(story)


def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None:
        chat_log = session_prompt
    return f'{chat_log}{restart_sequence} {question}{start_sequence}{answer}'


chat_log = None


def dialog(question):
    global chat_log
    answer = ask(question, chat_log)
    chat_log = append_interaction_to_chat_log(question, answer, chat_log)
    return answer


app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/getresponse', methods=['POST'])
def func():
    #if request.method == 'POST':
     #   char_description = request.form
      #  session_prompt = chars[char_description["Character"]]
    if request.method == 'POST':
        data = request.form
        query = data["query"]
        gen_response = dialog(query)

    resp = {"answer": gen_response}
    return resp


if __name__ == '__main__':
    app.run()

