from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.views.generic import ListView
import datetime
import yaml
from django.template import Template, Context
import re
from .DSL.subset import *
from .DSL.verify import *


def regex_verify1(request):
    fp = open('template.html')
    t = Template(fp.read())
    fp.close()
    N = "1"
    with open('NE/experiment.yaml', 'r') as e:
        examples = yaml.load(e.read())
    requirement = examples[N][0]
    regex = examples[N][1]

    # test update 
    test = examples[N][2]
    testset = test.split(" ")
    newtest = ""
    for item in testset:
    	if re.match(regex, item):
    		newtest += "<mark>" + item + "</mark> "
    	else:
    		newtest += item + " "
    newtest = newtest.replace(" ", "<br>")

    # requirement/specification update
    requirementset = re.split("[\.|\,]", requirement)
    newrequirement = ""
    for r in requirementset:
        newrequirement += r + "<br>"
    result = verifyNL(requirementset, regex)
    newspecification = result[1]
    flag_V = result[0]
    if flag_V == "Verified":
        newspecification = newspecification + "<br>" + "<span style='background-color:green'>" + flag_V + "</span>"
    else:
        newspecification = newspecification + "<br>" + "<span style='background-color:red'>" + "Failed<br>" + flag_V + "</span>"

    html = t.render(Context({'regex': regex, 'test': newtest, 'specification': newspecification}))
    return HttpResponse(html)


def validate(request):
    fp = open('template.html')
    t = Template(fp.read())
    fp.close()
    regex = "Enter regex!"
    newtest = "Enter tests!"
    newrequirement = "Enter requirements!"
    newspecification = "Results"

    html = t.render(Context({'regex': regex, 'test': newtest, 'requirement': newrequirement,'specification': newspecification}))
    return HttpResponse(html)

def error_handler(request):
    fp = open('template.html')
    t = Template(fp.read())
    fp.close()
    regex = "Error! Please enter again!"
    newtest = "Error! Please enter again!"
    newrequirement = "Error! Please enter again!"
    newspecification = "Results"

    html = t.render(Context({'regex': regex, 'test': newtest, 'requirement': newrequirement,'specification': newspecification}))
    return HttpResponse(html)

def submit(request):
    if 'requirement' in request.GET:
        requirement = request.GET['requirement']
    else: 
        requirement = "Error input!"
        error_handler(request)
        return
    if 'regex' in request.GET:
        regex = request.GET['regex']
    else:
        regex = "Error input!"
        error_handler(request)
        return
    if 'tests' in request.GET:
        test = request.GET['tests']
    else:
        test = "Error input!"
        error_handler(request)
        return

    fp = open('after.html')
    t = Template(fp.read())
    fp.close()
    N = "1"
    with open('NE/experiment.yaml', 'r') as e:
        examples = yaml.load(e.read())
    testset = test.split(" ")
    newtest = ""
    for item in testset:
        if re.match(regex, item):
            newtest += "<mark>" + item + "</mark> "
        else:
            newtest += item + " "
    newtest = newtest.replace(" ", "<br>")

    # requirement/specification update
    # specificationset = examples[N][3].split("&&")
    requirementset = re.split("[\.|\,]", requirement)
    newrequirement = ""
    for r in requirementset:
        newrequirement += r + "<br>"
    result = verifyNL(requirementset, regex)
    newspecification = result[1]
    flag_V = result[0]
    if flag_V == "Verified":
        newspecification = newspecification + "<br>" + "<span style='background-color:green'>" + flag_V + "</span>"
    else:
        newspecification = newspecification + "<br>" + "<span style='background-color:red'>" + "Failed<br>""</span>" + "Counter Example<br>"+flag_V 

    html = t.render(Context({'regex': regex, 'test': newtest, 'requirement': newrequirement, 'specification': newspecification}))
    return HttpResponse(html)

