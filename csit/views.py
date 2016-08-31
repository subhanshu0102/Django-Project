"""
All the components of models are imported to use its associated objects.
These views are linked with Urls.py file in the CSIT folder.
The tags have bee used in the alphabetical order
		a-z,aa-zz,aaa-zzz,aaaa-zzzz.
You can change this accordingly and make sure you also change it in the Template which uses this tags.

"""
from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.utils import timezone
from .models import announcements
from .models import firstslider
from .models import secondslider
from .models import placement
from .models import event
from .models import membership_certification
from .models import testimonials
from .models import download
from .models import extra_notice_bigger
from .models import about_institute
from .models import chairman_speak
from .models import director_speak
from .models import governing_body
from .models import quality_policy
from .models import mission_vision
from .models import mechanical_engg
from .models import mech_faculty_details
from .models import mech_guest_lectures
from .models import mechanical_projects
from .models import mechanical_notices
from .models import mechanical_activities
from .models import computer_engg
from .models import comp_faculty_details
from .models import computer_guest_lectures
from .models import computer_projects
from .models import computer_notices
from .models import computer_activities
from .models import etnt_engg
from .models import etnt_faculty_details
from .models import etnt_guest_lectures
from .models import etnt_projects
from .models import etnt_notices
from .models import etnt_activities
from .models import ee_engg
from .models import eee_guest_lectures
from .models import eee__projects
from .models import eee__notices
from .models import eee_activities
from .models import eee_faculty_details
from .models import eni_engg
from .models import eni_faculty_details
from .models import eni_guest_lectures
from .models import eni_projects
from .models import eni_notices
from .models import eni_activities
from .models import mechatronics_engg
from .models import mex_faculty_details
from .models import mex_guest_lectures
from .models import mex_projects
from .models import mex_notices
from .models import mex_activities
from .models import information_technology
from .models import it_faculty_details
from .models import it_guest_lectures
from .models import it_projects
from .models import it_notices
from .models import it_activities
from .models import mtech_mechanical_engg
from .models import mtech_mech_faculty_details
from .models import mtech_mech_guest_lectures
from .models import mtech_mech_projects
from .models import mtech_mech_notices
from .models import mtech_mech_activities
from .models import mtech_computer_engg
from .models import mtech_computer_faculty_details
from .models import mtech_computer_guest_lectures
from .models import mtech_computer_projects
from .models import mtech_computer_notices
from .models import mtech_computer_activities
from .models import mtech_etnt_engg
from .models import mtech_etnt_faculty_details
from .models import mtech_etnt_guest_lectures
from .models import mtech_etnt_projects
from .models import mtech_etnt_notices
from .models import mtech_etnt_activities
from .models import applied_physics
from .models import applied_physics_faculty_details
from .models import applied_maths
from .models import applied_maths_faculty_details
from .models import applied_chemistry
from .models import applied_chemistry_faculty_details
from .models import about_canteen
from .models import about_hostel
from .models import about_cafe
from .models import about_postoffice
from .models import about_bank
from .models import about_atm
from .models import about_gym 
from .models import about_mea
from .models import mea_members
from .models import about_ace
from .models import ace_members
from .models import about_comet
from .models import comet_members
from .models import about_brite
from .models import brite_members
from .models import about_elite
from .models import elite_members
from .models import about_saeee
from .models import saeee_members
from .models import about_fame
from .models import fame_members
from .models import about_itclub
from .models import itclub_members
from .models import about_energyclub
from .models import energyclub_members
from .models import about_iclick
from .models import iclick_members
from .models import eminent_faculties


def index(request):
	a = announcements.objects.all()
	b = firstslider.objects.all()
	c = secondslider.objects.all()
	d = event.objects.all()
	e = placement.objects.all()
	f = testimonials.objects.all()
	g = membership_certification.objects.all()
	h = download.objects.all()
	i = extra_notice_bigger.objects.all()
	return render(request, 'csit/index.html',{'a':a,'b':b,'c':c,'d':d,'e':e,'f':f,'g':g,'h':h,'i':i})

def institute(request):
	j = about_institute.objects.all()
	return render(request, 'csit/institute.html',{'j':j})

def chairman(request):
	k = chairman_speak.objects.all()
	return render(request, 'csit/chairman.html',{'k':k})

def director(request):
	l = director_speak.objects.all()
	return render(request, 'csit/director.html',{'l':l})

