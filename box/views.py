from django.shortcuts import render
from django.views import View
from .models import Person, Address


class Index(View):
    def get(self, request):
        return render(request, 'index.html')


class People(View):
    def get(self, request):
        people = Person.objects.all()
        return render(request, 'people.html', {
            'people': people
        })


class NewPerson(View):
    def get(self, request):
        return render(request, 'new_person.html')
    def post(self, request):
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        description = request.POST.get('description')
        city = request.POST.get('city')
        street = request.POST.get('street')
        house_number = request.POST.get('house_number')
        flat_number = request.POST.get('flat_number')
        address = Address(
            city=city,
            street=street,
            house_number=house_number,
            flat_number=flat_number
        )
        address.save()
        person = Person(
            name=name,
            surname=surname,
            description=description,
            address=address
        )
        person.save()
        return render(request, 'new_person.html', {
            'added': 'New person has been added'
        })


class ModifyPerson(View):
    def get(self, request, id):
        person = Person.objects.get(id=id)
        print(person)
        print(person.name)
        return render(request, 'modify_person.html', {
            'person': person
        })
    def post(self, request, id):
        person = Person.objects.get(id=id)
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        description = request.POST.get('description')
        city = request.POST.get('city')
        street = request.POST.get('street')
        house_number = request.POST.get('house_number')
        flat_number = request.POST.get('flat_number')
        if name:
            person.name = name
        if surname:
            person.surname = surname
        if description:
            person.description = description
        if city:
            person.address.city = city
        if street:
            person.address.street = street
        if house_number:
            person.address.house_number = house_number
        if flat_number:
            person.address.flat_number = flat_number
        person.address.save()
        person.save()
        person = Person.objects.get(id=id)
        return render(request, 'modify_person.html', {
            'person': person,
            'modified': 'Person has been modified'
        })


class DeletePerson(View):
    def get(self, request, id):
        Person.objects.get(id=id).delete()
        return render(request, 'delete_person.html', {
            'deleted': 'Person has been removed',
        })


class ShowPerson(View):
    def get(self, request, id):
        person = Person.objects.get(id=id)
        return render(request, 'show_person.html', {
            'person': person
        })
