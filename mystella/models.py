from django.db import models
from django.contrib.auth.models import User
from django.db.models import Count
from django.template.defaultfilters import slugify





class Userprofile(models.Model):
    CHOICES = (
        ('Homme', 'Homme'),
        ('Femme', 'Femme'),
    )
    user = models.ForeignKey(User,related_name='userprofile', on_delete=models.CASCADE,null=True)
    name =models.CharField(max_length=50 ,null=True)
    Sex =models.CharField(max_length=50 ,choices=CHOICES)
    Phone =models.CharField(max_length=50)
    Email =models.EmailField(max_length=200)
    Address = models.CharField(max_length=200 , null=True)
    is_admin = models.BooleanField(blank=True, null=True,default=True)
    def __str__(self):
        return self.name

class Customer(models.Model):
    CHOICES = (
        ('Homme', 'Homme'),
        ('Femme', 'Femme'),
    )
    user = models.OneToOneField(User,null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200,null=True)
    Phone = models.CharField(max_length=50,null=True)
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    Sex =models.CharField(max_length=50 ,choices=CHOICES,null=True)
    Address = models.CharField(max_length=200, null=True,default='El-wiam')
    city = models.CharField(max_length=200, null=True,default='Sidi bel-abbes')
    county = models.CharField(max_length=200, null=True,default='Algérie')
    code = models.CharField(max_length=200, null=True,default='1500')






    def __str__(self):
        return str(self.name)





User.userprofile = property(lambda u:Userprofile.objects.get_or_create(user=u)[0])
User.customer = property(lambda c:Customer.objects.get_or_create(user=c)[0])



class Catalogue(models.Model):
    by = models.ForeignKey('auth.user', on_delete=models.SET_NULL, null=True, blank=True, )
    title = models.CharField(max_length=200, null=False)
    description = models.CharField(max_length=200)
    image = models.ImageField(null=True,blank=True)


    def __str__(self):
        return self.title


    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    @property
    def get_total(self):

        Cata = Catalogue.objects.get(pk=self.id)
        products = Cata.catalog.all()
        total_category = products.filter(catalog=self.id).count()

        return total_category



