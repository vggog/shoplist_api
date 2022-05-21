# Views # 


## Регистрация ##

url - /user/registration<br>
post-запрос<br>
json-requests-data: name(не уникальный), login(строго уникальный), password, repeat-password


## Аутентификация ##

url - /user/authentication<br>
post-запрос<br>
json-request-data: login, password


## Удалить пользователя ##
Только авторизованный пользователь<br>
url - /user/delete-user<br>
delete-запрос<br>
json-request-data: password


## Редактировать пользователя ##
Только авторизованный пользователь<br>
url - /user/edit-user<br>
put-запрос<br>
json-request-data:<br>
  в зависимости что надо изменить: name, login, new_password(в т.ч. repeat_new_password)<br>
  обязательное: password(текущий пароль)


## Просмотр профиля пользователя ##

url - /user/profile/user=(логин пользователя)<br>
get-запрос<br>


## Просмотр профиля текущего пользователя ##
Только авторизованный пользователь<br>
url - /user/profile/current<br>
get-запрос<br>

## Все списки покупок имеющие у пользователя ##
Только авторизованный пользователь<br>
url - /user/shopping-lists/all<br>
get-запрос
