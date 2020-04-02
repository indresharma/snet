from django.shortcuts import render, redirect, get_object_or_404
from .models import GroupMember, Group
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from post.forms import PostForm
from post.models import Post
from django.contrib.auth.decorators import login_required

class AllGroupsView(ListView):
    model = Group

class GroupView(View):
    def get(self, request, *args, **kwargs):
        obj = Group.objects.get(pk=self.kwargs.get('pk'))
        group_posts = Post.objects.filter(group=obj)
        return render(request, 'groups/group_detail.html', {'obj':obj, 'group_posts':group_posts})
        

class GroupCreateView(CreateView):
    model = Group
    fields = ('name', 'description')

    def form_valid(self, form):
        group = form.save()
        groupmember, created = GroupMember.objects.get_or_create(user=self.request.user, group=group)
        groupmember.save()
        return super().form_valid(form)

class GroupUpdateView(UpdateView):
    model = Group
    fields = ('description',)

def join_group(request, id):
    group = Group.objects.get(id=id)
    member, created = GroupMember.objects.get_or_create(user=request.user, group=group)
    if created==False:
        messages.error(request, 'You are already a memeber of this group')
    #get_or_create returns a tuple (object, False)
    member.save()
    return redirect('groups:all_group')

def leave_group(request, id):
    try:
        member = GroupMember.objects.get(user=request.user, group=id)
        member.delete()
        messages.success(request, 'You have left the group sucessfully')
    except ObjectDoesNotExist:
        messages.error(request, 'You are not a member of this group')
    
    return redirect('groups:all_group')

@login_required
def group_post(request, pk):
    form = PostForm()
    group = get_object_or_404(Group, pk=pk)
    try:
        groupmember = get_object_or_404(GroupMember, group=group, user=request.user)
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.group = group
                post.created_by = request.user
                post.save()
                return redirect('groups:main_group', pk)
    except ObjectDoesNotExist:
        messages.error(request, 'Please Join this group to post')
        return redirect('groups:main_group', pk)
    return render(request, 'post/post_form.html', {'form':form})  
    



