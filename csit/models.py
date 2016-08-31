from django.db import models
from time import time


def fs(instance,filename):
	return "firstslider/%s_%s" % (str(time()).replace('.','_'),filename)   
def ss(instance,filename):
	return "secondslider/%s_%s" % (str(time()).replace('.','_'),filename)
def dwnld(instance,filename):
	return "downloads/%s_%s" % (str(time()).replace('.','_'),filename)
def thumbs(instance,filename):
	return "membership_certification_thumbs/%s_%s" % (str(time()).replace('.','_'),filename)
def testimonial_images(instance,filename):
	return "testimonial_images/%s_%s" % (str(time()).replace('.','_'),filename)
def extra_notice_biggers(instance,filename):
	return "extra_notice_bigger_events/%s_%s" % (str(time()).replace('.','_'),filename)


def institute_img(instance,filename):
	return "institute_imgs/%s_%s" % (str(time()).replace('.','_'),filename)
def chairman(instance,filename):
	return "chairman/%s_%s" % (str(time()).replace('.','_'),filename)
def director(instance,filename):
	return "director/%s_%s" % (str(time()).replace('.','_'),filename)
def governing_body_img(instance,filename):
	return "governing_body_imgs/%s_%s" % (str(time()).replace('.','_'),filename)
def quality_policy_img(instance,filename):
	return "quality_policy_imgs/%s_%s" % (str(time()).replace('.','_'),filename)
def mission_img(instance,filename):
	return "mission_imgs/%s_%s" % (str(time()).replace('.','_'),filename)


def mech(instance,filename):
	return "mech/%s_%s" % (str(time()).replace('.','_'),filename)
def cse(instance,filename):
	return "cse/%s_%s" % (str(time()).replace('.','_'),filename)
def eee(instance,filename):
	return "eee/%s_%s" % (str(time()).replace('.','_'),filename)
def etnt(instance,filename):
	return "etnt/%s_%s" % (str(time()).replace('.','_'),filename)
def eni(instance,filename):
	return "eni/%s_%s" % (str(time()).replace('.','_'),filename)
def mex(instance,filename):
	return "mex/%s_%s" % (str(time()).replace('.','_'),filename)
def it(instance,filename):
	return "it/%s_%s" % (str(time()).replace('.','_'),filename)





def mtech_mechical(instance,filename):
	return "mtech_mech/%s_%s" % (str(time()).replace('.','_'),filename)
def mtech_computer(instance,filename):
	return "mtech_cse/%s_%s" % (str(time()).replace('.','_'),filename)
def mtech_etnt(instance,filename):
	return "mtech_etnt/%s_%s" % (str(time()).replace('.','_'),filename)


def physics(instance,filename):
	return "physics/%s_%s" % (str(time()).replace('.','_'),filename)
def maths(instance,filename):
	return "maths/%s_%s" % (str(time()).replace('.','_'),filename)
def chemistry(instance,filename):
	return "chemistry/%s_%s" % (str(time()).replace('.','_'),filename)




def mech_header(instance,filename):
	return "mech_header/%s_%s" % (str(time()).replace('.','_'),filename)
def cse_header(instance,filename):
	return "cse_header/%s_%s" % (str(time()).replace('.','_'),filename)
def eee_header(instance,filename):
	return "eee_header/%s_%s" % (str(time()).replace('.','_'),filename)
def etnt_header(instance,filename):
	return "etnt_header/%s_%s" % (str(time()).replace('.','_'),filename)
def eni_header(instance,filename):
	return "eni_header/%s_%s" % (str(time()).replace('.','_'),filename)
def mex_header(instance,filename):
	return "mex_header/%s_%s" % (str(time()).replace('.','_'),filename)
def it_header(instance,filename):
	return "it_header/%s_%s" % (str(time()).replace('.','_'),filename)
def mtech_mech_header(instance,filename):
	return "mtech_mech_header/%s_%s" % (str(time()).replace('.','_'),filename)
def mtech_cse_header(instance,filename):
	return "mtech_cse_header/%s_%s" % (str(time()).replace('.','_'),filename)
def mtech_etnt_header(instance,filename):
	return "mtech_etnt_header/%s_%s" % (str(time()).replace('.','_'),filename)
def physics_header(instance,filename):
	return "physics_header/%s_%s" % (str(time()).replace('.','_'),filename)
