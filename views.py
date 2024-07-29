from django.shortcuts import render, redirect
from markdown import markdown
from . import util
import random


def index(request):

    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
    

def entry (request, title):
    entry = util.get_entry(title)
    
    if entry == None:
        entry = markdown('#Page not found')

    return render (request, "encyclopedia/entry.html", {
        "title": title.capitalize(),
        "entry": markdown(entry)
    })
    
    
def search (request) :
    query = request.GET.get ("q").lower()
    list_entries = util.list_entries ()

    if query in [entry.lower() for entry in list_entries] :
        return redirect ('entry', title= query)
    
    list_matchs = [entry for entry in list_entries if query in entry.lower()]
    
    return render (request, "encyclopedia/search.html", {
        "list" : list_matchs
    })


def new_page (request) :
    if request.method == "POST":
        title = request.POST.get("entry_title")
        content = request.POST.get("entry_content")
    
        if title.lower () in [entry.lower() for entry in util.list_entries()] :
            message = "This entry already exists. Try adding a new entry."
            return render (request, "encyclopedia/new_page.html", {
                "message" : message
            })
        if title == "" or content == "" :
            message = "Can't add an empty entry."
            return render (request, "encyclopedia/new_page.html", {
                "message": message
            })    
        util.save_entry (title, content)
        
        return redirect ("entry", title= title)
    return render (request, "encyclopedia/new_page.html")


def random_page (request) :
    entries = util.list_entries ()
    print (entries)
    random_entry = random.choice (entries)
    return redirect ("entry", title = random_entry)


def edit (request, title) : # edit/CSS title=CSS
    content = util.get_entry (title)
    if request.method == "POST":
    #title = request.POST.get("entry_title") # title=None
        content = request.POST.get ('entry_content') #
        util.save_entry(title, content)
        return redirect ("entry", title = title)
    
        
    # content = request.POST.get ("entry_content")
    #     # content = request.POST.get ("entry_content")
    #     print (title)
    #     print(content)
   
    return render (request, "encyclopedia/edit.html",{
                                    "title": title,
                                    "content": content
                    }) 