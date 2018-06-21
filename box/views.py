from django.shortcuts import render, redirect
from django.views import View
from .models import Person, Address, Phone, Email, Group


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
        person = Person(
            name=name,
            surname=surname,
            description=description,
        )
        person.save()
        return render(request, 'new_person.html', {
            'added': 'New person has been added'
        })


class ModifyPerson(View):
    def get(self, request, id):
        person = Person.objects.get(id=id)
        return render(request, 'modify_person.html', {
            'person': person
        })
    def post(self, request, id):
        person = Person.objects.get(id=id)
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        description = request.POST.get('description')
        # city = request.POST.get('city')
        # street = request.POST.get('street')
        # house_number = request.POST.get('house_number')
        # flat_number = request.POST.get('flat_number')
        if name:
            person.name = name
        if surname:
            person.surname = surname
        if description:
            person.description = description
        # if city:
        #     person.address.city = city
        # if street:
        #     person.address.street = street
        # if house_number:
        #     person.address.house_number = house_number
        # if flat_number:
        #     person.address.flat_number = flat_number
        # person.address.save()
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
        addresses = Address.objects.filter(person__id=id)
        phones = Phone.objects.filter(person__id=id)
        emails = Email.objects.filter(person__id=id)
        groups = Group.objects.filter(person__id=id)
        return render(request, 'show_person.html', {
            'person': person,
            'addresses': addresses,
            'phones': phones,
            'emails': emails,
            'groups': groups
        })


class AddAddress(View):
    def get(self, request, id):
        person = Person.objects.get(id=id)
        return render(request, 'add_address.html', {
            'person': person
        })
    def post(self, request, id):
        person = Person.objects.get(id=id)
        city = request.POST.get('city')
        street = request.POST.get('street')
        house_number = request.POST.get('house_number')
        flat_number = request.POST.get('flat_number')
        if city and street and house_number and flat_number:
            address = Address.objects.create(
                city=city,
                street=street,
                house_number=house_number,
                flat_number=flat_number,
                person=person
            )
            address.save()
        return redirect('show-person', id=id)


class AddPhone(View):
    def get(self, request, id):
        person = Person.objects.get(id=id)
        return render(request, 'add_phone.html', {
            'person': person
        })
    def post(self, request, id):
        person = Person.objects.get(id=id)
        home_phone = request.POST.get('home_phone')
        work_phone = request.POST.get('work_phone')
        if home_phone or work_phone:
            phone = Phone.objects.create(
                home_phone=home_phone,
                work_phone=work_phone,
                person=person
            )
            phone.save()
        return redirect('show-person', id=id)


class AddEmail(View):
    def get(self, request, id):
        person = Person.objects.get(id=id)
        return render(request, 'add_email.html', {
            'person': person
        })
    def post(self, request, id):
        person = Person.objects.get(id=id)
        home_email = request.POST.get('home_email')
        work_email = request.POST.get('work_email')
        if home_email or work_email:
            email = Email.objects.create(
                home_email=home_email,
                work_email=work_email,
                person=person
            )
            email.save()
        return redirect('show-person', id=id)


class NewGroup(View):
    def get(self, request):
        return render(request, 'new_group.html')
    def post(self, request):
        name = request.POST.get('name')
        group = Group(
            name=name,
        )
        group.save()
        return render(request, 'new_group.html', {
            'added': 'New group has been added'
        })


class DeleteGroup(View):
    def get(self, request, id):
        Group.objects.get(id=id).delete()
        return render(request, 'delete_group.html', {
            'deleted': 'Group has been removed',
        })


class AddToGroup(View):
    def get(self, request, id):
        group = Group.objects.get(id=id)
        people = Person.objects.all()
        return render(request, 'add_to_group.html', {
            'group': group,
            'people': people
        })
    def post(self, request, id):
        person_id = request.POST.get('person')
        person = Person.objects.get(id=person_id)
        group = Group.objects.get(id=id)
        group.person.add(person)
        group.save()
        return render(request, 'groups.html', {
            'added': 'Person has been added'
        })


class DeleteFromGroup(View):
    def get(self, request, id):
        Group.objects.get(id=id).delete()
        return render(request, 'delete_from_group.html', {
            'deleted': 'Person has been removed from the group'
        })


class Groups(View):
    def get(self, request):
        groups = Group.objects.all()
        return render(request, 'groups.html', {
            'groups': groups,
        })
