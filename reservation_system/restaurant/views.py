from calendar import c
import json
from tabnanny import check
from django.shortcuts import render
from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt
from django.utils.dateparse import parse_datetime
from datetime import timedelta, datetime
from .models import Table, Reservation

# Create your views here.
def view_tables(request):
    tables = Table.objects.all()
    res = {}
    res['tables_count'] = tables.count()
    res['tables'] = []
    
    for table in tables:
        obj = {'table number': table.id, 'reservations': []}
        
        reservations = table.reservation_set.all()
    
        for reserv in reservations:
            obj['reservations'].append({
                "checkin": reserv.checkin_time,
                "checkout": reserv.checkout_time
            })

        res['tables'].append(obj)

    
    return JsonResponse(res)

PEOPLE_COUNT_POSSIBILITIES = [2, 4, 6, 12]

@csrf_exempt
def reservating_table(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body.decode("utf-8"))
            table_id = data['table number']
            checkin = parse_datetime(data['checkin']) 
            checkout = parse_datetime(data['checkout'])
            people_count = data['people_count']

            # People count check
            if people_count not in PEOPLE_COUNT_POSSIBILITIES:
                return JsonResponse({'message' : f'People count can only be 2, 4, 6, 12'})

            # Reservation Time check
            if checkin > checkout:
                return JsonResponse({'message' : f'invalid checkin and checkout time'})
            
            date = checkin.date()
            starttime = datetime(date.year, date.month, date.day, 17)
            endtime = datetime(date.year, date.month, date.day, 23)

            if not (starttime <= checkin and checkout <= endtime):
                return JsonResponse({'message' : f'Reservations can occur between 5pm to 11pm'})

            checkin -= timedelta(minutes=10)
            checkout += timedelta(minutes=10)

            # intersection check
            table = Table.objects.get(pk = table_id)
            reservations = table.reservation_set.all()
            
            for reserv in reservations:
                if(reserv.checkin_time > checkout or reserv.checkout_time < checkin):
                    pass
                else:
                    return JsonResponse({'message' : f'already reserved in the duration {reserv.checkin_time} to {reserv.checkout_time}'})

            Reservation.objects.create(table = table, people_count = people_count, checkin_time = checkin, checkout_time = checkout)

            return JsonResponse({'message' : 'sucessfully created the reservation'})

    except Exception as e:
        print(e)
        return JsonResponse({'message' : 'no such table or something went wrong'})