def governingbody(request):
	m = governing_body.objects.all()
	return render(request, 'csit/governingbody.html',{'m':m})

def qualitypolicy(request):
	n = quality_policy.objects.all()
	return render(request, 'csit/qualitypolicy.html',{'n':n})

def mission(request):
	o = mission_vision.objects.all()
	return render(request, 'csit/mission.html',{'o':o})

def me(request):
	p = mechanical_engg.objects.all()
	q = mech_faculty_details.objects.all()
	r = mech_guest_lectures.objects.all()
	s = mechanical_notices.objects.all()
	t = mechanical_projects.objects.all()
	u = mechanical_activities.objects.all()
	return render(request, 'csit/me.html',{'p':p,'q':q,'r':r,'s':s,'t':t,'u':u})

def cse(request):
	v = computer_engg.objects.all()
	w = comp_faculty_details.objects.all()
	x = computer_activities.objects.all()
	y = computer_notices.objects.all()
	z = computer_projects.objects.all()
	aa = computer_guest_lectures.objects.all()
	return render(request, 'csit/cse.html',{'v':v,'w':w,'x':x,'y':y,'z':z,'aa':aa})

def etnt(request):
	bb = etnt_engg.objects.all()
	cc = etnt_faculty_details.objects.all()
	dd = etnt_projects.objects.all()
	ee = etnt_activities.objects.all()
	ff = etnt_notices.objects.all()
	gg = etnt_guest_lectures.objects.all()
	return render(request, 'csit/etnt.html',{'bb':bb,'cc':cc,'dd':dd,'ee':ee,'ff':ff,'gg':gg})

def eee(request):
	hh = ee_engg.objects.all()
	ii = eee_activities.objects.all()
	jj = eee__notices.objects.all()
	kk = eee__projects.objects.all()
	ll = eee_faculty_details.objects.all()
	mm = eee_guest_lectures.objects.all()
	return render(request, 'csit/eee.html',{'hh':hh,'ii':ii,'jj':jj,'kk':kk,'ll':ll,'mm':mm})

def mex(request):
	nn = mechatronics_engg.objects.all()
	oo = mex_activities.objects.all()
	pp = mex_notices.objects.all()
	qq = mex_guest_lectures.objects.all()
	rr = mex_faculty_details.objects.all()
	ss = mex_projects.objects.all()
	return render(request, 'csit/mex.html',{'nn':nn,'oo':oo,'pp':pp,'qq':qq,'rr':rr,'ss':ss})

def ei(request):
	tt = eni_engg.objects.all()
	uu = eni_activities.objects.all()
	vv = eni_projects.objects.all()
	ww = eni_guest_lectures.objects.all()
	xx = eni_faculty_details.objects.all()
	yy = eni_notices.objects.all()
	return render(request, 'csit/ei.html',{'tt':tt,'uu':uu,'vv':vv,'ww':ww,'xx':xx,'yy':yy})

def it(request):
	zz  = information_technology .objects.all()
	aaa = it_faculty_details.objects.all()
	bbb = it_notices.objects.all()
	ccc = it_activities.objects.all()
	ddd = it_projects.objects.all()
	eee = it_guest_lectures.objects.all()
	return render(request, 'csit/it.html',{'zz':zz,'aaa':aaa,'bbb':bbb,'ccc':ccc,'ddd':ddd,'eee':eee})



def mtech_me(request):
	fff = mtech_mechanical_engg.objects.all()
	iii = mtech_mech_faculty_details.objects.all()
	jjj = mtech_mech_activities.objects.all()
	kkk = mtech_mech_notices.objects.all()
	lll = mtech_mech_projects.objects.all()
	mmm = mtech_mech_guest_lectures.objects.all()
	return render(request, 'csit/mtech_me.html',{'fff':fff,'iii':iii,'jjj':jjj,'kkk':kkk,'lll':lll,'mmm':mmm})

def mtech_cse(request):
	nnn = mtech_computer_engg.objects.all()
	ooo = mtech_computer_activities.objects.all()
	ppp = mtech_computer_faculty_details.objects.all()
	qqq = mtech_computer_guest_lectures.objects.all()
	rrr = mtech_computer_projects.objects.all()
	sss = mtech_computer_notices.objects.all()
	return render(request, 'csit/mtech_cse.html',{'nnn':nnn,'ooo':ooo,'ppp':ppp,'qqq':qqq,'rrr':rrr,'sss':sss})

