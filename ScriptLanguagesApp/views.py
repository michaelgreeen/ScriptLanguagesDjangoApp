from asyncio.log import logger
from numbers import Integral
from sqlite3 import IntegrityError
from .Common.logger import Logger
from .forms import PCForm, NewUserForm, PCEditForm
from .models import PC, Comment, PCRating
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views import View
from django.utils.decorators import method_decorator
from django.db.models import Avg
from django.db import IntegrityError

def is_superuser(user):
    return user.is_superuser

def already_rated(request):
        return render(request=request, template_name="creator/already-rated.html")

class IndexView(View):
    def __init__(self):
        super().__init__()
        self.logger = Logger()

    def get(self, request):
        self.logger.log('INFO', 'IndexView GET request')
        return render(request, 'index.html')

class RegisterView(View):
    def __init__(self):
        super().__init__()
        self.logger = Logger()

    def get(self, request):
        self.logger.log('INFO', 'RegisterView GET request')
        form = NewUserForm()
        return render(request=request, template_name="registration/register.html", context={"register_form": form})
    
    def post(self, request):
        self.logger.log('INFO', 'RegisterView POST request')
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            self.logger.log('INFO', 'RegisterView: User registered')
            return redirect("index")
        return render(request=request, template_name="registration/register.html", context={"register_form": form})

class CreatedSetsView(View):
    def __init__(self):
        super().__init__()
        self.logger = Logger()

    def get(self, request):
        self.logger.log('INFO', 'CreatedSetsView GET request')
        pcs = PC.objects.all()
        return render(request,"creator/created-sets.html", {'pcs':pcs})
@method_decorator(login_required, name='dispatch')
class DetailsView(View):
    def __init__(self):
        super().__init__()
        self.logger = Logger()

    def get(self, request, pc_id):
        self.logger.log('INFO', 'DetailsView GET request')
        pc = get_object_or_404(PC, id=int(pc_id))
        return render(request, 'creator/details.html', {'pc':pc})

@method_decorator(login_required, name='dispatch')
class RatePCView(View):
    def __init__(self):
        super().__init__()
        self.logger = Logger()
        
    def post(self, request, pc_id):
        pc = PC.objects.get(id=pc_id)
        rating = int(request.POST.get('rating'))
        user = request.user
        try:
            self.logger.log('INFO', 'RatePcView POST: Trying to create a rating')
            PCRating.objects.create(pc=pc, rating=rating,user=user)
            self.logger.log('INFO', 'RatePcView POST: Rating successfully created')
        except IntegrityError as e:
            self.logger.log('ERROR', f'RatePcView POST: UNIQUE constraint, Each user may assess the PC set exactly one time ')
            return redirect('already-rated')
        pc.average_rating = PCRating.objects.filter(pc=pc).aggregate(Avg('rating'))['rating__avg']
        pc.save()
        return redirect('created-sets')

@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(is_superuser), name='dispatch')
class AddSetView(View):
    def __init__(self):
        super().__init__()
        self.logger = Logger()

    def get(self, request):
        self.logger.log('INFO', 'AddSetView GET request')
        form = PCForm()
        return render(request, 'creator/add-set.html', {'form': form})
    
    def post(self, request):
        self.logger.log('INFO', 'AddSetView POST request')
        form = PCForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('created-sets')
        self.logger.log('ERROR', 'Invalid form submission')
        return render(request, 'creator/add-set.html', {'form': form})

class CommentAddView(View):
    def __init__(self):
        super().__init__()
        self.logger = Logger()

    def post(self, request, pc_id):
        self.logger.log('INFO', 'CommentAddView POST request')
        pc = get_object_or_404(PC, id=int(pc_id))
        text = request.POST.get('text')
        if text:
            comment = Comment.objects.create(pc=pc, user=request.user, text=text)
        return redirect('details', pc_id=pc_id)

@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(is_superuser), name='dispatch')
class CommentDeleteView(View):
    def __init__(self):
        super().__init__()
        self.logger = Logger()

    def get(self, request, comment_id):
        self.logger.log('INFO', 'CommentDeleteView GET request')
        comment = get_object_or_404(Comment, id=comment_id)
        comment.delete()
        return redirect('details', pc_id=comment.pc.id)

@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(is_superuser), name='dispatch')
class PCSetDeleteView(View):
    def __init__(self):
        super().__init__()
        self.logger = Logger()

    def get(self, request, pc_id):
        self.logger.log('INFO', 'PCSetDeleteView GET request')
        pc = get_object_or_404(PC, id=pc_id)
        pc.delete()
        return redirect('created-sets')

@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(is_superuser), name='dispatch')
class PCEditView(View):
    def __init__(self):
        super().__init__()
        self.logger = Logger()

    @staticmethod
    def get_pc_by_id(pc_id):
        return get_object_or_404(PC, id=pc_id)

    def get(self, request, pc_id):
        self.logger.log('INFO', 'PCEditView GET request')
        pc = self.get_pc_by_id(pc_id)
        form = PCEditForm(instance=pc)
        return render(request, 'creator/edit-set.html', {'form': form})

    def post(self, request, pc_id):
        self.logger.log('INFO', 'PCEditView POST request')
        pc = self.get_pc_by_id(pc_id)
        form = PCEditForm(request.POST, instance=pc)
        try:
            if form.is_valid():
                form.save()
                return redirect('created-sets')
            else:
                raise ValueError('Invalid form submission')
        except Exception as e:
            self.logger.log('ERROR', f'Error in PCEditView: {str(e)}')
            return render(request, 'creator/edit-set.html', {'form': form})