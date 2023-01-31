from django.http import HttpResponse
from forkrepo.forms import RepoForm
from django.template import RequestContext
from django.shortcuts import render
from github import Github
from github import GithubException

def index(request):

    context = RequestContext(request)
    is_forked = False
    
    if request.method == 'POST':
        repo_form = RepoForm(data=request.POST)

        if repo_form.is_valid():
            is_forked = True

            try:
                github = Github(request.POST['access_token'])
                github_user = github.get_user()
                repo = github.get_repo(request.POST['repository'])
                myfork = github_user.create_fork(repo)
            except GithubException as e:
                return HttpResponse(e)
        else:
            print(repo_form.errors)
    else:
        repo_form = RepoForm()
    return render(request,'index.html',{'repo_form': repo_form, 'is_forked': is_forked})