def mtech_etnt(request):
	ttt = mtech_etnt_engg.objects.all()
	uuu = mtech_etnt_notices.objects.all()
	vvv = mtech_etnt_activities.objects.all()
	www = mtech_etnt_projects.objects.all()
	xxx = mtech_etnt_guest_lectures.objects.all()
	yyy = mtech_etnt_faculty_details.objects.all()
	return render(request, 'csit/mtech_etnt.html',{'ttt':ttt,'uuu':uuu,'vvv':vvv,'www':www,'xxx':xxx,'yyy':yyy})

def physics(request):
	zzz = applied_physics.objects.all()
	aaaa = applied_physics_faculty_details.objects.all()
	return render(request, 'csit/physics.html',{'zzz':zzz,'aaaa':aaaa})

def chemistry(request):
	bbbb = applied_chemistry.objects.all()
	cccc = applied_chemistry_faculty_details.objects.all()
	return render(request, 'csit/chemistry.html',{'bbbb':bbbb,'cccc':cccc})

def maths(request):
	dddd =applied_maths.objects.all()
	eeee =applied_maths_faculty_details.objects.all()
	return render(request, 'csit/maths.html',{'dddd':dddd,'eeee':eeee})


def atm(request):
	ffff = about_atm.objects.all()
	return render(request, 'csit/atm.html',{'ffff':ffff})

def gym(request):
	gggg = about_gym.objects.all()
	return render(request, 'csit/gym.html',{'gggg':gggg})

def hostel(request):
	hhhh = about_hostel.objects.all()
	return render(request, 'csit/hostel.html',{'hhhh':hhhh})


def bank(request):
	iiii = about_bank.objects.all()
	return render(request, 'csit/bank.html',{'iiii':iiii})

def postoffice(request):
	jjjj = about_postoffice.objects.all()
	return render(request, 'csit/postoffice.html',{'jjjj':jjjj})

def cafe(request):
	kkkk = about_cafe.objects.all()
	return render(request, 'csit/cafe.html',{'kkkk':kkkk})

def canteen(request):
	llll = about_canteen.objects.all()
	return render(request, 'csit/canteen.html',{'llll':llll})

def contact(request):
	return render(request, 'csit/contact_us.html',{})

def eminent(request):
	ggggg = eminent_faculties.objects.all()
	return render(request, 'csit/eminent_faculties.html',{'ggggg':ggggg})

def admissions(request):
	return render(request, 'csit/admissions.html',{})

def rnd(request):
	return render(request, 'csit/rnd.html',{})

def life(request):
	return render(request, 'csit/life.html',{})

def mea(request):
	mmmm = about_mea.objects.all()
	nnnn = mea_members.objects.all()
	return render(request, 'csit/mea.html',{'mmmm':mmmm,'nnnn':nnnn})

def ace(request):
	store = about_ace.objects.all()
	pppp = ace_members.objects.all()
	return render(request, 'csit/ace.html',{})

def saeee(request):
	qqqq = about_saeee.objects.all()
	rrrr = saeee_members.objects.all()
	return render(request, 'csit/saeee.html',{})

def elite(request):
	ssss = about_elite.objects.all()
	tttt = elite_members.objects.all()
	return render(request, 'csit/elite.html',{})

def comet(request):
	uuuu = about_comet.objects.all()
	vvvv = comet_members.objects.all()
	return render(request, 'csit/comet.html',{})

def brite(request):
	wwww = about_brite.objects.all()
	xxxx = brite_members.objects.all()
	return render(request, 'csit/brite.html',{})

def fame(request):
	yyyy = about_fame.objects.all()
	zzzz = fame_members.objects.all()
	return render(request, 'csit/fame.html',{})

def itclub(request):
	aaaaa = about_itclub.objects.all()
	bbbbb = itclub_members.objects.all()
	return render(request, 'csit/itclub.html',{})

def iclick(request):
	ccccc = about_iclick.objects.all()
	ddddd = iclick_members.objects.all()
	return render(request, 'csit/iclick.html',{})

def energyclub(request):
	eeeee = about_energyclub.objects.all()
	fffff = energyclub_members.objects.all()
	return render(request, 'csit/energyclub.html',{})




def bad_request(request):
    response = render_to_response('csit/400.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 400
    return response


def permission_denied(request):
    response = render_to_response('csit/403.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 403
    return response


def page_not_found(request):
    response = render_to_response('csit/404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def server_error(request):
    response = render_to_response('csit/500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response
   