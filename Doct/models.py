from django.db import models
from django.contrib.auth.models import User
# Create your models here.

from datetime import datetime

from decimal import Decimal
from django.utils import timezone

from django.contrib.sites.models import Site
import time
from django.core.exceptions import ValidationError

from Doct.utils import NETWORK_CHOICES
from Doct.utils import COUNTRY_CHOICES
from django.contrib.auth.models import Permission
import urllib
import hashlib
from django.utils.translation import ugettext as _
from django.contrib.admin.models import LogEntry



class Page(models.Model):
	title=models.CharField(max_length=128)
	url=models.URLField()
	views=models.IntegerField(default=0)


	def __unicode__(self):
		return self.title



class  UserProfile(models.Model):
	# This line is required. Links UserProfile to a User model instance.
	user = models.OneToOneField(User)

	# The additional attributes we wish to include.

	website = models.URLField(blank=True)
	picture = models.ImageField(upload_to='profile_images', blank=True)

	# Override the __unicode__() method to return out something meaningful !
	def __unicode__(self):
		return self.user.username




class Topup(models.Model):

	
	amount_sent = models.CharField("Airtime", max_length=50)
	receiver_number = models.CharField(max_length=50, blank=False)
	receiver_fname= models.CharField(max_length=100, blank=False)
	receiver_lname= models.CharField(max_length=100, blank=False)
	sender_fullname = models.CharField(max_length=100)
	receiver_country_code = models.CharField(max_length=200)
	added = models.DateTimeField()
	productcode= models.CharField(max_length=100, blank=False)
	comments= models.CharField(max_length=100, blank=False)
	

	def __str__(self):
		return "%s %s %s %s %s" % (self.amount_sent,self.receiver_number , self.receiver_fname ,self.receiver_country_code , self.added )







# Doctor consult Websit models




class Diognosis(models.Model):
    dname = models.CharField(blank=False, max_length=40)
    telno = models.CharField(blank=False, max_length=20)
    gender = models.CharField(blank=False, max_length=30) # This is the payment Id
    diognosis = models.CharField(blank=False, max_length=700)
    added = models.DateTimeField(default=timezone.now, blank=True)
    page = models.IntegerField(blank=False)
    email = models.CharField(blank=False,max_length=50,  default=False)
    amb =  models.CharField(blank=False,max_length=5,  default=False)
    is_prescribed = models.BooleanField(default=False)
    compill =  models.CharField(blank=False, max_length=700)
    fup =  models.CharField(blank=False, max_length=700)
    reply =  models.CharField(blank=False, max_length=700)
    amt = models.CharField(blank=False, max_length=30) 
    doctorusername = models.CharField(blank=False, max_length=30) 
    illness = models.CharField(blank=False, max_length=700)
    comp_signs =  models.CharField(blank=False, max_length=700) 
    ill_id  =  models.CharField(blank=False, max_length=30)
    username = models.CharField(blank=False, max_length=20)
    when  =  models.DateTimeField(default=datetime.now, blank=True)
    dtelno = models.CharField(blank=False, max_length=20)
    demail = models.CharField(blank=False, max_length=40)
    consultation_success = models.BooleanField(default=False)

    @models.permalink
    def edit_diognosis(self):
        return ('Doct/editdiog', ({self.pk}), {})


class Enterpay(models.Model):
    telno = models.CharField(blank=False, max_length=20)
    amount = models.DecimalField(
        default=0.0, decimal_places=2, max_digits=10)
    added = models.DateTimeField(default=datetime.now, blank=True)
    dname = models.CharField(blank=False, max_length=40)


class Illness(models.Model):
    added = models.DateTimeField(default=timezone.now, blank=True)
    email = models.CharField(blank=False, max_length=40)
    pname = models.CharField(blank=False, max_length=50)
    sname = models.CharField(blank=False, max_length=50)
    gender = models.CharField(blank=False, max_length=30) # gender is the payment Id
    illness = models.CharField(blank=False, max_length=700)  
    comp_signs =  models.CharField(blank=False, max_length=700) 
    kin = models.CharField(blank=False, max_length=30)
    kintelno = models.CharField(blank=False, max_length=20)
    username = models.CharField(blank=False, max_length=20)
    page = models.IntegerField(blank=False)
    amb =  models.CharField(blank=False,max_length=5,  default=False)
    amt = models.CharField(blank=False,max_length=5,  default=False)
    doctorusername = models.CharField(blank=False, max_length=20)
    location = models.CharField(blank=False, max_length=700)
    when  =  models.DateTimeField(default=datetime.now, blank=True)
    dtelno = models.CharField(blank=False, max_length=20)
    dname = models.CharField(blank=False, max_length=40)
    demail = models.CharField(blank=False, max_length=40)
    consultation_success = models.BooleanField(default=False)

    def get_names(self):
        '''
        Return a users phonenumber
        '''
        text = '%s %s' % (self.pname, self.sname)
        try:
            text = text.encode('utf-8')
        except UnicodeEncodeError:
            pass
        return text
    
   
   

    

    
    

   

	
   
class Patientr(models.Model):
    username = models.CharField(blank=False, max_length=20, unique=True)
    pwd = models.CharField(blank=False, max_length=30, unique=True)
    
class Conddrugs(models.Model):
    cond = models.CharField(blank=False, max_length=20, unique=True)
    drugs = models.CharField(blank=False, max_length=400)
    
    