def maths_header(instance,filename):
	return "maths_header/%s_%s" % (str(time()).replace('.','_'),filename)
def chemistry_header(instance,filename):
	return "chemistry_header/%s_%s" % (str(time()).replace('.','_'),filename)





def canteen(instance,filename):
	return "canteen/%s_%s" % (str(time()).replace('.','_'),filename)
def postoffice(instance,filename):
	return "postoffice/%s_%s" % (str(time()).replace('.','_'),filename)
def gym(instance,filename):
	return "gym/%s_%s" % (str(time()).replace('.','_'),filename)
def cafe(instance,filename):
	return "cafe/%s_%s" % (str(time()).replace('.','_'),filename)
def hostel(instance,filename):
	return "hostel/%s_%s" % (str(time()).replace('.','_'),filename)
def bank(instance,filename):
	return "hostel/%s_%s" % (str(time()).replace('.','_'),filename)
def atm(instance,filename):
	return "atm/%s_%s" % (str(time()).replace('.','_'),filename)

def mea(instance,filename):
	return "mea/%s_%s" % (str(time()).replace('.','_'),filename)
def ace(instance,filename):
	return "ace/%s_%s" % (str(time()).replace('.','_'),filename)
def comet(instance,filename):
	return "comet/%s_%s" % (str(time()).replace('.','_'),filename)
def saeee(instance,filename):
	return "saeee/%s_%s" % (str(time()).replace('.','_'),filename)
def brite(instance,filename):
	return "brite/%s_%s" % (str(time()).replace('.','_'),filename)
def fame(instance,filename):
	return "fame/%s_%s" % (str(time()).replace('.','_'),filename)
def elite(instance,filename):
	return "elite/%s_%s" % (str(time()).replace('.','_'),filename)
def itclub(instance,filename):
	return "itclub/%s_%s" % (str(time()).replace('.','_'),filename)
def iclick(instance,filename):
	return "iclick/%s_%s" % (str(time()).replace('.','_'),filename)
def energyclub(instance,filename):
	return "energyclub/%s_%s" % (str(time()).replace('.','_'),filename)


def mea_header(instance,filename):
	return "mea_header/%s_%s" % (str(time()).replace('.','_'),filename)
def ace_header(instance,filename):
	return "ace_header/%s_%s" % (str(time()).replace('.','_'),filename)
def comet_header(instance,filename):
	return "comet_header/%s_%s" % (str(time()).replace('.','_'),filename)
def saeee_header(instance,filename):
	return "saeee_header/%s_%s" % (str(time()).replace('.','_'),filename)
def brite_header(instance,filename):
	return "brite_header/%s_%s" % (str(time()).replace('.','_'),filename)
def fame_header(instance,filename):
	return "fame_header/%s_%s" % (str(time()).replace('.','_'),filename)
def elite_header(instance,filename):
	return "elite_header/%s_%s" % (str(time()).replace('.','_'),filename)
def itclub_header(instance,filename):
	return "itclub_header/%s_%s" % (str(time()).replace('.','_'),filename)
def iclick_header(instance,filename):
	return "iclick_header/%s_%s" % (str(time()).replace('.','_'),filename)
def energyclub_header(instance,filename):
	return "energyclub_header/%s_%s" % (str(time()).replace('.','_'),filename)

def eminent_faculty(instance,filename):
	return "eminent_faculty/%s_%s" % (str(time()).replace('.','_'),filename)






class firstslider(models.Model):
	images = models.FileField(upload_to = fs )
class secondslider(models.Model):
	images = models.FileField(upload_to = ss )
class announcements(models.Model):
	announcement  = models.TextField()	
class event(models.Model):
	events = models.TextField()
	events_date = models.DateTimeField()
class placement(models.Model):
	placements = models.TextField()
class membership_certification(models.Model):
	thumbs  = models.FileField(upload_to = thumbs)
class testimonials(models.Model):
	name = models.CharField(max_length = 25)
	batch = models.CharField(max_length = 9)
	branch = models.CharField(max_length = 35)
	message = models.TextField()
	thumbs  = models.FileField(upload_to = testimonial_images) 
class download (models.Model):
	download_heading = models.CharField(max_length = 50)
	downloads = models.FileField(upload_to = dwnld )
