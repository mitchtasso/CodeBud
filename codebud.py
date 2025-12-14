import ollama
import sys

model = ''
textFile = ''
arguments = sys.argv
messages = []

def main_loop():
  if len(arguments) > 1:
    model = arguments[1]

    if len(arguments) > 2:
        messages = []
        try:

          with open(arguments[2], 'r') as f:
            textFile = f.read()
          
          print('----READ FILE----\n\n')
          print(textFile)
          print('\n\n----END READ----\n\n')

          messages.append({
            'role': 'system',
            'content': 'You are a programmer named CodeBud. Read the contents of this file and provide a very short analysis: ' + textFile
          })

          response = ollama.chat(model=model, messages=messages, stream=True)
          analysisResponse = ''
          for chunk in response:
              print(chunk['message']['content'], end='', flush=True)
              analysisResponse += chunk['message']['content']

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
            
            response = ollama.chat(model=model, messages=messages, stream=True)
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
      messages = [
          {
            'role': 'system',
            'content': 'You are a programmer named CodeBud. Do not provide explanations for code unless asked.'
          }]
      
      while (True):
        choice_input = input("\nPrompt(q to quit): ")
        print('\n')
        messages.append(
          {
            'role': 'user',
            'content': choice_input
          }
        )

        if choice_input == 'q':
          break
        
        response = ollama.chat(model=model, messages=messages, stream=True)
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

if __name__ == "__main__":
  print("Welcome to CodeBud!")
  try:
    if arguments[1] == '--help':
      print('Version: 1.0\n')
      print('----HELP----')
      print('How to format a basic chat command: codebud gemma3:1b #codebud [model name]')
      print('How to format a file read chat command: codebud gemma3:1b example.txt #codebud [model name] [path to file]')
      print('\nMUST HAVE OLLAMA AND MODELS INSTALLED FOR CHAT TO WORK')
      print('Ollama install cmd: curl -fsSL https://ollama.com/install.sh | sh')
      print('Ollama model install cmd: ollama run [model name]')
      exit()
    else:
      test = ollama.chat(model=arguments[1], messages=[])
      print("Model: " + arguments[1] + "\n")
  except:
    print("Error: No model specified to run the program. Or model specified is not typed correctly.\n")
    print("Please run 'codebud --help' for more information.")
    exit()

  main_loop()