# Views # 


## Регистрация ##

url - /user/registration<br>
post-запрос<br>
url принимает данные name, который будет отображаться при выводе пунктов списка.
login - для идентификации юзера. 
Password и repeat_password - не менее 8 знаков(латинские буквы и цифры)


## Аутентификация ##

url - /user/authentication<br>
post-запрос<br>
json-request-data: login, password<br>
jwt-авторизация в payload сохранять login юзера.  


## Удалить пользователя ##
Только авторизованный пользователь<br>
url - /user/delete-user<br>
delete-запрос<br>
json-request-data: password<br>
из payload берётся login юзера, сравниваются пароли. 


## Редактировать пользователя ##
Только авторизованный пользователь<br>
url - /user/edit-user<br>
put-запрос<br>
json-request-data:<br>
  в зависимости что надо изменить: name, login, new_password(в т.ч. repeat_new_password)<br>
  обязательное: password(текущий пароль)<br>
из payload берётся login юзера, сравниваются пароли. 


## Просмотр профиль пользователя ##

url - /user/profile/user=(логин пользователя)<br>
get-запрос<br>


## Просмотр профиль текущего пользователя ##
Только авторизованный пользователь<br>
url - /user/profile/current<br>
get-запрос<br>
из payload берётся login юзера. 

## Все списки покупок имеющие у пользователя ##
Только авторизованный пользователь<br>
url - /user/shopping-lists/all<br>
get-запрос<br>
из payload берётся login юзера, сравниваются пароли. 
