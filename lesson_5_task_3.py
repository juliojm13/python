tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена','Пося'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А'
]

# def tutors_class_ (tutors , klasses):
#     for tutor in tutors:
#         if tutors.index(tutor) < len(klasses):
#            result = (tutor, klasses[tutors.index(tutor)])
#         else:
#             result = (tutor, None)
#         yield result


tutor_class = ( (tutor , klasses [tutors.index(tutor)]) if tutors.index(tutor) < len(klasses) else (tutor , None) for tutor in tutors)
#tutor_class = tutors_class_(tutors,klasses)
print(tutor_class)
print(next(tutor_class))
print(next(tutor_class))
print(next(tutor_class))
print(next(tutor_class))
print(next(tutor_class))
print(next(tutor_class))
print(next(tutor_class))
print(next(tutor_class))
