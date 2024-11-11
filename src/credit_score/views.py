from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render

from .models import Answer, CreditScore, Question, UserResponse


@login_required(login_url="login")
def home(request):
    questions = Question.objects.all().prefetch_related("answers")
    context = {"questions": questions}
    return render(request, "questions.html", context=context)


@login_required(login_url="login")
def sumbit_form(request):
    if request.method == "POST":
        responses = request.POST.dict()
        del responses["csrfmiddlewaretoken"]

        total_score = 0

        for question_id, answer_id in responses.items():
            question = Question.objects.get(id=question_id)
            answer = Answer.objects.get(id=answer_id)

            UserResponse.objects.update_or_create(
                user=request.user, question=question, defaults={"answer": answer}
            )

            total_score += answer.score * question.weight
        CreditScore.objects.create(user=request.user, score=total_score)

        return JsonResponse({"score": total_score})


@login_required(login_url="login")
def result_page(request):
    user = request.user
    credit_score = CreditScore.objects.filter(user=user).order_by("-calculated_at")
    context = {"credit_score": credit_score}
    return render(request, "results.html", context=context)


# def sumbit_form(request):
#     if request.method == "POST":
#         responses = request.POST.dict()
#         del responses["csrfmiddlewaretoken"]

#         question_ids = list(responses.keys())
#         answer_ids = list(responses.values())

#         questions = {str(q.id): q for q in Question.objects.filter(id__in=question_ids)}
#         answers = {str(a.id): a for a in Answer.objects.filter(id__in=answer_ids)}

#         user_responses = []
#         total_score = 0

#         for question_id, answer_id in responses.items():
#             question = questions.get(question_id)
#             answer = answers.get(answer_id)

#             if not question or not answer:
#                 continue

#             user_responses.append(
#                 UserResponse(user=request.user, question=question, answer=answer)
#             )
#             total_score += answer.score * question.weight

#         UserResponse.objects.filter(
#             user=request.user, question_id__in=question_ids
#         ).delete()

#         UserResponse.objects.bulk_create(user_responses)

#         CreditScore.objects.create(user=request.user, score=total_score)

#         return JsonResponse({"status": "success", "score": total_score})
