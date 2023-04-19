# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib import messages
from .forms import PCForm, NewUserForm
from .models import PC, Comment
from django.contrib.auth.decorators import login_required, user_passes_test

def index_(request):
    return render(request, 'index.html')

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Udało Ci się zarejestrować! :)")
            return redirect("index")
        messages.error(request, "Niepowodzenie. Sprawdź wpisane dane.")
    form = NewUserForm()
    return render(request=request, template_name="registration/register.html", context={"register_form": form})

def created_sets_request(request):
    pcs = PC.objects.all()
    return render(request,"creator/created-sets.html", {'pcs':pcs})

def details_request(request, pc_id):
    if pc_id:
        pc = PC.objects.get(id=int(pc_id))
        return render(request, 'creator/details.html', {'pc':pc})
    else:
        redirect('created-sets')

def add_set_request(request):
    if request.method == 'POST':
        form = PCForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('created-sets')
    else:
        form = PCForm()
    return render(request, 'creator/add-set.html', {'form': form})

@login_required
def comment_add_request(request, pc_id):
    if request.method == 'POST':
        pc = PC.objects.get(id=int(pc_id))
        text = request.POST.get('text')
        if text:
            comment = Comment.objects.create(pc=pc, user=request.user, text=text)
    return redirect('details', pc_id = pc_id)
    
#ANTIPATTERN but will change it in the future. GET shouldnt be used for deletion.
#ADD DELETION FOR A USER THAT CREATED THE COMMENT
@login_required
@user_passes_test(lambda u: u.is_superuser)
def comment_delete_request(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == 'GET':
        comment.delete()
        return redirect('details', pc_id=comment.pc.id)
    return redirect('details', pc_id=comment.pc.id)

#ANTIPATTERN but will change it in the future. GET shouldnt be used for deletion.
@login_required
@user_passes_test(lambda u: u.is_superuser)
def pc_set_delete_request(request,pc_id):
    pc = get_object_or_404(PC, id=pc_id)
    if request.method == 'GET':
        pc.delete()
        return redirect('created-sets')
    return redirect('created-sets')

@login_required
@user_passes_test(lambda u: u.is_superuser)
def pc_set_edit_view(request,pc_id):
    if request.method == 'POST':
        pc = get_object_or_404(PC, id=pc_id)
    pass
    return render(request, 'creator/edit-set.html', {'form': form})