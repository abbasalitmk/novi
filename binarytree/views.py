
from django.shortcuts import render, redirect
from .models import BinaryTree
from .forms import BinaryTreeNodeForm


def create_binary_tree_node(request):
    if request.method == 'POST':
        form = BinaryTreeNodeForm(request.POST)
        if form.is_valid():
            binary_tree_node = form.save(commit=False)
            binary_tree_node.save()
            
            return redirect('view')
    else:
        form = BinaryTreeNodeForm()

    return render(request, 'create.html', {'form': form})



def view_binary_tree(request):
    search = request.GET.get('search')
    is_left = request.GET.get('left')
    is_right = request.GET.get('right')

    binary_tree = BinaryTree.objects.all()

    if search:
        binary_tree = binary_tree.filter(name__iexact=search)

    selected_node = None

    if binary_tree.exists():
        selected_node = binary_tree.first()

        if is_left == 'on':
            selected_node = find_last_child(selected_node, True)

        if is_right == 'on':
            selected_node = find_last_child(selected_node, False)

        if not is_left and not is_right and selected_node.parent:
            selected_node = selected_node.parent

    return render(request, 'view.html', {'binary_tree': binary_tree, 'is_left': is_left, 'is_right': is_right, 'selected_node': selected_node})


def find_last_child(node, is_left):
    children = BinaryTree.objects.filter(parent=node, is_left=is_left)
    
    if children:
        last_child = children.last()
        return find_last_child(last_child, is_left)
    
    return node


