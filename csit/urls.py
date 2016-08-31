"""
me  : Mechanical Engineering
cse : Computer Science & Engineering
etnt: Electrical and Telecommunication Engineering
eee : Electrical & Electronics Engineering
ei  : Electrical & Instrumentation Engineering
mex : Mechatronics
it : Information Technology

These are the basic functions used in views.py file.

"""
from django.conf.urls import url,include
from . import views
#from django.conf.urls import (handler400,handler403,handler404,handler500)


urlpatterns = [
    url(r'^$', views.index),
    url(r'^index',views.index),
                    
	url(r'^institute',views.institute),   
	url(r'^chairman',views.chairman),
	url(r'^director',views.director),
	url(r'^governingbody',views.governingbody),
	url(r'^qualitypolicy',views.qualitypolicy),
	url(r'^mission',views.mission),
    url(r'^eminent_faculties',views.eminent),

	url(r'^me$',views.me),
	url(r'^cse',views.cse),
	url(r'^etnt',views.etnt),
	url(r'^eee',views.eee),
	url(r'^ei',views.ei),
	url(r'^mex$',views.mex),
	url(r'^it',views.it),

	url(r'^mtech_me',views.mtech_me),
	url(r'^mtech_cse',views.mtech_cse),
	url(r'^mtech_etnt',views.mtech_etnt),
	url(r'^physics',views.physics),
	url(r'^maths',views.maths),
	url(r'^chemistry',views.chemistry),



	url(r'^canteen',views.canteen),
	url(r'^cafe',views.cafe),
	url(r'^postoffice',views.postoffice),
	url(r'^bank',views.bank),
	url(r'^atm',views.atm),
	url(r'^gym',views.gym),
	url(r'^hostel',views.hostel),
	url(r'^contact',views.contact),
	url(r'^admissions',views.admissions),
	url(r'^rnd',views.rnd),
	url(r'^life',views.life),



	url(r'^mea$',views.mea),
	url(r'^ace',views.ace),
	url(r'^saeee',views.saeee),
	url(r'^elite',views.elite),
	url(r'^comet',views.comet),
	url(r'^brite',views.brite),
	url(r'^fame',views.fame),
	url(r'^itclub',views.itclub),
	url(r'^iclick',views.iclick),
	url(r'^energyclub',views.energyclub),
	url(r'^404',views.page_not_found),
	url(r'^500',views.server_error),
]


