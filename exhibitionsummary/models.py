from django.db import models


# Create your models here.



class Summary(models.Model):

	conference = models.CharField(max_length=200)

	venue = models.CharField(max_length=300, blank=True)

	start = models.DateField('Start date', null=True)

	end = models.DateField('End date', null=True)

	accommodation = models.CharField('Accomodation address', max_length=300, blank=True)

	setup = models.DateTimeField('Set up', blank=True, null=True)

	dismantle = models.DateTimeField('Dismantle', blank=True, null=True)

	booth = models.IntegerField('Booth #', blank=True, default=1)

	furniture = models.TextField('Furniture provided', max_length=300, blank=True)

	registrations = models.IntegerField('Complimentary registrations', blank=True, default=1)

	power = models.BooleanField('Power supplied', default=False)

	brochures = models.TextField('Brochures', default="QTY x BROCHURE #", help_text="Include qty", max_length=500, blank=True)

	equipment = models.TextField('Equipment', default="", max_length=500, blank=True)

	banners = models.TextField('Banners', default="", max_length=200, blank=True)

	delivery = models.BooleanField('Delivered', default=False)

	hand = models.BooleanField('Hand carried', default=False)

	address = models.CharField('Delivery address', default="", max_length=300, blank=True)

	date = models.DateField('Ship date', help_text="2-3 days for Brisbane/Sydney/Adelaide/Melbourne, otherwise 4-5 days", null=True, blank=True)

	details = models.TextField('Details', default="", help_text="Artwork required, important links etc.", max_length=400, blank=True)

	class Meta:
		verbose_name = 'Exhibition Summary'
		verbose_name_plural = 'Exhibition Summaries'



	def get_absolute_url(self):
		return reverse('exhib-summary', args=[str(self.id)])

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.conference


	@property
	def Summary(self):
		return '%s - present' % self.setup.strftime('%d/%m/%Y')

