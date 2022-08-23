import string
from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from django.http import Http404, HttpResponse
from rest_framework.response import Response
from rest_framework import status
from .models import OrderModel
from .serializers import OrderSerializer
from datetime import datetime


class Orderview(GenericAPIView):
    queryset = OrderModel.objects.all()
    serializer_class = OrderSerializer

    def get(self, request, format=None):
        order = OrderModel.objects.all()
        serializer = OrderSerializer(order, many=True)
        req = request.data.get(request)
        user_time_get = request.data.get('booking_time')
        wash_type_get = request.data.get('wash_type')

        print('time_get',type(user_time_get))
        user_booking_time = datetime.strptime(user_time_get,'%H:%M:%S').time()
        print("get_time_convert",type(user_booking_time))
        # Filter Data according to date coding start Here
        booking_date = self.request.query_params.get('booking_date')
        print(booking_date)
        if booking_date is not None:
            date_filter = order.filter(booking_date=booking_date)
            serializer = OrderSerializer(date_filter, many=True)
            user_id = request.user.username
            print(user_id)
            for queries in date_filter:
                filter_time = queries.booking_time
                collect_time = queries.collection_time
                # user_name = queries.user.username
                # print(user_name)
                # user_id = request.user.id
                # print(user_id)
                # filter_time_serializer = OrderSerializer(date_filter, many=True)
                # collect_time_serializer = OrderSerializer(date_filter, many=True)
                # print('Filter Time',type(filter_time))
                print('filter TIme', filter_time)
                # print('Collection Time',type(collect_time))
                print('Collection TIme',collect_time)
            # if filter_time < user_booking_time:
                # print('congratulation')
                #######################################################
                # Time calculation start Here
                s1 = user_time_get
                if wash_type_get == 1:
                    s2 = '01:00:00'
                elif wash_type_get == 2:
                    s2 = '01:30:00'
                else:
                    s2 = '02:00:00'
                FMT = '%H:%M:%S'
                time_calculate = '00:00:00'
                time_subtration = '00:15:00'
                time_addition = '00:14:00'

                # Wash_type base time get
                step1 = datetime.strptime(s2, FMT)
                # '00:00:00'time subtraction
                step2 = datetime.strptime(time_calculate, FMT)
                # Get Time from User
                step3 = datetime.strptime(s1, FMT)
                # Time Subtraction Step
                step4 = datetime.strptime(time_subtration, FMT)
                # Time Addition Step
                step5 = datetime.strptime(time_addition, FMT)
                # Time Subtraction 
                subtraction_user_booking_time = step3 - step4
                # Temporary User Booking Time
                temp_booking_time = ((step1 - step2 + step3))  #.time()
                # print('temp_booking_time',type(temp_booking_time))
                temp_time = datetime.strftime(temp_booking_time, FMT)
                temp_booked_time = datetime.strptime(temp_time, FMT).time()
                print('temp_booked_time',type(temp_booked_time))
                # Time Addition
                after_time_addition = (temp_booking_time - step2 + step5)
                user_collection_time = datetime.strftime(after_time_addition, FMT)
                # print("after_time_addition",after_time_addition)
                # print("after_time_subtraction",str(after_time_subtraction))
                subtraction_book_time = str(subtraction_user_booking_time)
                # Time Calculation End Here

                # Time Matching Start Here
                # time_collect = OrderModel.objects.all
                # or(user_booking_time > temp_booked_time and user_booking_time >= user_collection_time)
                if (user_booking_time >= filter_time and collect_time <= user_booking_time):
                    print('order possible')
                    # return Response([{'user_booking_time':user_booking_time,'user_collection_time':user_collection_time},{'serialiser':serializer.data}])    
                else:
                    print('not Possibole')    

                            # store = request.user_id
                        # Time Maching End Here
                        ######################################################   
            return Response([{'user_booking_time':user_booking_time,'user_collection_time':user_collection_time},{'serialiser':serializer.data}])
            
            # Filter Data according to date coding end Here
        return Response({'serializer':serializer.data})

    def post(self, request, format=None):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


 