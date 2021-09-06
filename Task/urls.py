from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('add-quiz/', add_quiz_home, name='add quiz'),
    path('add-quiz/view-questions', view_questions, name='view questions'),
    path('add-quiz/add-questions', add_question, name='add questions'),
    path('add-quiz/update-question/<int:pk>', update_question, name='update question'),
    path('add-quiz/delete-question/<int:pk>', delete_question, name='delete question'),
    path('update-quiz/<int:pk>', update_quiz, name='update quiz'),
    path('attend-quiz-list/', quiz_attend_list, name="quiz attend list"),
    path('start-quiz/<int:pk>', start_quiz, name='start quiz'),
    path('start-quiz/', attend_question, name='attend quiz'),
    path('show-answer/', show_answer, name='show answer'),
    path('next-question/', next_question, name='next question'),
    path('attend-quiz/result/', show_result, name='show result'),
    path('logout/', logout_user, name="logout"),
    path('signup/', student_signup, name='student signup'),
    path('login/', user_login, name='user login'),
    # path('attend-quiz/<int:pk>/<int:pk>', view_question, name='view question')
]