from django.shortcuts import render
from .models import Destination , Testimonial 
# Create your views here.

def home(request):
    dest1 = Destination()
    dest1.name = 'Mumbai'
    dest1.price = 900
    dest1.img = 'destination_1.jpg'
    dest1.desc = 'The City That Never Sleeps'
    dest1.offer = False

    dest2 = Destination()
    dest2.name = 'Delhi'
    dest2.price = 1000
    dest2.img = 'destination_2.jpg'
    dest2.desc = 'THE CAPITAL'
    dest2.offer = True

    dest3 = Destination()
    dest3.name = 'Banglore'
    dest3.price = 1050
    dest3.img = 'destination_9.jpg'
    dest3.desc = 'Beauty'
    dest3.offer = False

    dests = [dest1 , dest2 , dest3]
    
    test1= Testimonial()
    test1.desc = 'Aeromanteia made my travel planning a breeze! With a user-friendly interface, extensive destination information, and seamless booking process, its my go-to website for all my travel needs.'
    test1.name = 'Shikha Amin'

    test2 = Testimonial()
    test2.desc = 'Aeromanteia is a game-changer! Easy booking, incredible destination information, and personalized itineraries make it my go-to travel website. Highly recommended!'
    test2.name = 'Himani Kandhari'

    test3 = Testimonial()
    test3.desc = 'Aeromanteia made planning my dream vacation a breeze! The user-friendly interface, extensive destination options, and seamless booking process exceeded my expectations. Highly recommended!'
    test3.desc = 'Manan Jain'

    test4 = Testimonial()
    test4.desc = 'Aeromanteia made my travel planning a breeze! Easy-to-use interface, extensive destination database, and seamless booking process. A go-to platform for stress-free vacations!'
    test4.name = 'Ashish Purohit'

    tests = [test1 , test2, test3, test4]

    return render(request,'index.html',{'tests':tests,'dests':dests})

# def about(request):
#     return render(request,'about.html')
    
    