class extra_notice_bigger (models.Model):
	heading = models.CharField(max_length = 50)
	related_pic = models.FileField(upload_to = extra_notice_biggers)
	content = models.TextField()
	url = models.CharField(max_length = 50)





class about_institute(models.Model):
	about_institute = models.TextField()
	about_institute_image = models.FileField(upload_to = institute_img)
class chairman_speak(models.Model):
	chairman_speaks = models.TextField()
	chairman_image = models.FileField(upload_to = chairman)
class director_speak(models.Model):
	director_speaks = models.TextField()
	director_image = models.FileField(upload_to = director)
class governing_body(models.Model):
	governing_bodys = models.TextField()
	governing_body_image = models.FileField(upload_to = governing_body_img)
class quality_policy(models.Model):
	quality_policys = models.TextField()
	quality_image = models.FileField(upload_to = quality_policy_img)
class mission_vision(models.Model):
	mission_visions = models.TextField()
	mission_image = models.FileField(upload_to = mission_img)



	
class mechanical_engg(models.Model):
	aim_of_the_course = models.TextField()
	strengths = models.TextField()
	labs = models.TextField()
	software = models.TextField()
	image = models.FileField(upload_to = mech_header)
class mech_faculty_details(models.Model):
	faculty_name = models.CharField(max_length=25)
	faculty_designation = models.CharField(max_length=25)
	faculty_experience =  models.CharField(max_length=25)
	faculty_area_of_interest = models.TextField()
	faculty_image = models.FileField(upload_to = mech)
	publications = models.CharField(max_length = 10)

class mech_guest_lectures(models.Model):
	guest_lectures_name = models.CharField(max_length = 25)
	guest_lectures_event_date = models.DateTimeField(blank = True,null = True)
class mechanical_projects(models.Model):
	project = models.TextField()
class mechanical_notices(models.Model):
	notices = models.TextField()
class mechanical_activities(models.Model):
	latest_activities = models.TextField()




class computer_engg(models.Model):
	aim_of_the_course = models.TextField()
	strengths = models.TextField()
	labs = models.TextField()
	software = models.TextField()
	image = models.FileField(upload_to = cse_header)
class comp_faculty_details(models.Model):
	faculty_name = models.CharField(max_length=25)
	faculty_designation = models.CharField(max_length=25)
	faculty_experience =  models.CharField(max_length=25)
	faculty_area_of_interest = models.TextField()
	faculty_image = models.ImageField(upload_to= cse)
	publications = models.CharField(max_length = 10)
class computer_guest_lectures(models.Model):
	guest_lectures_name = models.CharField(max_length = 25)
	guest_lectures_event_date = models.DateTimeField(blank = True,null = True)
class computer_projects(models.Model):
	project = models.TextField()
class computer_notices(models.Model):
	notices = models.TextField()
class computer_activities(models.Model):
	latest_activities = models.TextField()


class etnt_engg(models.Model):
	aim_of_the_course = models.TextField()
	strengths = models.TextField()
	labs = models.TextField()
	software = models.TextField()
	image = models.FileField(upload_to = etnt_header)
class etnt_faculty_details(models.Model):
	faculty_name = models.CharField(max_length=25)
	faculty_designation = models.CharField(max_length=25)
	faculty_experience =  models.CharField(max_length=25)
	faculty_area_of_interest = models.TextField()
	faculty_image = models.ImageField(upload_to = etnt)
	publications = models.CharField(max_length = 10)
class etnt_guest_lectures(models.Model):
	guest_lectures_name = models.CharField(max_length  = 25)
	guest_lectures_event_date = models.DateTimeField(blank = True,null = True)
class etnt_projects(models.Model):
	project = models.TextField()
class etnt_notices(models.Model):
	notices = models.TextField()
class etnt_activities(models.Model):
	latest_activities = models.TextField()

class ee_engg(models.Model):
	aim_of_the_course = models.TextField()
	strengths = models.TextField()
	labs = models.TextField()
	software = models.TextField()
	image = models.FileField(upload_to = eee_header)
class eee_faculty_details(models.Model):
	faculty_name = models.CharField(max_length=25)
	faculty_designation = models.CharField(max_length=25)
	faculty_experience =  models.CharField(max_length=25)
	faculty_area_of_interest = models.TextField()
	faculty_image = models.ImageField(upload_to= eee )
	publications = models.CharField(max_length = 10)
