from ollama import chat
import sys

model = ''
textFile = ''
arguments = sys.argv
messages = []

def main_loop():
  if len(arguments) > 2:
      messages = []
      try:

        with open(arguments[2], 'r') as f:
          textFile = f.read()
        
        print('----READ FILE----\n\n')
        print(textFile)
        print('\n\n----END READ----\n\n')

        
        if len(arguments) > 3:
          messages.append({
          'role': 'system',
          'content': 'You are a programmer named CodeBud. Read the contents of this file for context: ' + textFile + "\n Perform or answer this prompt, keep responses short always: " + arguments[3]
        })
        else:
          messages.append({
          'role': 'system',
          'content': 'You are a programmer named CodeBud. Read the contents of this file and wait for further instructions: ' + textFile
        })

        try:
          response = chat(model=model, messages=messages, stream=True)
          print("Model: " + arguments[1] + "\n")

          analysisResponse = ''
          for chunk in response:
              print(chunk['message']['content'], end='', flush=True)
              analysisResponse += chunk['message']['content']
        except:
          print('error: model not installed or was typed incorrectly')
          sys.exit(0)

        messages.append(
        {
          'role': 'assistant',
          'content': analysisResponse
        }
        )
        
        while (True):
          choice_input = input("\n\nPrompt(q to quit): ")
          print('\n')
          messages.append(
            {
              'role': 'user',
              'content': choice_input
            }
          )

          if choice_input == 'q':
            break
          
          response = chat(model=model, messages=messages, stream=True)
          modelResponse = ''
          if choice_input != 'q':
            for chunk in response:
                print(chunk['message']['content'], end='', flush=True)
                modelResponse += chunk['message']['content']
          
          messages.append(
            {
              'role': 'assistant',
              'content': modelResponse
            }
          )
          print('\n')

      except FileNotFoundError:
        print('error: file not found')

  else:
      print('error: please include the filename after the model name for the analysis to start')
      print('To start a basic chat with your ollama model, run: ollama run [model name]')

if __name__ == "__main__":
  print("CodeBud v1.1")
  try:
    if arguments[1] == '--help':
      print('----HELP----')
      print('How to format a basic chat command: ollama run gemma3:1b #ollama run [model name]')
      print('How to format a basic file read chat command: codebud gemma3:1b example.txt #codebud [model name] [path to file]')
      print('How to format a basic file read chat command with initial prompt: codebud gemma3:1b example.txt "Tell me what this file does." #codebud [model name] [path to file] ["prompt"]')
      print('\nMUST HAVE OLLAMA AND MODELS INSTALLED FOR CHAT TO WORK')
      print('Ollama install cmd: curl -fsSL https://ollama.com/install.sh | sh')
      print('Ollama model install cmd: ollama run [model name]')
      print('Ollama cmd to check your current installed models: ollama list')
      sys.exit(0)
  except IndexError:
    print("Error: No model specified to run the program. Or model specified is not typed correctly.\n")
    print("Please run 'codebud --help' for more information.")
    sys.exit(0)

  model = arguments[1]
  main_loop()
