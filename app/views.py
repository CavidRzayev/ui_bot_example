from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from .models import Message,BaseModels
import requests
import openai
openai.api_key = "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"

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
        data = request.POST.get("content")
        try:
            if len(data) == 0:redirect("index")
            else:
        
                query = {
                   "content":data,
               }
                url = "http://3.72.64.128:8585/api/v2/stream_chat/"
                header = {"Token": "r8uuwR07fZplje68Li1yQ8wjuXypGEKOTshGGmMFGpuAq5DDvG2FIZDGPIzaobuifDf7O1mjlASfIby2iU1zq2rSIm5krGTUBHMuFRQGix5OrcuEeW9r6yfRuPtYF4aeQldhipCbiW6FL1V84gb5gPu7kg6sCbWge09I46QbLo0rcsjzLMvwJRW8Dv"}
                response = requests.post(url,headers=header,json=query)
                print(response.content)

   
                return JsonResponse({"message": "OK", "data": data, "response": parse_response(response.text)})
        except Exception as e:
            print(e)
            return JsonResponse({"message": "Error", "error": str(e)})

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from app.serializers import StreamSerializer
import json

def parse_response(response):
    # Extracting text from each data object
    data_objects = [json.loads(obj.replace("data: ", ""))["text"] for obj in response.split("\r\n") if obj.startswith("data:")]

    # Combining the extracted text
    combined_text = ''.join(data_objects)

    return combined_text




def stream_data(request):
    data = request.POST.get("questions")



class AskStreamAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = StreamSerializer

    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            data = serializer.validated_data
            print(data)
            url = "http://3.72.64.128:8585/api/v2/stream_chat/"
            header = {"Token": "r8uuwR07fZplje68Li1yQ8wjuXypGEKOTshGGmMFGpuAq5DDvG2FIZDGPIzaobuifDf7O1mjlASfIby2iU1zq2rSIm5krGTUBHMuFRQGix5OrcuEeW9r6yfRuPtYF4aeQldhipCbiW6FL1V84gb5gPu7kg6sCbWge09I46QbLo0rcsjzLMvwJRW8Dv"}
            response = requests.post(url,json=data,headers=header)
            print(parse_response(response.text))
            return JsonResponse({"message": "OK", "data": data, "response": parse_response(response.text)})
        except Exception as e:
            print(e)
            return JsonResponse({"message": "Error", "error": str(e)})

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
