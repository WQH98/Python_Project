
import os
import openai

openai.api_key = "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"

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="我问的上一个问题是什么问题",
  max_tokens=256,
)

message = response.choices[0].text
print(message)

# if __name__ == '__main__':

