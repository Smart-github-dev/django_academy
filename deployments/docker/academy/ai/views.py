# Create your views here.
import openai
from django.conf import settings
from django.shortcuts import render

def ai_chat(request):
    template_name = "chat.html"
    return render(request, template_name, locals())

def ai_chat_interview(request):
    template_name = "chat_interview.html"
    return render(request, template_name, locals())

def ai_chatbox_start(request):
    template_name = "chatbox_start.html"
    return render(request, template_name, locals())

def ai_chatbox_dialog(request):
    template_name = "chatbox_dialog.html"
    return render(request, template_name, locals())


def ai_view(request):
    template_name = "chatbot.html"
    openai.api_key = getattr(settings, 'OPEN_AI_TOKEN', None)
    extention = 'I want you to act as an interviewer. I will be the candidate and you will ask me the interview questions for the position position. I want you to only reply as the interviewer. Do not write all the conservation at once. I want you to only do the interview with me. Ask me the questions and wait for my answers. Do not write explanations. Ask me the questions one by one like an interviewer does and wait for my answers. My first sentence is'
    if request.POST:
        message = request.POST.get("message")
        message = extention + message
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=message,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        bot_response = response.choices[0].text.strip()
        return render(request, template_name, {"message": message, "bot_response": bot_response})
    return render(request, template_name, locals())
