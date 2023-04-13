from django.http import HttpResponse
from .task import dummyData

# Create your views here.
def home(request):
    dummyData.delay()
    # tasks = [dummyAccountData,dummyLoanData]
    # chain(*tasks).apply_async()
    return HttpResponse("Hello From Celey !!!!")