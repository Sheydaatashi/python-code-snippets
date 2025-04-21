student_score={
    'sara':15,
    'ali':10,
    'zahra':17,
    'mehdi':9,
    'mohamad':19
}

top_student=max(student_score,key=student_score.get)
top_student=student_score[top_student]

print(top_student)