from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import View
from .forms import ReviewsForm
from .models import Review
from django.core.paginator import Paginator
from .models import Review
# Create your views here.
def message_list(request):
    reviews=Review.objects.all()
    return render(request,'Guest_Book/Form.html',context={'reviews':reviews})

class ReviewCreate(View):


        def get(self, request):
            form=ReviewsForm()
            return render(request,'Guest_Book/new_reviews.html',context={'form':form})


        def post(self,request):
            bound_form=ReviewsForm(request.POST,request.FILES)
            user_ip = request.META.get('REMOTE_ADDR', '') or request.META.get('HTTP_X_FORWARDED_FOR', '')
            if self.request.recaptcha_is_valid:
                if bound_form.is_valid():
                    # new_reviews=Review.objects.create(
                    #     name=bound_form.cleaned_data['name'],
                    #     email=bound_form.cleaned_data['email'],
                    #     site=bound_form.cleaned_data['site'],
                    #     body=bound_form.cleaned_data['body'],
                    #     ip=user_ip,
                    #     browser=request.META.get('HTTP_USER_AGENT'),
                    #     pic = bound_form.cleaned_data['pic']
                    #     )
                    new_reviews=bound_form.save(commit=False)
                    new_reviews.ip=user_ip
                    new_reviews.browser=request.META.get('HTTP_USER_AGENT')
                    new_reviews.save()
                    return redirect('/Guest_Book/')
            return render(request,"Guest_Book/new_reviews.html", context={'form': bound_form})



class AllInfo(View):
    def get(self,request):
        order_by = request.GET.get('sort','name')
        if (order_by=='name'):
            reviews=Review.objects.all().order_by('name')
        if (order_by=='date_pub'):
            reviews=Review.objects.all().order_by('-date_pub')
        paginator=Paginator(reviews,10)
        page_number=request.GET.get('page',1)
        page=paginator.get_page(page_number)
        is_paginated=page.has_other_pages()
        if page.has_previous():
            prev_url='?page={}'.format(page.previous_page_number())
        else:
            prev_url=''
        if page.has_next():
            next_url='?page={}'.format(page.next_page_number())
        else:
            next_url=''
        context={
            "page_object":page,
            "is_paginated": is_paginated,
            "next_url": next_url,
            "prev_url": prev_url,
            'order_by': order_by
        }
        return render(request,'Guest_Book/table.html',context=context)




def clear_data(request):
    reviews=Review.objects.all().delete()
    return render(request,'Guest_Book/Form.html',context={'reviews':reviews})
