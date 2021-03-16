from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html', {})


def add(request):
    from random import randint

    num_1 = randint(0, 10)
    num_2 = randint(0, 10)

    if request.method == "POST":
        answer = request.POST['answer']
        old_num_1 = request.POST['old_num_1']
        old_num_2 = request.POST['old_num_2']

        # Error Handling
        if not answer:
            my_answer = "Hey! you forget to fill out the form"
            color = 'danger'
            return render(request, 'subtract.html',
                          {
                              'color': color,
                              'my_answer': my_answer,
                              'num_1': num_1,
                              'num_2': num_2,
                          })

        correct = int(old_num_1) + int(old_num_2)
        if int(answer) == correct:
            my_answer = "Correct Answer.. Bravo! " + \
                old_num_1 + " + " + old_num_2 + " = " + answer
            color = "success"
        else:
            my_answer = "InCorrect Answer.. Try Again! " + old_num_1 + \
                " + " + old_num_2 + " is not equal " + \
                answer + " it is  " + str(correct)
            color = "danger"

        return render(request, 'add.html',
                      {
                          'answer': answer,
                          'my_answer': my_answer,
                          'num_1': num_1,
                          'num_2': num_2,
                          'color': color,


                      })
    return render(request, 'add.html', {
        'num_1': num_1,
        'num_2': num_2,
    })


def subtract(request):
    from random import randint

    num_1 = randint(0, 10)
    num_2 = randint(0, 10)

    if request.method == "POST":
        answer = request.POST['answer']
        old_num_1 = request.POST['old_num_1']
        old_num_2 = request.POST['old_num_2']

        # Error Handling
        if not answer:
            my_answer = "Hey! you forget to fill out the form"
            color = 'danger'
            return render(request, 'subtract.html',
                          {
                              'color': color,
                              'my_answer': my_answer,
                              'num_1': num_1,
                              'num_2': num_2,
                          })

        correct = int(old_num_1) - int(old_num_2)
        if int(answer) == correct:
            my_answer = "Correct Answer.. Bravo! " + \
                old_num_1 + " - " + old_num_2 + " = " + answer
            color = "success"
        else:
            my_answer = "InCorrect Answer.. Try Again! " + old_num_1 + \
                " - " + old_num_2 + " is not equal " + \
                answer + " it is  " + str(correct)
            color = "danger"

        return render(request, 'subtract.html',
                      {
                          'answer': answer,
                          'my_answer': my_answer,
                          'num_1': num_1,
                          'num_2': num_2,
                          'color': color,


                      })
    return render(request, 'subtract.html', {
        'num_1': num_1,
        'num_2': num_2,
    })


def multiply(request):
    from random import randint

    num_1 = randint(0, 10)
    num_2 = randint(0, 10)

    if request.method == "POST":
        answer = request.POST['answer']
        old_num_1 = request.POST['old_num_1']
        old_num_2 = request.POST['old_num_2']

        # Error Handling
        if not answer:
            my_answer = "Hey! you forget to fill out the form"
            color = 'danger'
            return render(request, 'multiply.html',
                          {
                              'color': color,
                              'my_answer': my_answer,
                              'num_1': num_1,
                              'num_2': num_2,
                          })

        correct = int(old_num_1) * int(old_num_2)
        if int(answer) == correct:
            my_answer = "Correct Answer.. Bravo! " + \
                old_num_1 + " * " + old_num_2 + " = " + answer
            color = "success"
        else:
            my_answer = "InCorrect Answer.. Try Again! " + old_num_1 + \
                " * " + old_num_2 + " is not equal " + \
                answer + " it is  " + str(correct)
            color = "danger"

        return render(request, 'multiply.html',
                      {
                          'answer': answer,
                          'my_answer': my_answer,
                          'num_1': num_1,
                          'num_2': num_2,
                          'color': color,


                      })
    return render(request, 'multiply.html', {
        'num_1': num_1,
        'num_2': num_2,
    })


def division(request):
    from random import randint

    num_1 = randint(0, 10)
    num_2 = randint(1, 10)

    if request.method == "POST":
        answer = request.POST['answer']
        old_num_1 = request.POST['old_num_1']
        old_num_2 = request.POST['old_num_2']

        # Error handling is not form is fill out
        if not answer:
            my_answer = "Hey! you forget to fill out the form"
            color = 'danger'
            return render(request, 'division.html',
                          {
                              'color': color,
                              'my_answer': my_answer,
                              'num_1': num_1,
                              'num_2': num_2,
                          })

        correct = int(old_num_1) / int(old_num_2)
        if float(answer) == correct:
            my_answer = "Correct Answer.. Bravo! " + \
                old_num_1 + " / " + old_num_2 + " = " + answer
            color = "success"
        else:
            my_answer = "InCorrect Answer.. Try Again! " + old_num_1 + \
                " / " + old_num_2 + " is not equal " + \
                answer + " it is  " + str(correct)
            color = "danger"

        return render(request, 'division.html',
                      {
                          'answer': answer,
                          'my_answer': my_answer,
                          'num_1': num_1,
                          'num_2': num_2,
                          'color': color,


                      })
    return render(request, 'division.html', {
        'num_1': num_1,
        'num_2': num_2,
    })