class eee_guest_lectures(models.Model):
	guest_lectures_name = models.CharField(max_length = 25)
	guest_lectures_event_date = models.DateTimeField(blank = True,null = True)
class eee__projects(models.Model):
	project = models.TextField()
class eee__notices(models.Model):
	notices = models.TextField()
class eee_activities(models.Model):
	latest_activities = models.TextField()

class eni_engg(models.Model):
	aim_of_the_course = models.TextField()
	strengths = models.TextField()
	labs = models.TextField()
	software = models.TextField()
	image = models.FileField(upload_to = eni_header)
class eni_faculty_details(models.Model):
	faculty_name = models.CharField(max_length=25)
	faculty_designation = models.CharField(max_length=25)
	faculty_experience =  models.CharField(max_length=25)
	faculty_area_of_interest = models.TextField()
	faculty_image = models.ImageField(upload_to = eni)
	publications = models.CharField(max_length = 10)
class eni_guest_lectures(models.Model):
	guest_lectures_name = models.CharField( max_length = 25)
	guest_lectures_event_date = models.DateTimeField(blank = True,null = True)
class eni_projects(models.Model):
	project = models.TextField()
class eni_notices(models.Model):
	notices = models.TextField()
class eni_activities(models.Model):
	latest_activities = models.TextField()

class mechatronics_engg(models.Model):
	aim_of_the_course = models.TextField()
	strengths = models.TextField()
	labs = models.TextField()
	software = models.TextField()
	image = models.FileField(upload_to = mex_header)
class mex_faculty_details(models.Model):
	faculty_name = models.CharField(max_length=25)
	faculty_designation = models.CharField(max_length=25)
	faculty_experience =  models.CharField(max_length=25)
	faculty_area_of_interest = models.TextField()
	faculty_image = models.ImageField(upload_to= mex)
	publications = models.CharField(max_length = 10)
class mex_guest_lectures(models.Model):
	guest_lectures_name = models.CharField(max_length = 25)
	guest_lectures_event_date = models.DateTimeField(blank = True,null = True)
class mex_projects(models.Model):
	project = models.TextField()
class mex_notices(models.Model):
	notices = models.TextField()
class mex_activities(models.Model):
	latest_activities = models.TextField()

class information_technology(models.Model):
	aim_of_the_course = models.TextField()
	strengths = models.TextField()
	labs = models.TextField()
	software = models.TextField()
	image = models.FileField(upload_to = it_header)
class it_faculty_details(models.Model):
	faculty_name = models.CharField(max_length=25)
	faculty_designation = models.CharField(max_length=25)
	faculty_experience =  models.CharField(max_length=25)
	faculty_area_of_interest = models.TextField()
	faculty_image = models.ImageField(upload_to= it)
	publications = models.CharField(max_length = 10)
class it_guest_lectures(models.Model):
	guest_lectures_name = models.CharField(max_length = 25)
	guest_lectures_event_date = models.DateTimeField(blank = True,null = True)
class it_projects(models.Model):
	project = models.TextField()
class it_notices(models.Model):
	notices = models.TextField()
class it_activities(models.Model):
	latest_activities = models.TextField()









class mtech_mechanical_engg(models.Model):
	aim_of_the_course = models.TextField()
	strengths = models.TextField()
	labs = models.TextField()
	software = models.TextField()
	image = models.FileField(upload_to = mtech_mech_header)
class mtech_mech_faculty_details(models.Model):
	faculty_name = models.CharField(max_length=25)
	faculty_designation = models.CharField(max_length=25)
	faculty_experience =  models.CharField(max_length=25)
	faculty_area_of_interest = models.TextField()
	faculty_image = models.ImageField(upload_to = mtech_mechical)
	publications = models.CharField(max_length = 10)
class mtech_mech_guest_lectures(models.Model):
	guest_lectures_name = models.CharField(max_length = 25)
	guest_lectures_event_date = models.DateTimeField(blank = True,null = True)
class mtech_mech_projects(models.Model):
	project = models.TextField()
class mtech_mech_notices(models.Model):
	notices = models.TextField()
class mtech_mech_activities(models.Model):
	latest_activities = models.TextField()