class converse(models.Model):
	username = models.CharField(blank=True, max_length=20)
	dusername  = models.CharField(blank=True, max_length=20)
	dmsg = models.CharField(blank=True, max_length=700)
	pmsg = models.CharField(blank=True, max_length=700)
	illness = models.CharField(blank=True, max_length=700)


class convMembers(models.Model):
	mem_username = models.CharField(blank=True, max_length=20)
	dusername  = models.CharField(blank=True, max_length=20)


class convReg(models.Model):
	mem_username  = models.CharField(blank=True, max_length=20)
	names= models.CharField(blank=True, max_length=300, default=False)





class Messages(models.Model):
	password_phone = models.CharField(blank=True, max_length=20)
	msg = models.CharField(blank=True, max_length=700)
	password_phone = models.CharField(blank=True, max_length=20)


class PaymentVeryUnvery(models.Model):
    pay_very = models.BooleanField(default=False)
    pay_unvery = models.BooleanField(default=False)
    username  = models.CharField(blank=True, max_length=20)

	




class convPersonFrien(models.Model):
	person_password = models.CharField(max_length=30)
	friend_password = models.CharField(max_length=30)
 
	
	
# chating app









def current_rate():
    '''current rate , backwards compatability , using charge now'''
    return False





class Register(models.Model):

    # user = models.OneToOneField(User)
    user = models.OneToOneField(User)
    fname = models.CharField(blank=True, max_length=20,  default=False)
    sname = models.CharField(blank=True, max_length=30,  default=False)
    page = models.IntegerField(blank=True)
    gender = models.CharField(blank=True, max_length=30,  default=False)
    telno = models.CharField(blank=True, max_length=20,  default=False)
    username = models.CharField(blank=True, max_length=20,default=False)
    password= models.CharField(max_length=30)
    email = models.CharField(blank=True,max_length=50,  default=False)
    street = models.CharField(blank=True,max_length=50,  default=False)
    city = models.CharField(blank=True,max_length=20, default=False)
    state = models.CharField(blank=True,max_length=20,  default=False)
    zip_code = models.CharField(blank=True,max_length=5,  default=False)
    specialty = models.CharField(max_length=20, default=False)
    role = models.CharField(max_length=20, default=False)
    profile_pic = models.ImageField(upload_to="images/uploads/", blank=True)
    account_blocked = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    def get_names(self):
        '''
        Return a users phonenumber
        '''
        text = '%s %s' % (self.fname, self.lname)
        try:
            text = text.encode('utf-8')
        except UnicodeEncodeError:
            pass
        return text

    def __unicode__(self):
        return self.user.username







class Contact(models.Model):

    # user = models.OneToOneField(User)
    telno = models.CharField(blank=True, max_length=20,  default=False)
    email = models.CharField(blank=True,max_length=50,  default=False)
    msg = models.CharField(blank=False, max_length=20,  default=False)



class LoginInfo(models.Model):
    '''store login data'''
    login_time = models.DateTimeField(auto_now_add=True)
    user_agent = models.CharField(max_length=1000, blank=True, null=True)
    remote_addr = models.IPAddressField()
    user = models.ForeignKey(User, blank=False, null=False)

    

    

class UserActions(models.Model):
    '''store user actions'''
    session = models.ForeignKey(LoginInfo, blank=False, null=False)
    log_entry = models.ForeignKey(LogEntry, blank=False, null=False)
    user = models.ForeignKey(User, blank=False, null=False)

    @property
    def user_location(self):
        location = 'UnKnown'
        try:
            if self.session.remote_addr:
                import requests
                r = requests.get('http://ipinfo.io/%s/json' %
                                 self.session.remote_addr)
                loc = r.json()
                if 'ip' in loc:
                    location = '%s' % loc['ip']
                if 'country' in loc:
                    location += ',%s' % loc['country']
                if 'city' in loc:
                    location += ',%s' % loc['city']
                if 'region' in loc:
                    location += ',%s' % loc['region']
        except Exception, e:
            pass
        return location




class Ambulance(models.Model):
    '''store login data'''
    amb_time = models.DateTimeField(auto_now_add=True)
    area = models.CharField(blank=True,max_length=50,  default=False)
    city = models.CharField(blank=True,max_length=50,  default=False)
    phone = models.CharField(blank=True, max_length=20,  default=False)







class Orderdrugs(models.Model):

    # user = models.OneToOneField(User)
    telno = models.CharField(blank=True, max_length=20,  default=False)
    area = models.CharField(blank=True,max_length=50,  default=False)
    city = models.CharField(blank=True,max_length=50,  default=False)
    msg = models.CharField(blank=False, max_length=20,  default=False)
    when = models.DateTimeField(auto_now_add=True)
    staff_no = models.CharField(blank=True,max_length=70,  default=False)
    staff_name = models.CharField(blank=True,max_length=70,  default=False)


class Labtests(models.Model):

    # user = models.OneToOneField(User)
    telno = models.CharField(blank=True, max_length=20,  default=False)
    area = models.CharField(blank=True,max_length=50,  default=False)
    city = models.CharField(blank=True,max_length=50,  default=False)
    msg = models.CharField(blank=False, max_length=20,  default=False)
    when = models.DateTimeField(auto_now_add=True)
    staff_no = models.CharField(blank=True,max_length=70,  default=False)
    staff_name = models.CharField(blank=True,max_length=70,  default=False)
