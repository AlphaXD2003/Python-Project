import os
import openai

openai.api_key = "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"

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Write an email to my boss for resignation\n\nSubject: Resignation - [Your Name]\n\nDear [Your Boss's Name],\n\nI am writing to inform you of my resignation from my position at [Company Name]. My last day will be [Date], as per my contract. It has been an honor and a pleasure to work with you and the team at [Company Name].\n\nI am grateful for the opportunity and experience I have gained at [Company Name] and wish the team all the best in 2020.\n\nPlease let me know if there is anything I can do to assist in the transition of my role.\n\nThank you for your support throughout my time with [Company Name].\n\nSincerely,\n[Your Name]",
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(type(response))
print(response)

'''
{
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "logprobs": null,
      "text": ""
    }
  ],
  "created": 1684667928,
  "id": "cmpl-7IbNItmkFbTGUvfgYNMnEl0DmegJV",
  "model": "text-davinci-003",
  "object": "text_completion",
  "usage": {
    "prompt_tokens": 156,
    "total_tokens": 156
  }
}
'''