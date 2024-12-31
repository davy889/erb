from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Contact
from django.contrib import messages
from contacts.models import Contact
from django.core.mail import send_mail

# Create your views here.

def contact(request):
    if request.method=="POST":
        listing_id=request.POST['listing_id']
        listing_title=request.POST['listing_title']
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        message=request.POST['message']
        user_id=request.POST['user_id']
        realtor_email=request.POST['realtor_email']
        # Check if user has made inquiry already
        if request.user.is_authenticated:
            user_id=request.user.id
            has_contacted=Contact.objects.all().filter(listing_id=listing_id,user_id=user_id)
            #if has_contacted:
            #    print('You have already made an inquiry for this listing')
            ##    messages.error(request,'You have already made an inquiry for this listing')
            #    return redirect('/listings/'+listing_id)
           
            contact=Contact(listing=listing_title,listing_id=listing_id,name=name,email=email,phone=phone,message=message,user_id=user_id)
            contact.save()
            

            #[realtor_email]

        try:
            print('Ready to send email')
            send_mail(
                'Listing Inquiry',
                f'There has been an inquiry for {listing_title}. Sign into the admin panel for more info.',
                'davy889@gmail.com',
                [realtor_email],
                fail_silently=False
            )
            print('Email sent')
            messages.success(request, 'Your request has been submitted, a realtor will get back to you soon')
        except Exception as e:
            print('Error sending email:', e)
            messages.error(request, f'Error sending email: {e}')


    return redirect('/listings/'+listing_id)
