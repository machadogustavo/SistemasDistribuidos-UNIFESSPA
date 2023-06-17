from socket import *
from threading import Thread, Lock

serverPort = 10000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print("Server ready")

answer_key = {"1": "VVFFV", "2": "VVVV"}
total_questions = len(answer_key)

statistics = {}
lock = Lock()
counter = 0


def print_statistics():
  print("Statistics:")
  for question, stats in statistics.items():
    print(f"Question {question}: correct={stats['correct']}, incorrect={stats['incorrect']}")


def process_message(message, clientAddress):
  global counter
  questionNumber, numberOfOptions, answers = message.split(';') #separação mensagem recebida

  correct_answer = answer_key.get(questionNumber, "")
  correct = sum(1 for a, b in zip(answers, correct_answer) if a == b)
  incorrect = len(answers) - correct

  with lock:
    if questionNumber not in statistics:
      statistics[questionNumber] = {'correct': 0, 'incorrect': 0}

    if correct == len(correct_answer):
      statistics[questionNumber]['correct'] += 1
    if incorrect:
      statistics[questionNumber]['incorrect'] += 1

    counter += 1

    if counter == total_questions:
      print_statistics()
      counter = 0

  response = f"{questionNumber};{int(correct)};{int(incorrect)}" #retorno servidor
  serverSocket.sendto(response.encode('utf-8'), clientAddress)


while True:
  message, clientAddress = serverSocket.recvfrom(2048) #maximo
  message = message.decode('utf-8')

  Thread(target=process_message, args=(message, clientAddress)).start()