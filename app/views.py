from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from .models import Message,BaseModels
import requests
import openai
openai.api_key = ""

def index(request):
    if request.user.is_authenticated:pass
    else: return redirect("login")
        
    if not request.session.session_key:
        request.session.create()
    message = BaseModels.objects.filter(user=request.user).order_by("-id")
    if message:
        context = {
            "sidebar_data" : message,
            "last":Message.objects.filter(user=request.user).last()
        }
    else:
        context = {

        }
    return render(request,"index.html",context=context)

@csrf_exempt
def save(request):
    
    if not request.session.session_key:
        request.session.create()
    if request.method == "POST":
        now = datetime.now().time()
        data = request.POST.get("questions")
        path = request.POST.get("path").strip("/detail/")
        if len(data) == 0:redirect("index")
        else:
            message =  Message()
            message.session_id = request.session.session_key
            message.quesion = data
            query = {
                "questions":data,
                "session":request.session.session_key
            }
            url = "http://ai.abb-bank.az:8080/api/v1"
            header = {"Token": "r8uuwR07fZplje68Li1yQ8wjuXypGEKOTshGGmMFGpuAq5DDvG2FIZDGPIzaobuifDf7O1mjlASfIby2iU1zq2rSIm5krGTUBHMuFRQGix5OrcuEeW9r6yfRuPtYF4aeQldhipCbiW6FL1V84gb5gPu7kg6sCbWge09I46QbLo0rcsjzLMvwJRW8Dv"}
            response = requests.post(url,headers=header,json=query)
            print(response.content)
            message.answer = response.json()["message"]
            message.user  = request.user
            message.save()
            try:
                base = BaseModels.objects.get(id=path)
                base.message.add(message)
                base.save()
            except Exception as e:
                print(e)
            print(response.json())
            return JsonResponse({"message":response.json()["message"]})


@csrf_exempt
def gtp(request):
    user_prompt = request.GET.get("q")

    chatbot_response = None
    if user_prompt:
        
        chatbot_response = api_calling(q)
    
    
    context = {
        "chatbot_response":chatbot_response

    }
    if request.method == "POST":
        data = request.POST.get("questions")
        q = f""" Today is {datetime.now()}. Limit your answer with maximum 300 word.  
                                                        Answer the question  delimited by triple backticks in azerbaijan language ```{data}```
                                                        If you can not find the answer at the information give information in azerbaijan languaguge.
                                                    """
        chatbot_response = api_calling(q)
        return JsonResponse({"message":chatbot_response}) 
    return render(request,"gpt.html",context)



def api_calling(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = completions.choices[0].text
    return message

   


def detail(request,id):
    message = BaseModels.objects.filter(id=id).last()
    sidebar_data = BaseModels.objects.filter(user=request.user).order_by("-id")
    context = {
        "sidebar_data":sidebar_data,
        "data":message,
        "link_active":"active",
        "last":Message.objects.filter(user=request.user).last()
    }
    return render(request,"detail.html",context)


def create_detail(request):
    create = BaseModels.objects.create(user=request.user,status=True)
    return redirect("detail",create.id)


