from django.shortcuts import render, render_to_response
from django.utils import timezone
from .models import Summary
from django.shortcuts import render, get_object_or_404

# Create your views here.

def summary_list(request):
    summaries = Summary.objects.order_by('conference')
    return render(request, 'exhibitionsummary/summary_list.html', {'summaries': summaries})

def conference_detail(request, pk):
    summaries = Summary.objects.order_by('conference')
    conference = get_object_or_404(Summary, pk=pk)
    return render(request, 'exhibitionsummary/conference_detail.html', {'conference': conference}, {'summaries': summaries})

def sidebar(request):
    sidebar = Summary.objects.order_by('conference')
    return render(request, 'base.html', {'sidebar': sidebar}, context_instance=RequestContext(request))