class mtech_computer_engg(models.Model):
	aim_of_the_course = models.TextField()
	strengths = models.TextField()
	labs = models.TextField()
	software = models.TextField()
	image = models.FileField(upload_to = mtech_cse_header)
class mtech_computer_faculty_details(models.Model):
	faculty_name = models.CharField(max_length=25)
	faculty_designation = models.CharField(max_length=25)
	faculty_experience =  models.CharField(max_length=25)
	faculty_area_of_interest = models.TextField()
	faculty_image = models.ImageField(upload_to= mtech_computer)
	publications = models.CharField(max_length = 10)
class mtech_computer_guest_lectures(models.Model):
	guest_lectures_name = models.CharField(max_length = 25)
	guest_lectures_event_date = models.DateTimeField(blank = True,null = True)
class mtech_computer_projects(models.Model):
	project = models.TextField()
class mtech_computer_notices(models.Model):
	notices = models.TextField()
class mtech_computer_activities(models.Model):
	latest_activities = models.TextField()

class mtech_etnt_engg(models.Model):
	aim_of_the_course = models.TextField()
	strengths = models.TextField()
	labs = models.TextField()
	software = models.TextField()
	image = models.FileField(upload_to = mtech_etnt_header)

class mtech_etnt_faculty_details(models.Model):
	faculty_name = models.CharField(max_length=25)
	faculty_designation = models.CharField(max_length=25)
	faculty_experience =  models.CharField(max_length=25)
	faculty_area_of_interest = models.TextField()
	faculty_image = models.ImageField(upload_to= mtech_etnt)
	publications = models.CharField(max_length = 10)
class mtech_etnt_guest_lectures(models.Model):
	guest_lectures_name = models.CharField(max_length = 25)
	guest_lectures_event_date = models.DateTimeField(blank = True,null = True)
class mtech_etnt_projects(models.Model):
	project = models.TextField()
class mtech_etnt_notices(models.Model):
	notices = models.TextField()
class mtech_etnt_activities(models.Model):
	latest_activities = models.TextField()




class applied_physics(models.Model):
	aim_of_the_course = models.TextField()
	strengths = models.TextField()
	labs = models.TextField()
	software = models.TextField()
	image = models.FileField(upload_to = physics_header)
class applied_physics_faculty_details(models.Model):
	faculty_name = models.CharField(max_length=25)
	faculty_designation = models.CharField(max_length=25)
	faculty_experience =  models.CharField(max_length=25)
	faculty_area_of_interest = models.TextField()
	faculty_image = models.ImageField(upload_to= physics)
	publications = models.CharField(max_length = 10)
class applied_maths(models.Model):
	aim_of_the_course = models.TextField()
	strengths = models.TextField()
	labs = models.TextField()
	software = models.TextField()
	image = models.FileField(upload_to = maths_header)
class applied_maths_faculty_details(models.Model):
	faculty_name = models.CharField(max_length=25)
	faculty_designation = models.CharField(max_length=25)
	faculty_experience =  models.CharField(max_length=25)
	faculty_area_of_interest = models.TextField()
	faculty_image = models.ImageField(upload_to= maths)
	publications = models.CharField(max_length = 10)
class applied_chemistry(models.Model):
	aim_of_the_course = models.TextField()
	strengths = models.TextField()
	labs = models.TextField()
	software = models.TextField()
	image = models.FileField(upload_to = chemistry_header)
class applied_chemistry_faculty_details(models.Model):
	faculty_name = models.CharField(max_length=25)
	faculty_designation = models.CharField(max_length=25)
	faculty_experience =  models.CharField(max_length=25)
	faculty_area_of_interest = models.TextField()
	faculty_image = models.ImageField(upload_to= chemistry)
	publications = models.CharField(max_length = 10)




class about_canteen(models.Model):
	content = models.TextField()
	image = models.FileField(upload_to = canteen)
class about_cafe(models.Model):
	content = models.TextField()
	image = models.FileField(upload_to = cafe)
class about_hostel(models.Model):
	content = models.TextField()
	image = models.FileField(upload_to = hostel)
class about_postoffice(models.Model):
	content = models.TextField()
	image = models.FileField(upload_to = postoffice)
class about_bank(models.Model):
	content = models.TextField()
	image = models.FileField(upload_to = bank)
class about_atm(models.Model):
	content = models.TextField()
	image = models.FileField(upload_to = atm)
