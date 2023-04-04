import pyttsx3
import wolframalpha

engine = pyttsx3.init()
#client = wolframalpha.Client("92QAR3-8T389K6VU8")
#result = client.query('derivative of x^4 sin x').results
#print(next(result).text)
engine.say("Neytal Persian: نيتل; also known as Naithal and Netal is a village in Tavabe-e Kojur Rural District, Kojur District, Nowshahr County, Mazandaran Province, Iran.")
engine.runAndWait()
