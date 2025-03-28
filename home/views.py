from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Person, Question,Answer
from .serializers import PerosnSerializer, QuestionSerializer, AnswerSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from permissions import IsOwnerOrReadOnly
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle


class Home (APIView) :
    permission_classes = [IsAuthenticated,]
    # throttle_scope = 'questions'
    serializer_class = PerosnSerializer


    def get(self, request) :
        person = Person.objects.all()
        ser_data = PerosnSerializer(instance = person, many=True)
        return Response(data = ser_data.data)
    



class QuestionListView (APIView) :
    """
        This Will Show The Questions With Their Answers.
    """

    throttle_classes = [UserRateThrottle, AnonRateThrottle]
    serializer_class = QuestionSerializer

    def get (self, requset) :
        questions = Question.objects.all()
        ser_data = QuestionSerializer(instance=questions, many = True)
        return Response(data = ser_data.data, status=status.HTTP_200_OK)


class QuestionCreateView (APIView) :
    """
        This Is For Creating a Question.
    """

    permission_classes = [IsAuthenticated,]
    serializer_class = QuestionSerializer

    def post (self, request) :
        ser_data = QuestionSerializer(data = request.POST)
        if ser_data.is_valid() :
            ser_data.save()
            return Response(ser_data.data, status=status.HTTP_201_CREATED)
        return Response(ser_data.errors, status= status.HTTP_400_BAD_REQUEST)


class QuestionUpdateView(APIView) :
    """
        This For Updating a Question.
    """

    permission_classes = [IsOwnerOrReadOnly,]
    serializer_class = QuestionSerializer

    def put (self, request, pk) :
        question = Question.objects.get(pk=pk)
        self.check_object_permissions(request, question)
        ser_data = QuestionSerializer(instance=question, data=request.data, partial=True)
        if ser_data.is_valid() :
            ser_data.save()
            return Response(ser_data.data, status=status.HTTP_200_OK)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionDeleteView (APIView) :
    """
        This is For Deleting A Question.
    """
    permission_classes = [IsOwnerOrReadOnly]

    def delete (self, request, pk) :
        question = Question.objects.get(pk=pk)
        question.delete() 
        return Response({'message': 'question deleted.'}, status=status.HTTP_200_OK)
 

