
from rasa_core.agent import Agent
from rasa_core.utils import EndpointConfig
from rasa_core.interpreter import RasaNLUInterpreter

agent = Agent.load('models/dialogue',interpreter=RasaNLUInterpreter('./models/nlu/default/restaurantbot/'),
        action_endpoint=EndpointConfig(url="http://127.0.0.1:5055/webhook"))
print("Bot is ready to talk! Start conversation with 'hi'")
while True:
    st = input()
    if st == 'stop':
        break
    responses = agent.handle_text(st)
    for response in responses:
        print(response["text"])        