from django.shortcuts import render
import experiences

# Create your views here.
def experience_index(request):
	available_exaperiences = experiences.models.Experience.objects.filter(published=True)

	return render(request, 'experiences/index.html', {
		'available_exaperiences': available_exaperiences,
		})