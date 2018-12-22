from django.db import models
from django.urls import reverse

class Company(models.Model):

	name = models.CharField(max_length=100)

	class Meta:
		verbose_name = 'manufacturer'
		verbose_name_plural = 'Manufacturers'

	def __str__(self):

		return self.name

	def get_absolute_url(self):

		return reverse('company-detail', args=[str(self.id)])

class Category(models.Model):

	name = models.CharField(max_length=100)

	class Meta:
		verbose_name = 'category'
		verbose_name_plural = 'Categories'

	def __str__(self):
		return self.name

	def get_absolute_url(self):

		return reverse('category-detail', args=[str(self.id)])

	def display_category(self):
		return ', '.join(category.name for category in self.category.all()[:3])
    
	display_category.short_description = 'Category'

class Solution(models.Model):

	name = models.CharField(max_length=100)

	class Meta:
		verbose_name = 'solution'
		verbose_name_plural = 'Solutions'

	def __str__(self):
		return self.name

	def get_absolute_url(self):

		return reverse('solution-detail', args=[str(self.id)])

	def display_solution(self):
		return ', '.join(solution.name for solution in self.solution.all()[:3])
    
	display_solution.short_description = 'Solution'


class Publication(models.Model):

	publication = models.CharField(max_length=300)

	link = models.URLField(max_length=300, blank=True)

	class Meta:
		verbose_name = 'publication'
		verbose_name_plural = 'Publications'

	def __str__(self):
		return self.name

	def get_absolute_url(self):

		return reverse('publication-detail', args=[str(self.id)])

	def display_solution(self):
		return ', '.join(publication.name for publication in self.solution.all()[:3])
    

class Product(models.Model):

	name = models.CharField(max_length=200)

	company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True)

	description = models.TextField('Description', max_length=2000, help_text='Enter a description of product')

	productnumber = models.CharField('Product #', max_length=9, help_text='Product # SDXX-XXXX')

	category = models.ManyToManyField(Category, help_text='Select a category for this product')

	solution = models.ManyToManyField(Solution, help_text='Select a solution for this product')

	description = models.TextField('Description', max_length=2000, help_text='Enter a description of product')

	def __str__(self):

		return self.name

	def get_absolute_url(self):

		return reverse('product-detail', args=[str(self.id)])

