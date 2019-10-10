from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings




def sms(request):
	data=student_detail.objects.all()
	if request.method=="POST":
		for i in data:
			subject = 'Today Your Bus Detail'
			message = ' Hii'+" "+ str(i.student_name)+" "+' your'+" "+ str(i.bus_no) + " "+'and time'+" "+ str(i.bus_time)
			email_from = settings.EMAIL_HOST_USER
			recipient_list = [str(i.email)]
			send_mail( subject, message, email_from, recipient_list )
		return redirect('studentviewform')
		#return HttpResponse(render(request,"sms.html",{}))
	return render(request,'sms.html',{"data":data})



# Insta_Gram Get All followers
# Insta_Gram Send Messaging (Single Users)
# Insta_Gram Send Messaging (Multiple Users)
# Insta_Gram IGTV API Integrate
# Insta_Gram Suggestion Users(For follow)
