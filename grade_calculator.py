class Grade_Calculator:

  def __init__(self):
    self.grade = 0.0
    self.grade_list = []
    self.weight_list = []

  
  def current_grade(self, user_input):

    self.grade_list = []
    self.weight_list = []
    
    if not user_input:
      return "No Grades Given"
    elif len(user_input) % 2 == 1:
      return "More Grades given then weights"

    return self.fill_lists(user_input)

  
  def fill_lists(self, user_input):
    
    for grade_index in range(0, len(user_input), 2):
      self.grade_list.append(float(user_input[grade_index]))
      self.weight_list.append(float(user_input[grade_index + 1]))

    if sum(self.weight_list) == 100.0:
      self.get_mean()
    elif sum(self.weight_list) < 100.0:
      self.get_curr_mean()
    else:
      return "Sum of weights is more than 100"

    return "Your current grade is " + str(self.grade)

  
  def get_curr_mean(self):
    weight_multiplier = 100.0 / sum(self.weight_list)
    self.grade = 0.0

    for i in range(len(self.grade_list)):
      self.grade += (self.grade_list[i] / 100) * (self.weight_list[i] * weight_multiplier)
    
    return self.grade

    
  def get_mean(self):
    self.grade = 0.0

    for i in range(len(self.grade_list)):
      self.grade += (self.grade_list[i] / 100) * self.weight_list[i]

    return self.grade
