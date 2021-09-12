from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from django.template.loader import render_to_string

from .forms import *
from django.contrib.auth import authenticate, login, logout
from datetime import datetime
from django.core.serializers.json import DjangoJSONEncoder


# Create your views here.


def home(request):
    if request.user.is_authenticated:
        quizzes = Quiz.objects.all()
        return render(request, 'Task/home.html', {'quizzes': quizzes})
    else:
        form = RegForm
        return render(request, 'Task/home.html', {'form': form})


def student_signup(request):
    if request.method == "POST":
        form = RegForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = 2
            user.save()
            return redirect('home')
        else:
            return render(request, 'Task/home.html', {'form': form})


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("INVALID CREDENTIALS")


def logout_user(request):
    logout(request)
    return redirect('home')


def add_quiz_home(request):
    if request.method == "POST":
        form = QuizForm(request.POST)
        if form.is_valid():
            quiz1 = form.save()
            request.session['quiz_id'] = quiz1.id
            return redirect('view questions')
    else:
        form = QuizForm
    return render(request, 'Task/quiz.html', {'form': form})


def view_questions(request):
    quiz_id = request.session['quiz_id']
    questions1 = Question.objects.filter(quiz_ref=quiz_id)
    if questions1.count() < 10:
        add_ques = 1
    else:
        add_ques = 0
    return render(request, 'Task/all_questions_in_quiz.html', {'questions': questions1, 'add_ques': add_ques})


def add_question(request):
    quiz_id = request.session['quiz_id']
    questions1 = Question.objects.filter(quiz_ref=quiz_id)
    if request.method == "POST":
        c = questions1.count() + 1
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.quiz_ref_id = quiz_id
            question.num = c
            question.save()
            if c < 11:
                return redirect('add questions')
            else:
                return redirect('home')
    else:
        form = QuestionForm
    return render(request, 'Task/add_edit_question.html', {'form': form, 'questions': questions1})


def update_question(request, pk):
    quiz_id = request.session['quiz_id']
    all_questions = Question.objects.filter(quiz_ref=quiz_id)
    ques = Question.objects.get(pk=pk)
    if request.method == "POST":
        c = all_questions.count() + 1
        form = QuestionForm(request.POST, instance=ques)
        if form.is_valid():
            question = form.save(commit=False)
            question.save()
            return redirect('view questions')
    else:
        form = QuestionForm(instance=ques)
    return render(request, 'Task/add_edit_question.html', {'form': form, 'questions': all_questions})


def delete_question(request, pk):
    Question.objects.get(pk=pk).delete()
    return redirect('view questions')


def update_quiz(request, pk):
    request.session['quiz_id'] = pk
    return redirect('view questions')


def quiz_attend_list(request):
    quizzes = Quiz.objects.all()
    return render(request, 'Task/quiz_attend_list.html', {'quizzes': quizzes})


def start_quiz(request, pk):
    request.session['quiz_id'] = pk
    request.session['marks'] = 0
    tq = Question.objects.filter(quiz_ref=pk).count()
    if tq == 0:
        return HttpResponse('OOPS NO QUESTION IS HERE')
    else:
        return render(request, 'Task/quiz_start_home.html')


def attend_question(request):
    quiz_id = request.session['quiz_id']
    all_questions = Question.objects.filter(quiz_ref=quiz_id).order_by('pk')
    first_question = all_questions.first()
    request.session['question_id'] = first_question.id
    return render(request, 'Task/question.html', {'question': first_question})


def next_question(request):
    question_id = request.session['question_id']
    quiz_id = request.session['quiz_id']
    data = dict()
    cur_question = Question.objects.filter(quiz_ref=quiz_id, id__gt=question_id).order_by('id').first()
    if cur_question:
        request.session['question_id'] = cur_question.id
        context = {'question': cur_question}
        data['next_question'] = True
        data['question'] = render_to_string('Task/question_content.html', context, request)
    else:
        data['next_question'] = False
        total_questions = Question.objects.filter(quiz_ref=quiz_id).count()
        correct_answers = AnswerEntries.objects.filter(whether_answered_right=True, ques_ref__quiz_ref=quiz_id).count()
        context = {'total_questions': total_questions, 'correct_answers': correct_answers}
        data['result'] = render_to_string('Task/result.html', context, request=request)
    return JsonResponse(data)


def show_result(request):
    return render(request, 'Task/result.html')


def show_answer(request):
    user = request.user
    que_id = request.session['question_id']
    question = Question.objects.get(pk=que_id)
    if question.is_multiple_correct:
        opt1 = int(request.GET.get('opt1'))
        opt2 = int(request.GET.get('opt2'))
        opt3 = int(request.GET.get('opt3'))
        opt4 = int(request.GET.get('opt4'))
        f = 1
        if question.is_ans_option_1:
            if opt1 != 1:
                f = 0
        else:
            if opt1 != 0:
                f = 0
        if f == 1:
            if question.is_ans_option_2:
                if opt2 != 1:
                    f = 0
            else:
                if opt2 != 0:
                    f = 0
        if f == 1:
            if question.is_ans_option_3:
                if opt3 != 1:
                    f = 0
            else:
                if opt3 != 0:
                    f = 0
        if f == 1:
            if question.is_ans_option_4:
                if opt4 != 1:
                    f = 0
            else:
                if opt4 != 0:
                    f = 0
        if f == 1:
            result = "CORRECT"
        else:
            result = "WRONG"
    else:
        ans = request.GET.get('ans')
        result = "WRONG"
        if question.is_ans_option_1:
            if ans == "option1":
                result = "CORRECT"
            else:
                result = "WRONG"
        elif question.is_ans_option_2:
            if ans == 'option2':
                result = "CORRECT"
            else:
                result = "WRONG"
        elif question.is_ans_option_3:
            if ans == 'option3':
                result = "CORRECT"
            else:
                result = "WRONG"
        elif question.is_ans_option_4:
            if ans == 'option4':
                result = "CORRECT"
            else:
                result = "WRONG"
    if result == "CORRECT":
        AnswerEntries.objects.update_or_create(ques_ref=question, user_ref=user,
                                               defaults={'whether_answered_right': True})
    else:
        AnswerEntries.objects.update_or_create(ques_ref=question, user_ref=user,
                                               defaults={'whether_answered_right': False})
    return render(request, 'Task/answer.html', {'question': question, 'result': result})