def example(request):
    if 'your' in request.GET:
        fp = open('template.html')
        t = Template(fp.read())
        fp.close()
        regex = "Enter regex!"
        newtest = "Enter tests!"
        newrequirement = "Enter requirements!"
        newspecification = "Results"
        html = t.render(Context({'regex': regex, 'test': newtest, 'requirement': newrequirement,'specification': newspecification}))
        return HttpResponse(html)   
    if 'bigregex' in request.GET:
        fp = open('bigregex.html')
        t = Template(fp.read())
        fp.close()
        html = t.render(Context())
        return HttpResponse(html)
    if 'example1' in request.GET:
        n = "1"
    if 'example2' in request.GET:
        n = "2"
    if 'example3' in request.GET:
        n = "3"
    if 'example4' in request.GET:
        n = "4"
    if 'example5' in request.GET:
        n = "5"
    fp = open('after.html')
    t = Template(fp.read())
    fp.close()
    with open('NE/experiment.yaml', 'r') as e:
        examples = yaml.load(e.read())

    requirement = examples[n][0]
    regex = examples[n][1]

    # test update 
    test = examples[n][2]
    testset = test.split(" ")
    newtest = ""
    for item in testset:
        if re.match(regex, item):
            newtest += "<mark>" + item + "</mark> "
        else:
            newtest += item + " "
    newtest = newtest.replace(" ", "<br>")

    # requirement/specification update
    requirementset = re.split("[\.|\,]", requirement)
    newrequirement = ""
    for r in requirementset:
        newrequirement += r + "<br>"
    result = verifyNL(requirementset, regex)
    newspecification = result[1]
    flag_V = result[0]
    if flag_V == "Verified":
        newspecification = newspecification + "<br>" + "<span style='background-color:green'>" + flag_V + "</span>"
    else:
        newspecification = newspecification + "<br>" + "<span style='background-color:red'>" + "Failed<br>" + flag_V + "</span>"

    html = t.render(Context({'regex': regex, 'test': newtest, 'requirement': newrequirement, 'specification': newspecification}))
    return HttpResponse(html)

def regex_verify2(request):
    fp = open('template.html')
    t = Template(fp.read())
    fp.close()
    N = "2"
    with open('NE/experiment.yaml', 'r') as e:
        examples = yaml.load(e.read())
    requirement = examples[N][0]
    regex = examples[N][1]

    # test update 
    test = examples[N][2]
    testset = test.split(" ")
    newtest = ""
    for item in testset:
    	if re.match(regex, item):
    		newtest += "<mark>" + item + "</mark> "
    	else:
    		newtest += item + " "
    newtest = newtest.replace(" ", "<br>")

    # requirement/specification update
    specificationset = examples[N][3].split("&&")
    requirementset = re.split("[\.|\,]", requirement)
    newrequirement = ""
    for item in requirementset:
   		newrequirement += item + "<br>"

    # specification translate
    newspecification = ""
    for item in specificationset:
    	if True:
    		newspecification += item + "<br>"
    	else:
    		newspecification += "<span style='background-color:red'>" + item + "</span>" + "<br>"

    html = t.render(Context({'regex': regex, 'test': newtest, 'requirement': newrequirement, 'specification': newspecification}))
    return HttpResponse(html)

def request_page(request):
    if 'mybtn' in request.POST:
        # print request.GET.get('getrequirement')
        fp = open('template.html')
        t = Template(fp.read())
        fp.close()
        N = "1"
        with open('NE/experiment.yaml', 'r') as e:
            examples = yaml.load(e.read())
        requirement = examples[N][0]
        regex = examples[N][1]

        # test update 
        test = examples[N][2]
        testset = test.split(" ")
        newtest = ""
        for item in testset:
            if re.match(regex, item):
                newtest += "<mark>" + item + "</mark> "
            else:
                newtest += item + " "
        newtest = newtest.replace(" ", "<br>")

        # requirement/specification update
        specificationset = examples[N][3].split("&&")
        requirementset = re.split("[\.|\,]", requirement)
        newrequirement = ""
        for item in requirementset:
            newrequirement += item + "<br>"

        # specification translate
        newspecification = ""
        for item in specificationset:
            if True:
                newspecification += item + "<br>"
            else:
                newspecification += "<span style='background-color:red'>" + item + "</span>" + "<br>"

        html = t.render(Context({'regex': regex, 'test': newtest, 'requirement': newrequirement, 'specification': newspecification}))
        return HttpResponse(html)
         