class Brand(models.Model):
    name = models.CharField(max_length=200, null=False)
    image = models.ImageField(null=True,blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    def __str__(self):
        return self.name
    @property
    def get_total(self):
        mark = Brand.objects.get(pk=self.id)
        products = mark.brand.all()
        total_brand = products.filter(brand=self.id).count()

        return total_brand



from django.db.models import F
from django.db import transaction



MEMORY = [
	('4Go', '4Go'),
	('8Go', '8Go'),
	('16Go', '16Go'),
	('32Go', '32Go'),
	('64Go', '64Go'),
	('128Go', '128Go'),
	('256Go', '256Go'),
	('1To', '1To'),

]
OP = [
	('Android', 'Android'),
	('IOS', 'IOS'),
	('Fire', 'Fire'),
	('Linux', 'Linux'),
	('Windows', 'Windows'),


]
CAM = [

	('up to 2.9 MP', 'up to 2.9 MP'),
	('3 to 4.9 MP', '3 to 4.9 MP'),
	('5 to 7.9 MP', '5 to 7.9 MP'),
	('8 to 12.9 MP', '8 to 12.9 MP'),
	('13 to 19.9 MP', '13 to 19.9 MP'),
	('20 MP and above', '20 MP and above'),


]

class Product(models.Model):
    id = models.AutoField(primary_key=True, unique = True)
    name = models.CharField(max_length=200, null=True)
    color = models.CharField(max_length=200, null=True,default='black')
    catalog = models.ForeignKey(Catalogue, null=True, blank=True, related_name='catalog', on_delete=models.CASCADE)
    price = models.FloatField(null=False,default=200)
    old_price = models.FloatField(default=100,null=False ,blank=True)
    brand = models.ForeignKey(Brand, null=True, blank=True, related_name='brand', on_delete=models.CASCADE)
    Product_details = models.CharField(max_length=1000, null=True,blank=True)
    description = models.CharField(max_length=1000, null=True,blank=True)
    image = models.ImageField(null=True,blank=True)
    is_archived = models.BooleanField(default=False, null=True, blank=True)
    is_top_selling = models.BooleanField(default=True, null=True, blank=True)
    is_top_ranking = models.BooleanField(default=True, null=True, blank=True)
    is_flash_deal = models.BooleanField(default=True, null=True, blank=True)
    is_garanted = models.BooleanField(default=True, null=True, blank=True)
    is_new = models.BooleanField(default=True, null=True, blank=True)
    is_promo = models.BooleanField(default=False, null=True, blank=True)
    remise = models.IntegerField(default=10,null=True)

    Camera = models.CharField(max_length=100, null=True,blank=True ,choices=CAM)
    Cam = models.IntegerField( null=True,blank=True,default=15 )
    Memory = models.CharField(max_length=100, null=True,blank=True ,choices=MEMORY)
    System = models.CharField(max_length=100, null=True,blank=True ,choices=OP)
    size = models.CharField(max_length=100, null=True,blank=True)
    Processor = models.CharField(max_length=100, null=True,blank=True)
    battery = models.CharField(max_length=100, null=True,blank=True)
    weight = models.CharField(max_length=100, null=True,blank=True)


    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


    def getremise(self):
        x = (self.old_price*100)/(self.price)
        y = 100-x
        tax = round(y, 2)

        return tax


    @property
    def getrate(self):
        try:
            reviews = self.review_set.all()
            total = sum([review.rating for review in reviews]) / len(reviews)
            return total
        except ZeroDivisionError:
            return 0

    @property
    def total_review(self):
            reviews = self.review_set.all()
            x = len(reviews)
            return x



    def rater_one (self):
        reviews = self.review_set.all()
        one = sum([review.rating==1 for review in reviews])
        return one
    def rater_two (self):
        reviews = self.review_set.all()
        one = sum([review.rating==2 for review in reviews])
        return one
    def rater_three(self):
        reviews = self.review_set.all()
        one = sum([review.rating==3 for review in reviews])
        return one
    def rater_four (self):
        reviews = self.review_set.all()
        one = sum([review.rating==4 for review in reviews])
        return one
    def rater_five (self):
        reviews = self.review_set.all()
        one = sum([review.rating==5 for review in reviews])
        return one


class Images(models.Model):
    product = models.ForeignKey(Product,null=True, blank=True, on_delete=models.CASCADE )
    image = models.ImageField(upload_to='image/',null=True, blank=True)

    def __str__(self):
        return self.product.title + ' image'

RATE_CHOICES = [
	(1, '1 - Trash'),
	(2, '2 - Horrible'),
	(3, '3 - Terrible'),
	(4, '4 - Bad'),
	(5, '5 - OK'),
	(6, '6 - Watchable'),
	(7, '7 - Good'),
	(8, '8 - Very Good'),
	(9, '9 - Perfect'),
	(10, '10 - Master Piece'),
]

COMPLETE_CHOICES = [
	('In progress', 'In progress'),
	('Completed', 'Completed'),
	('Delayed', 'Delayed'),
	('Pending', 'Pending'),

]

class Review(models.Model):
    username = models.CharField(max_length=1000, null=True,default='ryad')
    product = models.ForeignKey(Product,null=True, blank=True, on_delete=models.CASCADE)
    email = models.EmailField()
    text = models.CharField(max_length=1000, null=True,default='niceproduct')
    date_added = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=3)




class Order(models.Model):

    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.CharField(max_length=15, choices=COMPLETE_CHOICES,)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)


    @property
    def get_total_cart(self):
       orderitems =self.orderitem_set.all()
       total = sum([item.get_total  for item in orderitems])
       return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    accepted = models.BooleanField(default=False)


    @property
    def get_total(self):
            total = self.quantity* self.product.price
            return total














class Wish(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_wish_cart(self):
       wishitems =self.wishitem_set.all()
       total = sum([item.get_total  for item in wishitems])
       return total

    @property
    def get_wish_items(self):
        wishitems = self.wishitem_set.all()
        total = sum([item.quantity for item in wishitems])
        return total

    @property
    def get_wishh_items(self):
        wishitems = self.wishitem_set.all()
        sum=0
        for item in wishitems :
            sum=sum+1

        total=sum
        return total

class WishItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    wish = models.ForeignKey(Wish, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)


    @property
    def get_total(self):
        if self.product.price is None:
            return None
        total = self.quantity* self.product.price
        return total