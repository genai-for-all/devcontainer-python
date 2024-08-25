import os
import ollama # type: ignore

#os.environ['OLLAMA_HOST'] = "http://host.docker.internal:11434"

stream = ollama.chat(
    model='dolphin-phi:2.7b',
    messages=[{'role': 'user', 'content': 'What is the best pizza of the world'}],
    stream=True,
)

for chunk in stream:
  print(chunk['message']['content'], end='', flush=True)