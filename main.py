from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# from spacy.cli import download
#
# download("en_core_web_sm")
# class ENGSM:
#     ISO_639_1 = 'en_core_web_sm'


# chatbot = ChatBot("Lampião", tagger_language= ENGSM)
chatbot = ChatBot(
    "Lampião",
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch'
    ],
    database_uri=None
)



conversa = [

    "coe",
    "e aí, tranquilo?",
    "tranquilo",
    "não liga",
    "eita poxa!",
    "qual é a boa de hoje?",
    "rapá, vamo que vamo em PLN!!!",
    "caramba, mo véi!!!",
    "show né!?",
    "tacágotaSerena",
]

trainer = ListTrainer(chatbot)
trainer.train(conversa)


while True:
    try:
        mensagem = input("Digite aqui:")
        resposta = chatbot.get_response(mensagem)
        print(resposta)
    except(KeyboardInterrupt, EOFError, SystemExit):
        break