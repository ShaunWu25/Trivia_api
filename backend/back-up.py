try:
  # get my request body
  body = request.get_json()

  if not ('quiz_category' in body and 'previous_questions' in body):
      abort(422)

  # get the category and previous questions
  category = body.get('quiz_category')
  previous  = body.get('previous_questions')

  if ((category is None) or (previous is None)):
      abort(400)

  # load all questions if "ALL" is selected
  if category['type'] == 'click':
      questions = Question.query.filter(Question.id.notin_((previous))).all()
  # load questions for selected category
  else:
      questions = Question.query.filter_by(category=category['id']).filter(Question.id.notin_((previous))).all()

  # get a random question
  question = questions[random.randrange(0, len(questions))].format() if len(questions) > 0 else None

  # return the question
  return jsonify({
      'success': True,
      'question': question.format()
  })

except:
  abort(422)