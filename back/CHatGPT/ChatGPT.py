import openai
from rest_framework.templatetags.rest_framework import data
from django.http import JsonResponse

openai.api_key = "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"


def OpenChat(request):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "you are a nutrittionist and you are talking to a client about their diet."},
            {"role": "user", "content": request['userInteraction']},
        ]
    )

    return JsonResponse(data={"response": response.choices[0].message.content}, safe=False)


def chat(request):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "you are a nutrittionist and you are talking to a client about their diet."},

            {"role": "user", "content": request['userInteraction']},
            {"role": "assistant", "content": request["response"]}
        ]
    )
    return JsonResponse(data={"response": response.choices[0].message.content}, safe=False)
