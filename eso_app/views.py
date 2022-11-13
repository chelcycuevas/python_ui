from django import http
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Alliances, Zones, Classes, Races, BuildEditor, Skills
from .forms import BuildEditorForm


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_zones = Zones.objects.all().count()
    num_classes = Classes.objects.all().count()

    # Available books (status = 'a')
    # num_instances_available = Classes.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_races = Races.objects.count()

    context = {
        # 'num_zones': num_zones,
        # 'num_classes': num_classes,
        # 'num_races': num_races,
    }

    form = BuildEditorForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return http.HttpResponseRedirect('/')

    context['form'] = form

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


def build_detail_view(request, *args, **kwargs):
    build = get_object_or_404(BuildEditor, pk=kwargs['pk'])
    return render(request, 'build_detail.html', context={'build': build})


class BuildEditorView(ListView):
    model = BuildEditor
    context_object_name = 'build_list'
    template_name = 'build_list.html'


class BuildEditorDetailView(DetailView):
    model = BuildEditor
    context_object_name = 'build'
    template_name = 'build_detail.html'


class AlliancesView(ListView):
    model = Alliances
    context_object_name = 'alliance_list'
    template_name = 'alliance_list.html'


class AlliancesDetailView(DetailView):
    model = Alliances
    context_object_name = 'alliance'
    template_name = 'alliance_detail.html'


class ClassesView(ListView):
    model = Classes
    context_object_name = 'class_list'
    template_name = 'class_list.html'


class ClassesDetailView(DetailView):
    model = Classes
    context_object_name = 'class'
    template_name = 'class_detail.html'


class RacesView(ListView):
    model = Races
    context_object_name = 'race_list'
    template_name = 'race_list.html'


class RacesDetailView(DetailView):
    model = Races
    context_object_name = 'race'
    template_name = 'race_detail.html'


class SkillsView(ListView):
    model = Skills
    context_object_name = 'skill_list'
    template_name = 'skill_list.html'


class SkillsDetailView(DetailView):
    model = Skills
    context_object_name = 'skill'
    template_name = 'skill_detail.html'


class ZonesView(ListView):
    model = Zones
    context_object_name = 'zone_list'
    template_name = 'zone_list.html'


class ZonesDetailView(DetailView):
    model = Zones
    context_object_name = 'zone'
    template_name = 'zone_detail.html'
