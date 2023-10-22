def convert_word_to_integer(mobile_number):
  mobile_number_dict = {
      "zero": "0",
      "one": "1",
      "two": "2",
      "three": "3",
      "four": "4",
      "five": "5",
      "six": "6",
      "seven": "7",
      "eight": "8",
      "nine": "9",
  }

  integer_mobile_number = ""
  for word in mobile_number.split():
      integer_mobile_number += mobile_number_dict[word]

  return integer_mobile_number

mobile_number_in_words = "eight eight three zero eight one five one eight two"
integer_mobile_number = convert_word_to_integer(mobile_number_in_words)

print(integer_mobile_number)