def user_info(name: str, surname: str, born_year: int, city: str, email: str, tel: str):
    """
    This func for print user info
    :param :name is str
    :param :surname is str
    :param :born_year is int
    :param :city is str
    :param :email is str
    :param :tel is str
    :param :print is str
    """
    user_info = name + str(', ')\
                + surname + str(', ') + str(born_year)\
                + str(', ') + city + str(', ') + email\
                + str(', ') + tel
    print(user_info)

name = 'Иван'
surname = 'Иванов'
born_year = 1988
city = 'Москва'
email = 'ivan@ivan.ru'
tel = '+7777777777'

user_info(name, surname, born_year, city, email, tel)
