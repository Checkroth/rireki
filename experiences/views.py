from django.shortcuts import render
import examples

# Create your views here.
def experience_index(request):
	all_examples = examples.models.Example.objects.filter(published=True)

	return render(request, 'examples/index.html', {
		'examples': all_examples,
		})