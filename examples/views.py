from django.shortcuts import render
import examples

# Create your views here.
def examples_list(request):
	available_examples = examples.models.Example.objects.filter(published=True)

	return render(request, 'examples/index.html', {
		'examples': available_examples,
		})

def show_example(request, example_id):
	try: 
		example = examples.Example.get(id=example_id)
	# Figure out the right exception for instance not found
	except examples.models.Example.DoesNotExist:
		# Error page render here (from static pages)
		pass

	return render(request, 'examples/_example.html', {
		'example': example,
		})