class about_gym(models.Model):
	content = models.TextField()
	image = models.FileField(upload_to = gym)

class about_mea(models.Model):
	about = models.TextField()
	image = models.FileField(upload_to  = mea_header)
	notices  = models.TextField()
	activities = models.TextField()
class mea_members(models.Model):
	name = models.CharField(max_length = 25)
	sem =models.CharField(max_length = 3)
	sec =models.CharField(max_length = 3)
	img = models.FileField(upload_to = mea)

class about_ace(models.Model):
	about = models.TextField()
	image = models.FileField(upload_to  = ace_header)
	notices  = models.TextField()
	activities = models.TextField()
class ace_members(models.Model):
	name = models.CharField(max_length = 25)
	sem =models.CharField(max_length = 3)
	sec =models.CharField(max_length = 3)
	img = models.FileField(upload_to = ace)

class about_fame(models.Model):
	about = models.TextField()
	image = models.FileField(upload_to  = fame_header)
	notices  = models.TextField()
	activities = models.TextField()
class fame_members(models.Model):
	name = models.CharField(max_length = 25)
	sem =models.CharField(max_length = 3)
	sec =models.CharField(max_length = 3)
	img = models.FileField(upload_to = fame)

class about_elite(models.Model):
	about = models.TextField()
	image = models.FileField(upload_to  = elite_header)
	notices  = models.TextField()
	activities = models.TextField()
class elite_members(models.Model):
	name = models.CharField(max_length = 25)
	sem =models.CharField(max_length = 3)
	sec =models.CharField(max_length = 3)
	img = models.FileField(upload_to = elite)


class about_brite(models.Model):
	about = models.TextField()
	image = models.FileField(upload_to  = brite_header)
	notices  = models.TextField()
	activities = models.TextField()
class brite_members(models.Model):
	name = models.CharField(max_length = 25)
	sem =models.CharField(max_length = 3)
	sec =models.CharField(max_length = 3)
	img = models.FileField(upload_to = brite)

class about_saeee(models.Model):
	about = models.TextField()
	image = models.FileField(upload_to  = saeee_header)
	notices  = models.TextField()
	activities = models.TextField()
class saeee_members(models.Model):
	name = models.CharField(max_length = 25)
	sem =models.CharField(max_length = 3)
	sec =models.CharField(max_length = 3)
	img = models.FileField(upload_to = saeee)


class about_comet(models.Model):
	about = models.TextField()
	image = models.FileField(upload_to  = comet_header)
	notices  = models.TextField()
	activities = models.TextField()
class comet_members(models.Model):
	name = models.CharField(max_length = 25)
	sem =models.CharField(max_length = 3)
	sec =models.CharField(max_length = 3)
	img = models.FileField(upload_to = comet)

class about_itclub(models.Model):
	about = models.TextField()
	image = models.FileField(upload_to  = itclub_header)
	notices  = models.TextField()
	activities = models.TextField()
class itclub_members(models.Model):
	name = models.CharField(max_length = 25)
	sem =models.CharField(max_length = 3)
	sec =models.CharField(max_length = 3)
	img = models.FileField(upload_to = itclub)

class about_iclick(models.Model):
	about = models.TextField()
	image = models.FileField(upload_to  = iclick_header)
	notices  = models.TextField()
	activities = models.TextField()
class iclick_members(models.Model):
	name = models.CharField(max_length = 25)
	sem =models.CharField(max_length = 3)
	sec =models.CharField(max_length = 3)
	img = models.FileField(upload_to = iclick)

class about_energyclub(models.Model):
	about = models.TextField()
	image = models.FileField(upload_to  = energyclub_header)
	notices  = models.TextField()
	activities = models.TextField()
class energyclub_members(models.Model):
	name = models.CharField(max_length = 25)
	sem =models.CharField(max_length = 3)
	sec =models.CharField(max_length = 3)
	img = models.FileField(upload_to = energyclub)
class eminent_faculties(models.Model):
	name = models.CharField(max_length = 30)
	designation = models.CharField(max_length = 40)
	department = models.CharField(max_length = 40)
	qualifications = models.CharField(max_length = 50)
	specialization = models.CharField(max_length = 50)
	experience = models.CharField(max_length = 10)
	image = models.FileField(upload_to = eminent_faculty)
