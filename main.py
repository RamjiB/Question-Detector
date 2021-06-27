import question_detection as qd

isQ = qd.IsQuestion()
pred = isQ.predict_question('How are you')
print(pred)

pred = isQ.predict_question('Yes, I am good')
print(pred)