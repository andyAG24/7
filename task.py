cook_book = {}
with open('book.txt') as f:

  fs = f.readlines()
  name_line = fs[0].replace('\n', '')
  i = int(fs[1].replace('\n', ''))
  fs[2].replace('\n', '')
  cook_book[name_line] = [{}]

  list_1 = []
  k = 0
  while k < i:
    recipe = {}
    ingredient_line = fs[2+k].replace('\n', '')
    ingr_list = ingredient_line.split('|')
    recipe['ingridient_name'] = ingr_list[0].replace(' ', '')
    recipe['quantity'] = int(ingr_list[1])
    recipe['measure'] = ingr_list[2].replace(' ', '')
    list_1.append(recipe)
    k += 1
  print('\n', list_1, '\n')
  cook_book[name_line] = list_1

  p = 2 + i + 1
  print(p)
  name_line = fs[p].replace('\n', '')
  print(name_line)
  num_line = int(fs[p+1].replace('\n', ''))

  print(p+num_line)
  list_2 = []
  k = 2 + i + 1
  while k < p + num_line:
    recipe = {}
    ingredient_line = fs[2+k].replace('\n', '')
    ingr_list = ingredient_line.split('|')
    recipe['ingridient_name'] = ingr_list[0].replace(' ', '')
    recipe['quantity'] = int(ingr_list[1])
    recipe['measure'] = ingr_list[2].replace(' ', '')
    list_2.append(recipe)
    k += 1
  cook_book[name_line] = list_2

  i1 = 2 + k + 1
  print(i1)
  name_line = fs[i1].replace('\n', '')
  print(name_line)
  num_line = int(fs[i1+1].replace('\n', ''))

  list_3 = []
  k1 = 2 + k + 1
  while k1 < i1 + num_line:
    recipe = {}
    ingredient_line = fs[2+k1].replace('\n', '')
    ingr_list = ingredient_line.split('|')
    recipe['ingridient_name'] = ingr_list[0].replace(' ', '')
    recipe['quantity'] = int(ingr_list[1])
    recipe['measure'] = ingr_list[2].replace(' ', '')
    list_3.append(recipe)
    k1 += 1
  cook_book[name_line] = list_3

  i2 = 2 + i1 + 1 + i
  print(i2)
  name_line = fs[i2].replace('\n', '')
  print(name_line)
  num_line = int(fs[i2+1].replace('\n', ''))

  list_4 = []
  k2 = 2 + i1 + 1 + i
  while k2 < i2 + num_line:
    recipe = {}
    ingredient_line = fs[2+k2].replace('\n', '')
    ingr_list = ingredient_line.split('|')
    recipe['ingridient_name'] = ingr_list[0].replace(' ', '')
    recipe['quantity'] = int(ingr_list[1])
    recipe['measure'] = ingr_list[2].replace(' ', '')
    list_4.append(recipe)
    k2 += 1
  cook_book[name_line] = list_4

  def get_shop_list_by_dishes(dishes, person_count):
    di = str(dishes).replace("['", "").replace("']", "")
    for key in cook_book.keys():
      if key == di:
        i = 0
        recipe = {}
        while i < len(cook_book[key]):
          product = cook_book[key][i]['ingridient_name']
          recipe[product] = {}
          recipe[product]['quantity'] = cook_book[key][i]['quantity'] * person_count
          recipe[product]['measure'] = cook_book[key][i]['measure']
          i += 1
        print(recipe)
  print('\n')

  dish_name = input('Enter name:')
  person_amount = int(input('Enter amount of persons:'))
  get_shop_list_by_dishes([dish_name], person_amount)


    